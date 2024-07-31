class ParadaBus:
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__direccion = "s/n"
        self.__longitud = "0.0"
        self.__latitud = "0.0"

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _longitud(self):
        return self.__longitud

    @_longitud.setter
    def _longitud(self, value):
        self.__longitud = value

    @property
    def _latitud(self):
        return self.__latitud

    @_latitud.setter
    def _latitud(self, value):
        self.__latitud = value

    def __str__(self) -> str:
        return f"{self._id}, {self._nombre}"

    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "direccion": self._direccion,
            "longitud": self._longitud,
            "latitud": self._latitud,
        }

    def deserializable(data: dict):
        paradaBus = ParadaBus()
        paradaBus._id = data["id"]
        paradaBus._nombre = data["nombre"]
        paradaBus._direccion = data["direccion"]
        paradaBus._longitud = data["longitud"]
        paradaBus._latitud = data["latitud"]
        return paradaBus
