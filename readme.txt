1-Abrir cmd en el directorio donde tengamos la API
2-Activar entorno virtual -> Scripts\activate.bat (en windows) o /bin/activate (linux)    
3-Instalar requerimientos -> pip install -r requirements (fastapi,uvicorn,sqlalchemy,mysql-connector-python,passlib,bcrypt,python-jose,python-multipart)
4-Crear una base de datos mysql con nombre db en un entorno local con xampp
5-Correr servidor unicorn -> uvicorn main:app --reload
6-Abrir swagger -> http://127.0.0.1:8000/docs#/