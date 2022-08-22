# GreenSoft

- Autores: Grupo Astra

- Prerequisitos:
    Python 3.10

- Como ejecutar la app local:

    ### Clonar el repositorio 
    git clone https://github.com/juduque/GreenSoft.git

    ### Inciar projecto en un ambiente de Linux
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    ### iniciar projecto en un ambiente de Windows 
    python3 -m venv .venv
    source .venv\Scripts\activate.bat
    pip install -r requirements.txt


- Como probarla localmente
    Cuando el ambiente se encuentra creado y se hayan intalado los requrimientos,
    ejecutar en la terminal el siguiente comando (Es importante estar parado en la 
    raiz del projecto)

        uvicorn main:app --reload

- Como abrirla cuando esta en ejecución

    En el buscador (Chome, firefox, edge), ingresar a la siguiente url

    http://localhost:8000/docs