import pytest

from recycling_rewards import collection_accepted, reward_points, slot_status


@pytest.mark.parametrize(
    ("material", "weight", "bonus", "expected"),
    [
        ("paper", 3, False, 0),
        ("paper", 8, False, 18),
        ("plastic", 4, True, 12),
        ("metal", 5, True, 36),
        ("plastic", 25, False, 220),
        ("metal", 30, False, 504),
    ],
)
def test_reward_points(material, weight, bonus, expected):
    assert reward_points(material, weight, bonus) == expected


@pytest.mark.parametrize(
    ("material", "weight"),
    [("glass", 10), ("paper", -1)],
)
def test_reward_points_rejects_invalid_input(material, weight):
    with pytest.raises(ValueError):
        reward_points(material, weight, False)


@pytest.mark.parametrize(
    ("weight", "bags", "hazardous", "expected"),
    [
        (4, 8, True, True),
        (60, 1, False, False),
        (10, 4, False, False),
        (10, 3, False, True),
    ],
)
def test_collection_accepted(weight, bags, hazardous, expected):
    assert collection_accepted(weight, bags, hazardous) is expected


@pytest.mark.parametrize(
    ("minutes", "morning", "holiday", "expected"),
    [
        (20, True, False, "open"),
        (10, True, False, "late"),
        (4, True, False, "missed"),
        (25, False, True, "open"),
    ],
)
def test_slot_status(minutes, morning, holiday, expected):
    assert slot_status(minutes, morning, holiday) == expected
