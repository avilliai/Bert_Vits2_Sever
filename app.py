# -*- coding: utf-8 -*-
import json
import sys, os

import yaml
from flask import request, Flask, send_file
from scipy.io import wavfile

if sys.platform == "darwin":
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import logging

logging.getLogger("numba").setLevel(logging.WARNING)
logging.getLogger("markdown_it").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("matplotlib").setLevel(logging.WARNING)

logging.basicConfig(level=logging.INFO, format="| %(name)s | %(levelname)s | %(message)s")

logger = logging.getLogger(__name__)

import torch
import argparse
import commons
import utils
from models import SynthesizerTrn
from text.symbols import symbols
from text import cleaned_text_to_sequence, get_bert
from text.cleaner import clean_text
import gradio as gr
import webbrowser


net_g = None


def get_text(text, language_str, hps):
    norm_text, phone, tone, word2ph = clean_text(text, language_str)
    phone, tone, language = cleaned_text_to_sequence(phone, tone, language_str)

    if hps.data.add_blank:
        phone = commons.intersperse(phone, 0)
        tone = commons.intersperse(tone, 0)
        language = commons.intersperse(language, 0)
        for i in range(len(word2ph)):
            word2ph[i] = word2ph[i] * 2
        word2ph[0] += 1
    bert = get_bert(norm_text, word2ph, language_str)
    del word2ph

    assert bert.shape[-1] == len(phone)

    phone = torch.LongTensor(phone)
    tone = torch.LongTensor(tone)
    language = torch.LongTensor(language)

    return bert, phone, tone, language

def infer(text, lang,sdp_ratio, noise_scale, noise_scale_w, length_scale, sid):
    global net_g
    bert, phones, tones, lang_ids = get_text(text, "ZH", hps)
    with torch.no_grad():
        x_tst=phones.to(device).unsqueeze(0)
        tones=tones.to(device).unsqueeze(0)
        lang_ids=lang_ids.to(device).unsqueeze(0)
        bert = bert.to(device).unsqueeze(0)
        x_tst_lengths = torch.LongTensor([phones.size(0)]).to(device)
        del phones
        speakers = torch.LongTensor([hps.data.spk2id[sid]]).to(device)
        audio = net_g.infer(x_tst, x_tst_lengths, speakers, tones, lang_ids, bert, sdp_ratio=sdp_ratio
                           , noise_scale=noise_scale, noise_scale_w=noise_scale_w, length_scale=length_scale)[0][0,0].data.cpu().float().numpy()
        del x_tst, tones, lang_ids, bert, x_tst_lengths, speakers
        return audio

async def tts_fn(text, speaker,path, lang,sdp_ratio=0.2, noise_scale=0.6, noise_scale_w=0.8, length_scale=1.2):
    with torch.no_grad():
        audio = infer(text, lang,sdp_ratio=sdp_ratio, noise_scale=noise_scale, noise_scale_w=noise_scale_w, length_scale=length_scale, sid=speaker)
        wavfile.write(path, hps.data.sampling_rate, audio)
    return "Success", (hps.data.sampling_rate, audio)
app1 = Flask(__name__)
@app1.route('/synthesize', methods=['POST'])
async def synthesize():
    # 解析请求中的参数
    data = request.get_json()
    data = json.loads(data)
    with open('config/settings.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    speaker = data['speaker']
    text = data['text']
    out = data["out"]

    mes=result.get(speaker)

    model=mes.get("model")
    lang=mes.get("lang")


    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", default=model[0], help="path of your model")
    parser.add_argument("--config_dir", default=model[1], help="path of your config file")
    parser.add_argument("--share", default=False, help="make link public")
    parser.add_argument("-d", "--debug", action="store_true", help="enable DEBUG-LEVEL log")

    args = parser.parse_args()
    if args.debug:
        logger.info("Enable DEBUG-LEVEL log")
        logging.basicConfig(level=logging.DEBUG)
    global hps
    hps = utils.get_hparams_from_file(args.config_dir)
    global device
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    global net_g
    net_g = SynthesizerTrn(
        len(symbols),
        hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        n_speakers=hps.data.n_speakers,
        **hps.model).to(device)
    _ = net_g.eval()

    _ = utils.load_checkpoint(args.model_dir, net_g, None, skip_optimizer=True)

    speaker_ids = hps.data.spk2id
    speakers = list(speaker_ids.keys())

    await tts_fn(text, speaker, out,lang)
    print("ok")
    return send_file(out, as_attachment=True)

if __name__ == "__main__":


    if os.path.exists("logss/azusa/config.json"):
        print(1)

#    webbrowser.open("http://127.0.0.1:6006")
#    app.launch(server_port=6006, show_error=True)

    #app.launch(show_error=True)
    app1.run(debug=True, host='127.0.0.1', port=9080)