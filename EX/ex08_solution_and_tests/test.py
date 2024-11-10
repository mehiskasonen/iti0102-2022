"""Tests for test.py."""


import solution


def test_student_study__evening_coffee_true():
    """Test if students work @ 19 with coffee."""
    input_amount = 19
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__evening_coffee_false():
    """Test if students work @ 19 without coffee."""
    input_amount = 19
    res = solution.students_study(input_amount, False)
    assert res is True


def test_student_study__night_coffee_true():
    """Test if students work @ 3 with coffee."""
    input_amount = 3
    res = solution.students_study(input_amount, True)
    assert res is False


def test_student_study__night_coffee_false():
    """Test if students work @ 2 without coffee."""
    input_amount = 2
    res = solution.students_study(input_amount, False)
    assert res is False


def test_student_study__day_coffee_true():
    """Test if students work @ 12 with coffee."""
    input_amount = 12
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__day_coffee_false():
    """Test if students work @ 12 without coffee."""
    input_amount = 12
    res = solution.students_study(input_amount, False)
    assert res is False


def test_student_study__evening_edge_case_coffee_true():
    """Test if students work @ 18 with coffee."""
    input_amount = 18
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__evening_edge_case_coffee_true2():
    """Test if students work @ 24 with coffee."""
    input_amount = 24
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__evening_edge_case_coffee_false():
    """Test if students work @ 24 with coffee."""
    input_amount = 18
    res = solution.students_study(input_amount, False)
    assert res is True


def test_student_study__evening_edge_case_coffee_false2():
    """Test if students work @ 24 with coffee."""
    input_amount = 24
    res = solution.students_study(input_amount, False)
    assert res is True


def test_student_study__night_edge_case_coffee_true():
    """Test if students work @ 1 with coffee."""
    input_amount = 1
    res = solution.students_study(input_amount, True)
    assert res is False


def test_student_study__night_edge_case_coffee_true2():
    """Test if students work @ 4 without coffee."""
    input_amount = 4
    res = solution.students_study(input_amount, True)
    assert res is False


def test_student_study__night_edge_case_coffee_false():
    """Test if students work @ 5 without coffee."""
    input_amount = 4
    res = solution.students_study(input_amount, False)
    assert res is False


def test_student_study__night_edge_case_coffee_false2():
    """Test if students work @ 1 without coffee."""
    input_amount = 1
    res = solution.students_study(input_amount, False)
    assert res is False


def test_student_study__day_edge_case_coffee_true():
    """Test if students work @ 5 with coffee."""
    input_amount = 5
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__day_edge_case_coffee_true2():
    """Test if students work @ 17 with coffee."""
    input_amount = 17
    res = solution.students_study(input_amount, True)
    assert res is True


def test_student_study__day_edge_case_coffee_false():
    """Test if students work @ 5 without coffee."""
    input_amount = 5
    res = solution.students_study(input_amount, False)
    assert res is False


def test_student_study__day_edge_case_coffee_false2():
    """Test if students work @ 17 without coffee."""
    input_amount = 17
    res = solution.students_study(input_amount, False)
    assert res is False


def test_lottery__all_fives():
    """Test all fives."""
    a = 5
    b = 5
    c = 5
    res = solution.lottery(a, b, c)
    assert res == 10


def test_lottery__all_same_positive():
    """Test all same positive inputs."""
    a = 4
    b = 4
    c = 4
    res = solution.lottery(a, b, c)
    assert res == 5


def test_lottery__all_same_negative():
    """Test all same negative inputs."""
    a = -1
    b = -1
    c = -1
    res = solution.lottery(a, b, c)
    assert res == 5


def test_lottery__all_same_zero():
    """Test all zero inputs."""
    a = 0
    b = 0
    c = 0
    res = solution.lottery(a, b, c)
    assert res == 5


def test_lottery__a_b_same_c_diff():
    """Test when a and b are same, but c is different."""
    a = 4
    b = 4
    c = 3
    res = solution.lottery(a, b, c)
    assert res == 0


def test_lottery__a_c_same_b_diff():
    """Test when a and c are same, but b is different."""
    a = 2
    b = 4
    c = 2
    res = solution.lottery(a, b, c)
    assert res == 0


def test_lottery__b_c_same_a_diff():
    """Test if students work @ 17 without coffee."""
    a = 4
    b = 2
    c = 2
    res = solution.lottery(a, b, c)
    assert res == 1


def test_lottery__all_diff():
    """Test when all inputs are different."""
    a = 1
    b = 2
    c = 3
    res = solution.lottery(a, b, c)
    assert res == 1


def test_fruit_order__all_zero():
    """Test all zeros."""
    a = 0
    b = 0
    c = 0
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__zero_amount_zero_small():
    """Test zero amount small baskets."""
    a = 0
    b = 1
    c = 0
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__only_big_exact_match():     # only_big_exact_match
    """Test zero amount small baskets."""
    a = 0
    b = 1
    c = 5
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__zero_amount_zero_big():
    """Test with zero big baskets."""
    a = 1
    b = 0
    c = 0
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__zero_amount_others_not_zero():
    """Test with zero big baskets."""
    a = 1
    b = 2
    c = 0
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    """Test with only big baskets, but higher order amount. Amount is multiple of five."""
    a = 0
    b = 10
    c = 100
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__only_big_more_than_required_match():
    """Test with only big baskets and more then amount."""
    a = 0
    b = 3
    c = 10
    res = solution.fruit_order(a, b, c)
    assert res == 0


def test_fruit_order__only_big_more_than_required_no_match():   # jääb tsüklisse
    """Test with only big baskets and more then amount."""
    a = 0
    b = 6
    c = 21
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Test with only smalls, return more than 5 smalls."""
    a = 6
    b = 0
    c = 6
    res = solution.fruit_order(a, b, c)
    assert res == 6


def test_fruit_order__only_small_not_enough_more_than_5_smalls():
    """Test only smalls, more than 5, but not enough."""
    a = 6
    b = 0
    c = 9
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__only_small_more_than_required():
    """Test only small, more than required."""
    a = 8
    b = 0
    c = 4
    res = solution.fruit_order(a, b, c)
    assert res == 4


def test_fruit_order__match_with_more_than_5_smalls():
    """Test match with more than 5 smalls."""
    a = 7
    b = 2
    c = 17
    res = solution.fruit_order(a, b, c)
    assert res == 7


def test_fruit_order__use_all_smalls_some_bigs():
    """Test when using all small baskets and some big baskets."""
    a = 2
    b = 3
    c = 12
    res = solution.fruit_order(a, b, c)
    assert res == 2


def test_fruit_order__use_some_smalls_all_bigs():
    """Test when using all big baskets, but only some small baskets."""
    a = 5
    b = 2
    c = 13
    res = solution.fruit_order(a, b, c)
    assert res == 3


def test_fruit_order__use_some_smalls_some_bigs():
    """Test when using some small baskets and some big baskets."""
    a = 5
    b = 4
    c = 18
    res = solution.fruit_order(a, b, c)
    assert res == 3


def test_fruit_order__not_enough():
    """Test when not enough."""
    a = 2
    b = 3
    c = 20
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Test with enough big baskets but not enough small baskets."""
    a = 2
    b = 4
    c = 18
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Test when there are  more than 5 small baskets, but still not enough."""
    a = 8
    b = 2
    c = 19
    res = solution.fruit_order(a, b, c)
    assert res == -1


def test_fruit_order__match_large_numbers():
    """Test when there are enough big baskets, but not enough small baskets. Uses big input values."""
    a = 200
    b = 110
    c = 709
    res = solution.fruit_order(a, b, c)
    assert res == 159


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Test when there are enough big baskets, but not enough small baskets. Uses big input values."""
    a = 1
    b = 601
    c = 3004
    res = solution.fruit_order(a, b, c)
    assert res == -1
