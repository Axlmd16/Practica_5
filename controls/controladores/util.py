import pandas as pd
import numpy as np


class Util:

    def haversine(lon1, lat1, lon2, lat2):

        lon1 = np.radians(lon1.astype(float))
        lat1 = np.radians(lat1.astype(float))
        lon2 = np.radians(lon2.astype(float))
        lat2 = np.radians(lat2.astype(float))

        r = 6371

        dlon = np.subtract(lon2, lon1)
        dlat = np.subtract(lat2, lat1)

        a = np.add(
            np.power(np.sin(np.divide(dlat, 2)), 2),
            np.multiply(
                np.cos(lat1),
                np.multiply(np.cos(lat2), np.power(np.sin(np.divide(dlon, 2)), 2)),
            ),
        )
        c = np.multiply(2, np.arcsin(np.sqrt(a)))

        return c * r
