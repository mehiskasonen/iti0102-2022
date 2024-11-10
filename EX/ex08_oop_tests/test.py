import random
import pytest
from solution import Factory, Cake, WrongIngredientsAmountException

@pytest.fixture
def factory() -> Factory:
    return Factory()


def test_produce_cake_only_basic(factory):
    amount = factory.bake_cake(1, 1)
    assert amount == 1


@pytest.mark.dependency()
def test_produce_cake_only_medium(factory):
    assert factory.bake_cake(2, 2) == 1
    assert factory.bake_cake(4, 4) == 2


@pytest.mark.dependency()
def test_produce_cake_only_large(factory):
    assert factory.bake_cake(5, 5) == 1
    assert factory.bake_cake(10, 10) == 2


@pytest.mark.dependency(depends=["test_produce_cake_only_medium"])
def test_produce_cake_medium_remaining_ingredients_produce_more_cakes(factory):
    assert factory.bake_cake(3, 3) != 1  # 0
    assert factory.bake_cake(5, 5) != 2  # 1


@pytest.mark.dependency(depends=["test_produce_cake_only_large"])
def test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory):
    assert factory.bake_cake(6, 6) != 1
    assert factory.bake_cake(11, 11) != 2


def test_produce_cake_get_cakes(factory):
    factory.bake_cake(1, 1)
    assert len(factory.get_cakes_baked()) == 1
    cake = factory.get_last_cakes(1)[0]
    assert cake is not None
    assert type(cake) == Cake


def test_produce_cakes_get_last_cakes(factory):
    amount = factory.bake_cake(3, 3)
    assert amount == 2
    cakes = factory.get_last_cakes(2)
    assert type(cakes) == list
    assert len(cakes) == 2
    cakes = factory.get_last_cakes(1)
    assert type(cakes) == list
    assert len(cakes) == 1


def test_produce_cakes_order_medium_before(factory):
    factory.bake_cake(3, 3)
    cakes = factory.get_last_cakes(2)
    assert cakes
    assert cakes[0].type == "medium"
    assert cakes[1].type != "medium"


def test_produce_cakes_order_large_before(factory):
    factory.bake_cake(6, 6)
    cakes = factory.get_last_cakes(2)
    assert cakes[0].type == "large"
    assert cakes[1].type != "large"


@pytest.mark.dependency()
def test_get_cakes_correct_amount(factory):
    factory.bake_cake(9, 9)
    assert len(factory.get_cakes_baked()) == 3


@pytest.mark.dependency()
def test_get_last_cakes_correct_amount(factory):
    factory.bake_cake(9, 9)
    for i in range(0, 3):
        assert len(factory.get_last_cakes(i)) == i


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_cakes_returns_cakes(factory):
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_cakes_baked())


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_last_cakes_returns_cakes(factory):
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_last_cakes(4))


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount", "test_get_last_cakes_correct_amount"])
def test_produce_cakes_order(factory):
    factory.bake_cake(8, 8)
    assert len(factory.get_cakes_baked()) == 3
    cakes = factory.get_last_cakes(3)
    assert cakes[2].type == "basic"
    assert cakes[1].type == "medium"
    assert cakes[0].type == "large"


def test_cake_basic():
    basic_cake = Cake(1, 1)
    assert basic_cake.type == "basic"


def test_cake_medium():
    medium_cake = Cake(2, 2)
    assert medium_cake.type == "medium"


def test_cake_large():
    large_cake = Cake(5, 5)
    assert large_cake.type == "large"


def test_cake_wrong_ingredients_throws_exception():
    for i in {i for i in range(1000)} - {1, 2, 5}:
        with pytest.raises(WrongIngredientsAmountException):
            Cake(i, i)


def test_cake_equals():
    cake_basic_1 = Cake(1, 1)
    cake_basic_2 = Cake(1, 1)
    cake_medium_1 = Cake(2, 2)
    cake_medium_2 = Cake(2, 2)
    cake_large_1 = Cake(5, 5)
    cake_large_2 = Cake(5, 5)
    assert cake_basic_1 == cake_basic_2
    assert cake_medium_1 == cake_medium_2
    assert cake_large_1 == cake_large_2


def test_cake_repr():
    cake_basic = Cake(1, 1)
    cake_medium = Cake(2, 2)
    cake_large = Cake(5, 5)
    assert cake_basic.__repr__() == "Cake(basic)"
    assert cake_medium.__repr__() == "Cake(medium)"
    assert cake_large.__repr__() == "Cake(large)"


def test_factory_str_amount(factory):
    num = random.randint(3, 1000)
    for x in [(1, 1) for _ in range(2, num)]:
        factory.bake_cake(*x)
    assert str(factory) == f"Factory with {num - 2} cakes."


def test_factory_str_single(factory):
    factory.bake_cake(1, 1)
    assert str(factory) == "Factory with 1 cake."

