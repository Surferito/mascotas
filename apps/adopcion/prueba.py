
from datetime import datetime

class ChipiCabify(object):
    """
    funciona hasta 40km, no incluye espera
    """

    def __init__(self, distance):
        self.distance = distance
        self.is_weekend = datetime.today().weekday() > 4 or (
            datetime.today().weekday() == 4 and 22 <= datetime.now().hour)
        self.estimate_price = self._calculate()

    def _calculate(self):
        price_km = self.distance * 1.65
        if price_km < 6:
            price_km = 6
        if self.distance > 20:
            resta = self.distance - 20
            price_km = resta * 1.10 + 33
        if self.is_weekend and price_km < 8:
            price_km = 8
        return format(price_km, '.2f')

    def get_estimate_price(self):
        return self.estimate_price

trayecto1 = ChipiCabify(7)
print(trayecto1._calculate())
trayecto2 = ChipiCabify(4)
print(trayecto2._calculate())