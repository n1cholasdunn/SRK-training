power_endurance = [["Pre-training Test", "Test 1", "Test 2"], ["62seconds", "64", "65"]]

max_pullups = [["Pre-training Test", "Test 1", "Test 2"], ["13", "14", "15"]]

max_lockoff = [["Pre-training Test", "Test 1", "Test 2"], ["27 seconds", "30", "32"]]

oa_finger_strength = [
    ["Pre-training Test", "Test 1", "Test 2"],
    ["L=110lbs R=110lbs", "L=115lbs R=115lbs", "L=118lbs R=118lbs"],
    ["L=92% R=92%", "L=94% R=94%", "L=96% R=96%"],
]

oa_pinch_strength = [
    ["Pre-training Test", "Test 1", "Test 2"],
    ["L=110lbs R=110lbs", "L=115lbs R=115lbs", "L=118lbs R=118lbs"],
]


finger_strength = [
    ["Pre-training Test", "Test 1", "Test 2"],
    ["187lb ", "190lb", "192lb"],
    ["119%", "121%", "122%"],
]
# >>> from planApi.utils.crud.climbing.oa_finger_strength import test_func
# [{'Test': 'Pre-training Test', 'Left': 110, 'Right': 110, 'LeftPercentage': 0.92, 'RightPercentage': 0.92}, {'Test': 'Test 1', 'Left': 115, 'Right': 115, 'LeftPercentage': 0.94, 'RightPercentage': 0.94}, {'Test': 'Test 2', 'Left': 118, 'Right': 118, 'LeftPercentage': 0.96, 'RightPercentage': 0.96}]
# >>> print(test_func())
# [{'Test': 'Pre-training Test', 'Left': 110, 'Right': 110, 'LeftPercentage': 0.92, 'RightPercentage': 0.92}, {'Test': 'Test 1', 'Left': 115, 'Right': 115, 'LeftPercentage': 0.94, 'RightPercentage': 0.94}, {'Test': 'Test 2', 'Left': 118, 'Right': 118, 'LeftPercentage': 0.96, 'RightPercentage': 0.96}]


def extract_values(data):
    extracted_data = []

    for index in range(len(data[0])):
        test = data[0][index]
        left_weight = int(data[1][index].split("=")[1].split(" ")[0])
        right_weight = int(data[1][index].split("=")[2].split(" ")[0])
        left_percentage = int(data[2][index].split("=")[1].split("%")[0])
        right_percentage = int(data[2][index].split("=")[2].split("%")[0])

        extracted_data.append(
            {
                "test": test,
                "left_weight": left_weight,
                "right_weight": right_weight,
                "left_percentage": left_percentage,
                "right_percentage": right_percentage,
            }
        )

    return extracted_data


# Example usage:
data = [
    ["Pre-training Test", "Test 1", "Test 2"],
    ["L=110lbs R=110lbs", "L=115lbs R=115lbs", "L=118lbs R=118lbs"],
    ["L=92% R=92%", "L=94% R=94%", "L=96% R=96%"],
]

results = extract_values(data)

# Print the extracted values for each iteration
for result in results:
    print("Test:", result["test"])
    print("Left:", result["left_weight"], "lbs")
    print("Right:", result["right_weight"], "lbs")
    print("Left Percentage:", result["left_percentage"], "%")
    print("Right Percentage:", result["right_percentage"], "%")
    print()

# oa_pinch
# [{'Test': 'Pre-training Test', 'Left': 110, 'Right': 110}, {'Test': 'Test 1', 'Left': 115, 'Right': 115}, {'Test': 'Test 2', 'Left': 118, 'Right': 118}]
