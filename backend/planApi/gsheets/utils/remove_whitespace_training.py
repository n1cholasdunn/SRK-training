def remove_otw_empty_elements(data):
    # Determine maximum length of rows in the dataset
    max_length = max(len(row) for row in data)

    # Extend each row to the maximum length with empty strings
    for row in data:
        while len(row) < max_length:
            row.append("")

    # Transpose the data to work with columns
    transposed_data = list(zip(*data))

    # Identify columns that have at least one non-empty entry
    valid_columns = [
        col for col in transposed_data if any(item.strip() for item in col)
    ]

    # Transpose the filtered columns back to rows
    filtered_data = [list(row) for row in zip(*valid_columns)]

    return filtered_data


# example = [
#     [
#         "Feet Only Slab/Weight Transfers",
#         "slab wall",
#         "1-2 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "No hands or only 1 finger for balance. Do NOT pull with hands at all. Shift weight over one and push with your legs. ",
#     ],
#     [
#         "Quiet Feet",
#         "any wall",
#         "1-2 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Climb a route up and down with intentional foot placements and do NOT let your feet make a sound when placing them on a hold. Be light on your toes but fully weighting them. ",
#     ],
#     [
#         "Flagging Drills: Step throughs",
#         "vertical wall",
#         "1-2 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Choose a climb that zig zags and allows you to practice stepping through to flag repeatedly. Focus on keeping your hips open and centered over your standing foot/ balanced between the opposite leg and same arm as standing foot side. Be intentional with your toe placements. ",
#     ],
#     [
#         "Foot Switching: Match vs Hops",
#         "vertical wall",
#         "1-2 min",
#         "2",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Climb a vertical route by matching and switching feet without hopping. Both feet wll touch the same hold at the same time. Then climb the same route while only allowing yourself to hop to switch feet: your feet must touch some of the same holds but never at the same time. Reflect on the difference between the two climbing styles and what felt more controlled. There's a time and place for both.",
#     ],
#     [
#         "Pivots/Hip Taps & Drop Knees",
#         "any wall",
#         "1-2 min",
#         "2",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Pivot on one foot in a slightly squatted position and suck your hip perpendicularly into the wall to tap it on the wall. Do not reach for next hand hold unless you tapped the hip, then grab the hold above. Repeat the whole way up.",
#     ],
#     [
#         "Rock overs with 2-3 second pause",
#         "systems wall",
#         "1-2 min",
#         "3/leg",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Find a single move on the wall in which you can practice rocking over to reach (but not immediately grab with reaching hand). Pull your hips over your high foot by toeing down hard and dragging it towards yourself till your hips are close to or above your ankle. Unweight your other foot entirely so all weight is in one arm/back and opposite foot. Reach for a far away hand hold (with arm on same side as pulling foot) and pause in this contracted leg position to hold the hip height for about 2-3 seconds before you grab the hand hold. ",
#     ],
#     [
#         "Heel Hooking ",
#         "systems wall",
#         "30 sec - 2 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Practice heek hooking different types of ledges. Focus on precise heel placement and angle of the foot: toes outward? knee facing outward or lunging over heel? Which muscles are most engaged and how can you leverage them to you aid your move?",
#     ],
#     [
#         "Projecting Harder Routes: spotting weaknesses",
#         "any wall",
#         "5 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Pick 3 routes of varying wall angles to project. Identify points of difficulty and analyze what is lacking in order to make that single move or sequence of moves successful. Could using momentum help you or hurt you? Is there an alternative beta you could try? Is it simply a lack of beta implementation keeping you from success in this move or is there just a base strength requirement you haven't met yet? Think outside the box. Be creative. Solve the puzzle. ",
#     ],
#     [
#         "Dead Points",
#         "systems wall",
#         "30 sec - 1 min",
#         "5",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Practice alternating dead points. dynamically reach for a hold outside the midline of your body at max extension from tip to toe without letting your toes come off the foothold. This is generally a cross body tension move from one hand to the opposite foot. Do one per side, rest and analyze movement. Repeat for the number of sets assigned. ",
#     ],
#     [
#         "Dynos",
#         "systems wall",
#         "30 sec - 1 min",
#         "5",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Practice explosive all out dynamic jumps in which 3 or 4 points of contact leave the wall and reconnect at a higher point. Play with differet types of dynos: arched jumps, pogos/pendulum swings, thrutching/using spring loaded movements to create momentum. ",
#     ],
#     [
#         "5 Contact Strength Rapid Fires (alternating arms)",
#         "systems wall",
#         "2 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "start on two hand holds and throw dynamically to different holds at different heights with varying hand shapes, angles, and directions. throw and always return back down to original holds. repeat 5 times per arm. rest, repeat with a different hold set. We're looking for various quick moves to a broad range of hold types in a short duration requiring a momentary judgement call on which muscles are required and how your hand should be shaped before even grabbing it.",
#     ],
#     [
#         "Gastons and Lie Backs",
#         "systems wall",
#         "30 sec - 1 min",
#         "3",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "Climb a line which utilizes gastons and lie backs. During lie backs, focus on creating a strong wedge between the arms, body, and wall. ",
#     ],
#     [
#         "Toe Hooking",
#         "systems wall",
#         "30 sec - 2 min",
#         "3",
#     ],
#     [
#         "Bicycles",
#         "systems wall",
#         "30 sec - 1 min",
#         "3",
#     ],
#     [
#         "Rose Moves",
#         "systems wall",
#         "1 min",
#         "3",
#     ],
# ]

# # # Remove empty elements
# filtered_example = remove_otw_empty_elements(example)

# # Print the filtered data
# for sublist in filtered_example:
#     print(sublist)
