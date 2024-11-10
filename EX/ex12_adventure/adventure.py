"""Dungeons and Pythons."""

import math
from operator import attrgetter


class World:
    """World-class."""

    def __init__(self, python_master: str):
        """World Class constructor."""
        self.python_master = python_master
        self.graveyard = []
        self.adventurers = []
        self.monsters = []
        self.set_necromancer_status = False

    def get_python_master(self):
        """Return the name of Python Master."""
        return self.python_master

    def get_graveyard(self):
        """Return list of characters in the graveyard."""
        return self.graveyard

    def get_monster_list(self):
        """Return monster list."""
        return list(filter(lambda npc: not npc.active, self.monsters))

    def get_adventurer_list(self):
        """Return adventurer list."""
        return list(filter(lambda pc: not pc.active, self.adventurers))
        # return [pc for pc in self.adventurers if pc.active is False]

    def add_adventurer(self, player_character: 'Adventurer'):
        """Add adventurer to list of adventurers."""
        if isinstance(player_character, Adventurer):
            self.adventurers.append(player_character)

    def add_monster(self, non_player_character: 'Monster'):
        """Add monster to list of monsters."""
        if isinstance(non_player_character, Monster):
            self.monsters.append(non_player_character)

    def remove_character(self, name):
        """Remove inactive PC or NPC with given name from the game-world and put it into the graveyard."""
        to_remove = []

        for pc in self.adventurers:
            if pc.name == name:
                if not pc.active:
                    to_remove.append(pc)
                    break

        for item in to_remove:
            self.graveyard.append(item)

        self.adventurers = set(self.adventurers) - set(to_remove)

    def necromancers_active(self, active: bool):
        """Revive all characters from the graveyard if necromancers are active.

        If necromancers status is True, function revive_graveyard() is used.
        Necromancers will be eaten and status will be set to False.

        :param active: shows if necromancers are active or not.
        """
        self.set_necromancer_status = True
        if active is True:
            self.revive_graveyard()
        self.set_necromancer_status = False

    def revive_graveyard(self):
        """Revive all characters in the graveyard.

        All characters will be put into monster list, new type will be Zombie.
        All adventurers will be turned into Monsters with the same power. Monsters name will be Undead [adventurers name]
        and Monster type is Zombie [adventurers class_type].
        Old Adventurer type objects will be lost.
        """
        if self.necromancers_active(True):
            for char in self.graveyard:
                if isinstance(char, Adventurer):
                    adventurer_to_monster = Monster(f"Undead {char.name}", f"Zombie {char.class_type}", char.power)
                    self.monsters.append(adventurer_to_monster)
                    self.graveyard.remove(char)
                    # print(adventurer_to_monster)
                    # char = Monster(f"{char.name}, Zombie {char.class_type}, {char.power}")
                if isinstance(char, Monster):
                    char.type = "Zombie"
                    self.monsters.append(char)

    def get_active_adventurers(self):
        """Return list of all active adventurers' sorted by exp in descending order."""
        # active_adventurers = [pc.active for pc in self.adventurers if pc.active]
        active_adventurers = list(filter(lambda pc: pc.active, self.adventurers))
        active_by_exp = sorted(active_adventurers, key=lambda pc: pc.experience, reverse=True)
        return active_by_exp

    def select_by_class_and_inactivity(self, class_type: str) -> list:
        """Added method to reduce code."""
        adventurers_by_class = list(filter(lambda s: class_type == s.class_type, self.adventurers))
        adventurers_by_activity = list(filter(lambda s: not s.active, adventurers_by_class))
        return adventurers_by_activity

    def add_strongest_adventurer(self, class_type: str):
        """Add Adventurer with highest pow with given class_type, who is not active."""
        selected = self.select_by_class_and_inactivity(class_type)
        strongest_inactive_adventurer = max(selected, key=attrgetter('power'))
        strongest_inactive_adventurer.active = True
        self.get_active_adventurers()

    def add_weakest_adventurer(self, class_type: str):
        """Add Adventurer with lowest pow with given class_type, who is not active."""
        selected = self.select_by_class_and_inactivity(class_type)
        weakest_inactive_adventurer = min(selected, key=attrgetter('power'))
        weakest_inactive_adventurer.active = True
        self.get_active_adventurers()

    def add_most_experienced_adventurer(self, class_type: str):
        """Add Adventurer with highest exp with given class_type, who is not active."""
        selected = self.select_by_class_and_inactivity(class_type)
        most_experienced_inactive_adventurer = max(selected, key=attrgetter('experience'))
        most_experienced_inactive_adventurer.active = True
        self.get_active_adventurers()

    def add_least_experienced_adventurer(self, class_type: str):
        """Add Adventurer with lowest exp with given class_type, who is not active."""
        selected = self.select_by_class_and_inactivity(class_type)
        least_experienced_inactive_adventurer = min(selected, key=attrgetter('experience'))
        least_experienced_inactive_adventurer.active = True
        self.get_active_adventurers()

    def add_adventurer_by_name(self, name: str):
        """Add adventurer with given name, if he/she exists and is not active."""
        adventurers_by_name = list(filter(lambda pc: name == pc.name, self.adventurers))
        inactive_adventurers_by_name = list(filter(lambda pc: not pc.active, adventurers_by_name))
        for pc in inactive_adventurers_by_name:
            pc.active = True
        self.get_active_monsters()

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Add all adventurers with given class_type, if they are not active."""
        selected = self.select_by_class_and_inactivity(class_type)
        for npc in selected:
            npc.active = True
        self.get_active_adventurers()

    def add_all_adventurers(self):
        """Add all adventurers, who are not active."""
        adventurers_by_activity = list(filter(lambda s: not s.active, self.adventurers))
        for pc in adventurers_by_activity:
            pc.active = True
        self.get_active_adventurers()

    def get_active_monsters(self) -> list:
        """Return list of active monsters, sorted by power in descending order."""
        active_monsters = list(filter(lambda npc: npc.active, self.monsters))
        active_by_power = sorted(active_monsters, key=lambda npc: npc.power, reverse=True)
        return active_by_power

    def add_monster_by_name(self, name: str):
        """Add monster with given name, if not active."""
        monsters_by_name = list(filter(lambda npc: name == npc.name, self.monsters))
        inactive_monster_by_name = list(filter(lambda npc: not npc.active, monsters_by_name))
        for pc in inactive_monster_by_name:
            pc.active = True
        self.get_active_monsters()

    def add_strongest_monster(self):
        """Add monster with the highest pow, who is not active."""
        monsters_by_activity = list(filter(lambda npc: not npc.active, self.monsters))
        # monsters_by_pow = list(filter(lambda npc: npc.power, monsters_by_activity))
        monster_by_pow = max(monsters_by_activity, key=attrgetter('power'))
        monster_by_pow.active = True
        self.get_active_monsters()

    def add_weakest_monster(self):
        """Add monster with lowest pow, who is not active."""
        monsters_by_activity = list(filter(lambda npc: not npc.active, self.monsters))
        # monsters_by_pow = list(filter(lambda npc: npc.power, monsters_by_activity))
        monster_by_pow = min(monsters_by_activity, key=attrgetter('power'))
        monster_by_pow.active = True
        self.get_active_monsters()

    def add_all_monsters_of_type(self, type: str):
        """Add all monsters of given type, who are not active."""
        monsters_by_type = list(filter(lambda npc: type == npc.type, self.monsters))
        monsters_by_activity = list(filter(lambda npc: not npc.active, monsters_by_type))
        for npc in monsters_by_activity:
            npc.active = True
        self.get_active_monsters()

    def add_all_monsters(self):
        """Add all monsters, who are not active."""
        monsters_by_activity = list(filter(lambda npc: not npc.active, self.monsters))
        for pc in monsters_by_activity:
            pc.active = True
        self.get_active_monsters()


class Adventurer:
    """Adventurer class.

    Every adventurer has a name, class type, power and experience.
    """

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Adventurer class constructor.

        :param name: element has one name.
        """
        self.name = name
        if class_type not in ("Paladin", "Druid", "Wizard"):
            class_type = "Fighter"
        self.class_type = class_type
        if power > 99:
            power = 10
        self.power = power
        self.experience = max(0, experience)
        self.active = False

    def __repr__(self) -> str:
        """Adventurer class representation.

        :return: string: So that you can read, dummy.
        """
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """Add power to adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """Add experience to adventurer."""
        if exp < 0:
            self.experience += 0
        if exp > 0:
            res = self.experience + exp
            if res > 99:
                to_add = math.floor(res / 10)
                self.add_power(to_add)
                self.experience = 0
            else:
                self.experience += exp


class Monster:
    """Monster class.

    Every monster has a name, a type and power.
    """

    def __init__(self, name: str, type: str, power: int):
        """Monster class constructor."""
        self.type = type
        self.power = power
        self.original_name = name
        self.active = False

    @property
    def name(self):
        """Add Undead into name if monster is of type undead."""
        if self.type == 'Zombie':
            new_name = "Undead " + self.original_name
            return new_name
        else:
            return self.original_name

    def __repr__(self):
        """Monster class representation."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50, 20)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40, 10)
    third_friend = Adventurer("Sander", "Wizard", 1, 12)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    adv1 = Adventurer("Tõnn", "Druid", 50)
    adv2 = Adventurer("Poksikott", "Construct", 1)
    adv3 = Adventurer("Tõnn", "Wizard", 50)
    adv4 = Adventurer("Poksikott", "Construct", 1)
    adv5 = Adventurer("Jänguru", "Animal", 1)

    world.add_adventurer(adv1)
    world.add_adventurer(adv2)
    world.add_adventurer(adv3)
    world.add_adventurer(adv4)
    world.add_adventurer(adv5)

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    print(friend.add_power(20))
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    # world.add_adventurer(hero)
    # world.add_adventurer(friend)
    # world.add_adventurer(another_friend)
    # world.add_adventurer(third_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots
    # ----------------------------------------------------------------------------------------------------
    world.add_monster(annoying_friend)
    # world.add_monster(hero)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    # world.add_adventurer(annoying_friend)
    print()
    print("Oodake veidikene, ma tekitan natukene kolle.")
    # goblin = Monster("", "Goblin", 2)
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    # print(goblin)
    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)
    print()
    print("Mängime esimese seikluse läbi!")
    # world.add_strongest_adventurer("Druid")
    # world.add_weakest_adventurer("Wizard")
    # world.add_most_experienced_adventurer("Paladin")
    # world.add_adventurer(friend)

    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep

    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    # world.add_adventurer_by_name("Sander")
    # world.add_weakest_adventurer("Wizard")
    # world.add_adventurer_by_name("Toots")
    # world.add_adventurer_by_name("XxX_Eepiline_Sõdalane_XxX")
    # print(world.get_adventurer_list())
    world.remove_character("Poksikott")
    # world.remove_character("Toots")
    # print(world.get_active_adventurers())
    # print(world.get_adventurer_list())
    print(world.get_adventurer_list())
    # print(world.get_active_adventurers())
    # world.remove_character("XxX_Eepiline_Sõdalane_XxX")
    print(world.get_graveyard())
    # print(world.get_adventurer_list())
    # print(world.get_active_adventurers())
    print()
    exit()

    # ============================================================================================================

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
