def remove_character(self, name):
    """Remove inactive PC or NPC with given name from the game-world and put it into the graveyard."""
    to_remove = []

    for pc in self.adventurers:
        if pc.name == name:
            if not pc.active:
                to_remove.append(pc)
                break

    # to_remove_name = [self.graveyard.append(pc) for pc in self.adventurers if pc.name == name]
    # to_remove_name = [pc for pc in self.adventurers if pc.name == name]
    # to_remove_name_active = [pc for pc in to_remove_name if not pc.active]

    for item in to_remove:
        self.graveyard.append(item)

    self.adventurers = set(self.adventurers) - set(to_remove)

# print(to_remove_name_active[0])
# self.graveyard.append(to_remove_name_active[0])

# for item in self.adventurers:
# if item in to_remove_name_active:
# self.adventurers.remove(item)
# self.graveyard.append(item)

# to_remove_name_npc = [npc for npc in self.monsters if npc.name == name]
# to_remove_name_active_npc = [npc for npc in to_remove_name_npc if not npc.active]

# for char in self.monsters:
# if char in to_remove_name_active_npc:
# self.monsters.remove(char)
# self.graveyard.append(char)

# to_remove_name = [self.graveyard.append(pc) for pc in to_remove_name_active]
# self.adventurers = [pc for pc in self.adventurers if not in to_remove_name]

# print(to_remove_name)
# print(self.graveyard)

# self.adventurers = [self.adventurers.remove(pc) for pc in self.adventurers if pc.name == name and pc.active]
# flag = False


# i = len(self.adventurers) - 1
# while i >= 0:
#     for pc in self.adventurers:
#         i -= 1
#         if pc.name == name:
#             if not pc.active:
#                 self.graveyard.append(pc)
#                 self.adventurers.remove(pc)
#             # return element
#
# j = len(self.monsters) - 1
# while j >= 0:
#     for npc in self.monsters:
#         j -= 1
#         if npc.name == name:
#             if not npc.active:
#                 self.graveyard.append(npc)
#                 self.monsters.remove(npc)
# return element

# for PC in self.adventurers:
#     if PC.name == name:
#         if not PC.active:
#             self.graveyard.append(PC)
#             self.adventurers.remove(PC)
#             break
#             # flag = True
#
# # if flag is False:
#     for NPC in self.monsters:
#         if NPC.name == name:
#             if not NPC.active:
#                 self.graveyard.append(NPC)
#                 self.monsters.remove(NPC)
#                 break

# first_to_delete = self.graveyard[0].name
# for char in self.graveyard:
# if first_to_delete == char.name:
# self.graveyard.remove(char)


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

    #def set_activity(self, active_or_not):
        #self._active = active_or_not