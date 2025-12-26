from vehicle1 import calculate_average, mileage_category


def test_average_normal_values():
    mileages = [10, 20, 30]
    assert calculate_average(mileages) == 20


def test_average_float_values():
    mileages = [12.5, 14.5, 15.0]
    assert calculate_average(mileages) == 14.0


def test_average_empty_list():
    mileages = []
    assert calculate_average(mileages) == 0


def test_low_mileage_category():
    avg_mileage = 8
    assert mileage_category(avg_mileage) == "Low Mileage"


def test_average_mileage_category():
    avg_mileage = 15
    assert mileage_category(avg_mileage) == "Average Mileage"


def test_high_mileage_category():
    avg_mileage = 25
    assert mileage_category(avg_mileage) == "High Mileage"