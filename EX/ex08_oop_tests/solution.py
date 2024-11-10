class Factory:
    def __init__(self):
        pass

    def bake_cake(self, toppings: int, base: int) -> int:
        if toppings and base > 10:

        if toppings == base:
            return toppings
        # if 1 < toppings < 4 and 1 < base < 4:

        # difference = toppings - base



    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount):
        self._type = None
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount

    @property
    def type(self):
        return self._type

    def __str__(self):
        return f'{self.base_amount} something {self.toppings_amount}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.base_amount == other.base_amount and self.toppings_amount == other.toppings_amount


class WrongIngredientsAmountException(Exception):
    pass

