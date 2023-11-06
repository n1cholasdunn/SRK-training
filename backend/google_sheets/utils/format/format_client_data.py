def format_client_data(data):
    label_to_field_mapping = {
        "Name": "name",
        "Phone": "phone",
        "Age": "age",
        "Email": "email",
        "Address": "address",
        "Emergency Contact:": "emergency_contact",
        "Emergency Phone:": "emergency_phone",
        "Height": "height",
        "Weight": "weight",
        "Ape Index": "ape_index",
        "Occupation": "occupation",
        "Hobbies": "hobbies",
        "Primary Climbing and Fitness Goals": "primary_goals",
        "Health Concerns": "health_concerns",
        "PAR-Q Complete: Yes/No?": "parq_complete",
        "Liability Waiver Signed: Y/N": "liability_waiver",
    }
    result = {}
    current_key = None

    for row in data:
        for cell in row:
            if cell in label_to_field_mapping:
                current_key = label_to_field_mapping[cell]
            elif current_key:
                # Convert 'Yes', 'yes', 'y', or 'Y' to True, otherwise False
                if current_key in ["parq_complete", "liability_waiver"]:
                    result[current_key] = cell.lower() in ["yes", "y"]
                else:
                    result[current_key] = cell
                current_key = None

    return result


# exmaple data
# data = [
#     [
#         "Name",
#         "Nicholas Dunn",
#         "",
#         "",
#         "Address",
#         "7693 Palmilla Dr #2302 San Diego CA 92122",
#     ],
#     ["Phone", "858-333-0609", "Email", "nickduunn@gmail.com"],
#     ["Age", "22", "Height", "5'10.5", "Weight", "157", "Ape Index"],
#     ["Occupation", "Delivery Driver", "", "", "Hobbies", "Photography/Reading"],
#     ["Emergency Contact:", "Father:Jeffery Dunn", "Emergency Phone:", "858-598-7355"],
#     [
#         "Primary Climbing and Fitness Goals",
#         "Climb with more intent behind technique and learn to read routes effectively/efficiently. Learn how to choose which flag to use/when to flag over having two feet on.",
#     ],
#     ["Health Concerns", "None"],
#     ["PAR-Q Complete: Yes/No?", "Yes", "Liability Waiver Signed: Y/N", "Y"],
# ]

# formatted_data = format_client_data(data)
# print(formatted_data)
