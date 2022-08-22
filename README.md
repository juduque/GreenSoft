# GreenSoft

- Astra
- Prerequisitos
- Como ejecutar la app local
- Como probarla local mente
- Como abrirla cuando esta en ejecución

# init project in local environment linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload