import string
from math import isfinite

import pytest
from hypothesis import given, strategies as st

from recycling_rewards import net_points, parse_collection, weight_average


NON_STRING_VALUES = st.one_of(
    st.none(),
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.lists(st.text()),
)


@given(
    material=st.text(alphabet=string.ascii_letters + " ", min_size=1).filter(
        lambda value: bool(value.strip())
    ),
    weight=st.floats(min_value=0, allow_nan=False, allow_infinity=False),
)
def test_parse_collection_valid_values(material, weight):
    normalized_material = material.strip().title()
    assert parse_collection(f"{material}:{weight!r}") == (
        normalized_material,
        weight,
    )


@given(
    st.sampled_from(
        [
            "",
            "paper",
            "paper:1:2",
            ":1",
            "paper:",
            "paper:-1",
            "paper:nan",
            "paper:inf",
            "paper:1e309",
        ]
    )
)
def test_parse_collection_rejects_invalid_values(text):
    with pytest.raises(ValueError):
        parse_collection(text)


@given(st.text())
def test_parse_collection_arbitrary_text_is_safe(text):
    try:
        material, weight = parse_collection(text)
    except ValueError:
        return

    assert material.strip()
    assert isfinite(weight)
    assert weight >= 0


@given(NON_STRING_VALUES)
def test_parse_collection_rejects_non_string_values(value):
    with pytest.raises(TypeError):
        parse_collection(value)


@given(st.lists(st.integers(min_value=0), min_size=1))
def test_weight_average_matches_floor_average(weights):
    csv_weights = ",".join(str(weight) for weight in weights)
    assert weight_average(csv_weights) == sum(weights) // len(weights)


@given(st.sampled_from(["", ",", "1,,2", "1.5", "-1", "1,"]))
def test_weight_average_rejects_invalid_values(text):
    with pytest.raises(ValueError):
        weight_average(text)


@given(st.text())
def test_weight_average_arbitrary_text_is_safe(text):
    try:
        average = weight_average(text)
    except ValueError:
        return

    assert isinstance(average, int)
    assert average >= 0


@given(NON_STRING_VALUES)
def test_weight_average_rejects_non_string_values(value):
    with pytest.raises(TypeError):
        weight_average(value)


@given(
    points=st.floats(min_value=0, max_value=1e100, allow_nan=False, allow_infinity=False),
    penalty=st.floats(min_value=0, max_value=1e100, allow_nan=False, allow_infinity=False),
)
def test_net_points_applies_multiplier_and_penalty(points, penalty):
    assert net_points(f"{points!r}|{penalty!r}") == max(points * 2 - penalty, 0)


@given(
    st.sampled_from(
        [
            "",
            "80",
            "|10",
            "10|",
            "10|2|1",
            "nan|1",
            "inf|0",
            "-1|0",
            "10|-1",
            "1e308|0",
        ]
    )
)
def test_net_points_rejects_invalid_values(text):
    with pytest.raises(ValueError):
        net_points(text)


@given(st.text())
def test_net_points_arbitrary_text_is_safe(text):
    try:
        points = net_points(text)
    except ValueError:
        return

    assert isfinite(points)
    assert points >= 0


@given(NON_STRING_VALUES)
def test_net_points_rejects_non_string_values(value):
    with pytest.raises(TypeError):
        net_points(value)
