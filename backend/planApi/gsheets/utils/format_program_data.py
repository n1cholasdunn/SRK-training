def format_program_data(data):
    result = {}

    # Handle the individual keys
    result["Program Type"] = [
        data[1][1],  # Self-Guided Written w/video consults
        data[1][2],  # Hourly Video Coaching
        data[2][1],  # In-Person Hourly Sessions
        data[2][2],  # In-Person Small Group Sessions
    ]

    result["Training Style:"] = data[0][4]

    result["If you chose Rock Climbing:"] = data[3][4]

    result["Payment Rate"] = [
        data[4][1],  # 1hr session
        data[5][1],  # 2hr session
    ]

    result["Highest grade you've climbed indoors"] = data[4][4]

    result["Flash grade indoors"] = data[4][7]

    result["Highest grade you've climbed outdoors"] = data[5][4]

    result["Flash grade outdoors"] = data[5][7]

    result["Program Start Date"] = data[6][1]

    return result
