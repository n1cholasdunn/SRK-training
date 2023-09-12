def remove_empty_elements(data):
    # Find the minimum sublist length
    min_length = min(len(sublist) for sublist in data)

    # Remove empty strings at the same index in all sublists
    filtered_data = [[item for item in sublist if item != ""] for sublist in data]

    # Truncate sublists to the minimum length
    filtered_data = [sublist[:min_length] for sublist in filtered_data]

    return filtered_data


# Example data
example = [
    [
        "Feet Only Slab/Weight Transfers",
        "slab wall",
        "1-2 min",
        "3",
        "",
        "",
        "",
        "",
        "",
        "",
        "No hands or only 1 finger for balance. Do NOT pull with hands at all. Shift weight over one and push with your legs. ",
    ],
    [
        "Quiet Feet",
        "any wall",
        "1-2 min",
        "3",
        "",
        "",
        "",
        "",
        "",
        "",
        "Climb a route up and down with intentional foot placements and do NOT let your feet make a sound when placing them on a hold. Be light on your toes but fully weighting them. ",
    ],
    [
        "Flagging Drills: Step throughs",
        "vertical wall",
        "1-2 min",
        "3",
        "",
        "",
        "",
        "",
        "",
        "",
        "Choose a climb that zig zags and allows you to practice stepping through to flag repeatedly. Focus on keeping your hips open and centered over your standing foot/ balanced between the opposite leg and same arm as standing foot side. Be intentional with your toe placements. ",
    ],
]

# Remove empty elements
filtered_example = remove_empty_elements(example)

# Print the filtered data
for sublist in filtered_example:
    print(sublist)
