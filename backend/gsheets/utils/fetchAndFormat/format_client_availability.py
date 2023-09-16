def format_availability(data):
    days_of_week = data[0][1:]  # Skip the "Training Availability" cell
    am_availability = data[1][1:]  # Skip the "AM" cell
    pm_availability = data[2][1:]  # Skip the "PM" cell

    availability_dict = {}
    for day, am, pm in zip(days_of_week, am_availability, pm_availability):
        availability_dict[day] = {
            "AM": am.strip(),  # Remove extra spaces
            "PM": pm.strip(),  # Remove extra spaces
        }

    return availability_dict


# # example data
# data = [
#     [
#         "Training Availability",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday",
#     ],
#     [
#         "AM",
#         "Open Availability ",
#         "Open Availability ",
#         "Open Availability ",
#         "Open Availability ",
#         "Open Availability ",
#         "Open Availability ",
#         "None",
#     ],
#     [
#         "PM",
#         "9:00-11:00",
#         "Open Availability ",
#         "None",
#         "None",
#         "None",
#         "None",
#         "9:00-11:00",
#     ],
# ]

# formatted_data = format_availability(data)
# print(formatted_data)
