import time


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus.
    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru
    @:return positions where jangurus first meet
    """
    current_time = 0
    max_time = 1000000
    speed1 = jump_distance1 / sleep1
    speed2 = jump_distance2 / sleep2
    delta_distance = pos1 - pos2
    delta_min = delta_distance * 2
    delta_max = delta_distance * 15
    delta_delta = delta_max - delta_min

    print(delta_distance)
    print(delta_min)
    print(delta_max)
    print(delta_delta)
    for i in range(max_time):
        current_time += 1
        if i % sleep1 == 0:
            pos1 += jump_distance1
        if i % sleep2 == 0:
            pos2 += jump_distance2
        if pos1 == pos2:
            return pos1
        if delta_delta > 10000:
            return -1



"""Tsükkel. Kui arv jagub sleep1-ga, siis suurenda pos1-te, kui arv jagub sleep2-ga, siis suurenda pos2-te. Kui pos1 == pos2, 
siis tulemus. Kui deltadelta > ?, siis return -1.

kiirus = Teepikkus / aeg ehk jump_distance1 / sleep1"""


if __name__ == "__main__":
    #print(meet_me(1, 2, 10, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    #print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    #print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    #print(meet_me(1, 7, 1, 15, 5, 1))  #  => 50
    #print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    #print(meet_me(1, 2, 1, 1, 3, 1))  # => -1