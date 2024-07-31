from os import environ, path
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
base_dir = path.abspath(path.dirname("__file__"))
load_dotenv(path.join(base_dir, "config/.env"))


class Config:
    """Clase para manejar la configuración de la aplicación."""

    # Configuración general
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    if not FLASK_APP or not FLASK_ENV:
        raise EnvironmentError(
            "Las variables de entorno FLASK_APP y FLASK_ENV son requeridas."
        )
