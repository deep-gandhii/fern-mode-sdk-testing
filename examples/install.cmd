python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\fern-0.0.2-py3-none-any.whl --force-reinstall
