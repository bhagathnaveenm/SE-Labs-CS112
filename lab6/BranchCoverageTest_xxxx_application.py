import pytest

from recycling_rewards import collection_accepted, reward_points, slot_status


@pytest.mark.parametrize(
    ("material", "weight", "bonus", "expected"),
    [
        ("paper", 5, False, 0),
        ("paper", 6, False, 6),
        ("paper", 4, True, 0),
        ("paper", 6, True, 12),
        ("plastic", 3, True, 6),
        ("metal", 2, True, 0),
        ("metal", 3, False, 12),
        ("plastic", 24, False, 210),
        ("metal", 23, False, 378),
    ],
)
def test_reward_points_branch_paths(material, weight, bonus, expected):
    assert reward_points(material, weight, bonus) == expected


@pytest.mark.parametrize(
    ("material", "weight"),
    [("glass", 1), ("paper", -1)],
)
def test_reward_points_invalid_inputs(material, weight):
    with pytest.raises(ValueError):
        reward_points(material, weight, False)


@pytest.mark.parametrize(
    ("weight", "bags", "hazardous", "expected"),
    [
        (5, 4, True, True),
        (6, 1, True, False),
        (51, 1, False, False),
        (50, 3, False, True),
        (50, 4, False, False),
    ],
)
def test_collection_acceptance_branch_paths(weight, bags, hazardous, expected):
    assert collection_accepted(weight, bags, hazardous) is expected


@pytest.mark.parametrize(
    ("minutes", "morning", "holiday", "expected"),
    [
        (20, True, False, "open"),
        (19, True, False, "late"),
        (4, True, False, "missed"),
        (10, False, False, "open"),
        (9, False, False, "late"),
        (-6, False, False, "missed"),
        (35, True, True, "open"),
        (34, True, True, "late"),
        (20, False, True, "late"),
        (9, False, True, "missed"),
    ],
)
def test_slot_status_branch_paths(minutes, morning, holiday, expected):
    assert slot_status(minutes, morning, holiday) == expected
