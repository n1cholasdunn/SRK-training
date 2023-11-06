import re


def format_test_with_seconds(data):
    if len(data) != 2:
        raise ValueError("Input data should have two sublists.")

    keys = data[0]
    values = data[1]
    int_values = [
        int(re.search(r"\d+", value).group()) if re.search(r"\d+", value) else None
        for value in values
    ]
    return [{key: value} for key, value in zip(keys, int_values)]


def format_oa_finger_strength(data):
    tests = data[0]
    lbs_values = data[1]
    percentage_values = data[2]

    def extract_values(s):
        """Extract the left and right values from a string."""
        left_value = (
            int(re.search(r"L=(\d+)", s).group(1)) if re.search(r"L=(\d+)", s) else None
        )
        right_value = (
            int(re.search(r"R=(\d+)", s).group(1)) if re.search(r"R=(\d+)", s) else None
        )

        return left_value, right_value

    formatted_data_list = []
    for i, test in enumerate(tests):
        left_lbs, right_lbs = extract_values(lbs_values[i])
        left_percentage, right_percentage = extract_values(percentage_values[i])

        formatted_data = {
            "Test": test,
            "Left": left_lbs,
            "Right": right_lbs,
            "LeftPercentage": left_percentage / 100,
            "RightPercentage": right_percentage / 100,
        }
        formatted_data_list.append(formatted_data)

    return formatted_data_list


def format_pinch_strength(data):
    tests = data[0]
    values = data[1]

    def extract_pinch_values(s):
        """Extract the left and right pinch values from a string."""
        left_match = re.search(r"L=(\d+)", s)
        right_match = re.search(r"R=(\d+)", s)

        left_value = int(left_match.group(1)) if left_match else None
        right_value = int(right_match.group(1)) if right_match else None

        return left_value, right_value

    formatted_data = []
    for i, test in enumerate(tests):
        left_value, right_value = extract_pinch_values(values[i])
        formatted_data.append(
            {
                "Test": test,
                "Left": left_value,
                "Right": right_value,
            }
        )

    return formatted_data


def format_finger_strength(data):
    tests = data[0]
    values = data[1]
    percentages = data[2]

    def extract_finger_values(s, is_percentage=False):
        """Extract finger strength values from a string."""
        match = re.search(r"(\d+)", s)
        value = int(match.group(1)) if match else None
        if is_percentage:
            value = value / 100 if value is not None else None
        return value

    formatted_data = []
    for i, test in enumerate(tests):
        value = extract_finger_values(values[i])
        percentage = extract_finger_values(percentages[i], is_percentage=True)
        formatted_data.append(
            {
                "Test": test,
                "1RM": value,
                "Percentage": percentage,
            }
        )

    return formatted_data


# max_lockoff = [["Pre-training Test", "Test 1", "Test 2"], ["27 seconds", "30", "32"]]
# print(format_test_with_seconds(max_lockoff))
