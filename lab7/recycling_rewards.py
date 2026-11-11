from math import isfinite


def _require_text(value, field):
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string")


def _parse_non_negative_float(value, field):
    try:
        number = float(value)
    except (ValueError, OverflowError) as error:
        raise ValueError(f"{field} must be a finite, non-negative number") from error

    if not isfinite(number) or number < 0:
        raise ValueError(f"{field} must be a finite, non-negative number")
    return number


def parse_collection(text):
    _require_text(text, "collection")
    if text.count(":") != 1:
        raise ValueError("collection must contain exactly one ':' separator")

    material, kg = text.split(":")
    material = material.strip()
    if not material:
        raise ValueError("material must not be empty")

    return material.title(), _parse_non_negative_float(kg.strip(), "weight")


def weight_average(weights_csv):
    _require_text(weights_csv, "weights")
    entries = weights_csv.split(",")
    if any(not entry.strip() for entry in entries):
        raise ValueError("weights must be a non-empty CSV of integers")

    try:
        values = [int(entry.strip()) for entry in entries]
    except ValueError as error:
        raise ValueError("weights must be a non-empty CSV of integers") from error

    if any(value < 0 for value in values):
        raise ValueError("weights must be non-negative")
    return sum(values) // len(values)


def net_points(text):
    _require_text(text, "points")
    if text.count("|") != 1:
        raise ValueError("points must contain exactly one '|' separator")

    points, penalty = text.split("|")
    points = _parse_non_negative_float(points.strip(), "points")
    penalty = _parse_non_negative_float(penalty.strip(), "penalty")
    total = points * 2 - penalty
    if not isfinite(total):
        raise ValueError("net points must be finite")
    return max(total, 0)


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg (e.g. paper:12): ")
    result = parse_collection(user_input)
    print("Material and Weight:", result)

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
    result = weight_average(user_input)
    print("Average Weight:", result)

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty (e.g. 80|10): ")
    result = net_points(user_input)
    print("Net Points:", result)


if __name__ == "__main__":
    main()
