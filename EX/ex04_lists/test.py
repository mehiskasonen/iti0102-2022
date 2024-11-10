import lists


def test_car_make_and_models_example():
    """Test that ['Audi', ['A4']] in [['Audi', ['A4'], 'Skoda', ['Super', 'Octavia', 'Superb'],...]]"""
    string = "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"
    test = ['Audi', ['A3']]
    res = lists.car_make_and_models(string)
    assert test in res, 'Ei sisalda'

def test_sum():
    assert sum([1, 2, 2]) == 6, "Should be 6"
