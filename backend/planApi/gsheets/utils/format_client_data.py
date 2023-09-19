def format_client_data(data):
    result = {}
    for row in data:
        key = None
        for cell in row:
            if not cell:
                continue
            if key is None:
                key = cell
            else:
                result[key] = cell
                key = None
    return result


# # exmaple data
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

# formatted_data = process_data(data)
# print(formatted_data)
