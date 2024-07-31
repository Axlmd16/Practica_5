import math

from controls.dao.data_access_object import Data_Access_Object
from models.parada_bus import ParadaBus


class ParadaControl(Data_Access_Object):
    def __init__(self):
        super().__init__(ParadaBus)
        self.__parada = None

    @property
    def _parada(self):
        if self.__parada is None:
            self.__parada = ParadaBus()
        return self.__parada

    @_parada.setter
    def _negocio(self, value):
        self.__parada = value

    def save(self):
        self._parada._id = self._generate_id()
        self._save(self._parada)
        self.__parada = None

    def list(self):
        return self._list()

    def update(self, pos):
        self._merge(self._parada, pos)
        self.__parada = None

    def get_distance(self, lat1, lon1, lat2, lon2):
        lat1 = float(lat1)
        lon1 = float(lon1)
        lat2 = float(lat2)
        lon2 = float(lon2)

        rad = math.pi / 180
        earth_radius_km = 6378.137

        dlat = (lat2 - lat1) * rad
        dlon = (lon2 - lon1) * rad

        a = (
                math.sin(dlat / 2) ** 2
                + math.cos(lat1 * rad) * math.cos(lat2 * rad) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_km = earth_radius_km * c

        # return round(distance_km * 1000, 3)  # Devuelve la distancia en metros
        return round(distance_km, 3)
