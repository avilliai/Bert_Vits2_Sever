cd venv/Scripts
rem 激活虚拟环境
call activate.bat
cd ../..
pip install flask[async]
pause