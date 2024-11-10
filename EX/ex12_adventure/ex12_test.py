import pytest

from adventure import *


@pytest.fixture()
def world_empty():
    #world = World("Ago")
    return World("Ago")


@pytest.fixture()
def world_complex():
    world_complex = World("Ago")
    hero1 = Adventurer("Ago", "Paladin", 50)
    hero2 = Adventurer("Mati", "Wizard", 10)
    monster = Monster("Mati", "Zombie", 15)
    world_complex.add_adventurer(hero1)

    return world_complex

@pytest.fixture()
def monster_ago():
    return Monster("Ago", "Zombie", 100)


def test_world_python_master(world_empty):
    assert world_empty.python_master == "Ago"


def test_world_complex(world_complex, monster_ago):
    world_complex.get_graveyard()
    world_complex.add_adventurer(monster_ago)


def test_adventurer_basic():
    hero1 = Adventurer("Ago", "Paladin", 10)
    assert str(hero1) == "Ago, the Paladin, Power: 10, Experience: 0."


def test_adventurer_advanced():
    pass


def test_adventurer_random():
    pass


def test_monster_basic():
    pass


def test_monster_zombie():
    pass


def test_monster_random():
    pass


def test_world():
    pass


def test_world_get_lists():
    pass


def test_world_add_characters():
    world2 = World("Ago")
    hero1 = Adventurer("Ago", "Paladin", 50)
    world2.add_adventurer(hero1)
    assert hero1 in world2.get_adventurer_list()
    # assert "Ago" in world_complex.get_active_adventurers()


def test_world_cat_not_add_to_list_if_wrong_type():
    pass


def test_world_add_adventurer_by_power():
    pass


def test_world_add_adventurer_by_xp():
    pass


def test_world_add_monsters_by_power():
    pass


def test_world_removing_characters_list(world_empty):
    adventurer1 = Adventurer("Sander", "Paladin", 50)
    adventurer2 = Adventurer("Tõnn", "Wizard", 50)
    world_empty.add_adventurer(adventurer1)
    world_empty.add_adventurer(adventurer2)
    world_empty.remove_character("Tõnn")
    assert "Tõnn, the Wizard, Power: 50, Experience: 0" not in world_empty.get_adventurer_list()


def test_world_removing_characters_graveyard(world_empty):
    adventurer1 = Adventurer("Sander", "Paladin", 50)
    adventurer2 = Adventurer("Tõnn", "Wizard", 50)
    world_empty.add_adventurer(adventurer1)
    world_empty.add_adventurer(adventurer2)
    world_empty.remove_character("Tõnn")
    assert adventurer2 in world_empty.get_graveyard()




