from fractions import Fraction

"""def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

        speed_1 = Fraction(jump_distance1, sleep1)
        speed_2 = Fraction(jump_distance2, sleep2)

        # Check which hare is slower. If equal speed, set slower_hare to 1.
        if speed_2 >= speed_1:
            slower_hare = 1
        else:
            slower_hare = 2

        distance_between_hares = None

        slower_just_moved = False

        current_position_1 = pos1
        current_position_2 = pos2

        # How long do they have left to sleep?
        current_sleep_remaining_1 = 0
        current_sleep_remaining_2 = 0


        # Do the loop.
        while True:
            # Check if the hares are still sleeping, and if not, jump and reset the sleep timer.
            if current_sleep_remaining_1 == 0:
                current_position_1 += jump_distance1
                current_sleep_remaining_1 = sleep1
                if slower_hare == 1:
                    slower_just_moved = True


            if current_sleep_remaining_2 == 0:
                current_position_2 += jump_distance2
                current_sleep_remaining_2 = sleep2
                if slower_hare == 2:
                    slower_just_moved = True


            current_sleep_remaining_1 -= 1
            current_sleep_remaining_2 -= 1


            # Check to see if they're at the same position.
            if current_position_1 == current_position_2:
                return current_position_1

            # Check if they will never meet. If the slower hare is behind the faster one, and after moving gets further behind,
            # or stays same distance as it was the previous time it jumped, then it will never catch up.
            if slower_just_moved:
                if slower_hare == 1:
                    if current_position_1 < current_position_2:
                        previous_distance_between_hares = distance_between_hares
                        distance_between_hares = current_position_2 - current_position_1
                        if previous_distance_between_hares != None and distance_between_hares >= previous_distance_between_hares:
                            return -1
                if slower_hare == 2:
                    if current_position_2 < current_position_1:
                        previous_distance_between_hares = distance_between_hares
                        distance_between_hares = current_position_1 - current_position_2
                        if previous_distance_between_hares != None and distance_between_hares >= previous_distance_between_hares:
                            return -1

            slower_just_moved = False"""

from fractions import Fraction

def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    if pos1 == pos2:
        # if they are already on the same place, they met at that position
        return pos1
    elif Fraction(jump_distance1, sleep1) == Fraction(jump_distance2, sleep2):
        # same speed but different positions like in 4th case (reed my comment about that)
        return -1

    if pos2 < pos1:
        # to ensure that 1st is lesser
        pos2, pos1 = pos1, pos2
        jump_distance2, jump_distance1 = jump_distance1, jump_distance2
        sleep2, sleep1 = sleep1, sleep2

    # simulation by seconds (it can also be by gcd(t1, t2))
    time = 1    # 1 or gcd assuming they do not jump instantly
    while pos1 != pos2:
        if not time % sleep2:
            if pos2 < pos1:
                #p2 < p1 which means speed1 > speed2 since at begining p1 < p2
                # 2nd will make even greater distance between that 1st won't catch up with
                return -1
            pos2 += jump_distance2
        if not time % sleep1:
            pos1 += jump_distance1
        time += 1 # or gcd
    return pos1


if __name__ == "__main__":
    print(meet_me(1, 2, 10, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))  #  => 50
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 2, 1, 1, 3, 1))  # => -1
    print(meet_me(1, 2, 1, 2, 1, 1))  # = > 3
    print(meet_me(1, 2, 1, 1, 2, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(3, 5, 10, 4, 1, 2))  # => 8
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(1, 7, 1, 15, 5, 1))  # => 50
