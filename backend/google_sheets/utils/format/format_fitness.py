def format_shark_skills_data(data):
    formatted_data = []

    test_set = {}

    # Pre-Training Test
    test_set["pre_training_practice_left"] = {
        "time": float(data[1][2]),
        "deduction_tally": float(data[1][3]),
        "total_deducted": float(data[1][4]),
        "final_total": float(data[1][5]),
    }

    test_set["pre_training_practice_right"] = {
        "time": float(data[2][2]),
        "deduction_tally": float(data[2][3]),
        "total_deducted": float(data[2][4]),
        "final_total": float(data[2][5]),
    }
    test_set["pre_training_first_left"] = {
        "time": float(data[3][2]),
        "deduction_tally": float(data[3][3]),
        "total_deducted": float(data[3][4]),
        "final_total": float(data[3][5]),
    }

    test_set["pre_training_first_right"] = {
        "time": float(data[4][2]),
        "deduction_tally": float(data[4][3]),
        "total_deducted": float(data[4][4]),
        "final_total": float(data[4][5]),
    }
    test_set["pre_training_second_left"] = {
        "time": float(data[5][2]),
        "deduction_tally": float(data[5][3]),
        "total_deducted": float(data[5][4]),
        "final_total": float(data[5][5]),
    }

    test_set["pre_training_second_right"] = {
        "time": float(data[6][2]),
        "deduction_tally": float(data[6][3]),
        "total_deducted": float(data[6][4]),
        "final_total": float(data[6][5]),
    }

    # Retest 1
    test_set["retest_1_practice_left"] = {
        "time": float(data[1][8]),
        "deduction_tally": float(data[1][9]),
        "total_deducted": float(data[1][10]),
        "final_total": float(data[1][11]),
    }

    test_set["retest_1_practice_right"] = {
        "time": float(data[2][8]),
        "deduction_tally": float(data[2][9]),
        "total_deducted": float(data[2][10]),
        "final_total": float(data[2][11]),
    }
    test_set["retest_1_first_left"] = {
        "time": float(data[3][8]),
        "deduction_tally": float(data[3][9]),
        "total_deducted": float(data[3][10]),
        "final_total": float(data[3][11]),
    }

    test_set["retest_1_first_right"] = {
        "time": float(data[4][8]),
        "deduction_tally": float(data[4][9]),
        "total_deducted": float(data[4][10]),
        "final_total": float(data[4][11]),
    }
    test_set["retest_1_second_left"] = {
        "time": float(data[5][8]),
        "deduction_tally": float(data[5][9]),
        "total_deducted": float(data[5][10]),
        "final_total": float(data[5][11]),
    }

    test_set["retest_1_second_right"] = {
        "time": float(data[6][8]),
        "deduction_tally": float(data[6][9]),
        "total_deducted": float(data[6][10]),
        "final_total": float(data[6][11]),
    }

    # Retest 2
    test_set["retest_2_practice_left"] = {
        "time": float(data[8][2]),
        "deduction_tally": float(data[8][3]),
        "total_deducted": float(data[8][4]),
        "final_total": float(data[8][5]),
    }

    test_set["retest_2_practice_right"] = {
        "time": float(data[9][2]),
        "deduction_tally": float(data[9][3]),
        "total_deducted": float(data[9][4]),
        "final_total": float(data[9][5]),
    }
    test_set["retest_2_first_left"] = {
        "time": float(data[10][2]),
        "deduction_tally": float(data[10][3]),
        "total_deducted": float(data[10][4]),
        "final_total": float(data[10][5]),
    }

    test_set["retest_2_first_right"] = {
        "time": float(data[11][2]),
        "deduction_tally": float(data[11][3]),
        "total_deducted": float(data[11][4]),
        "final_total": float(data[11][5]),
    }
    test_set["retest_2_second_left"] = {
        "time": float(data[12][2]),
        "deduction_tally": float(data[12][3]),
        "total_deducted": float(data[12][4]),
        "final_total": float(data[12][5]),
    }

    test_set["retest_2_second_right"] = {
        "time": float(data[13][2]),
        "deduction_tally": float(data[13][3]),
        "total_deducted": float(data[13][4]),
        "final_total": float(data[13][5]),
    }

    # Retest 3
    test_set["retest_3_practice_left"] = {
        "time": float(data[8][8]),
        "deduction_tally": float(data[8][9]),
        "total_deducted": float(data[8][10]),
        "final_total": float(data[8][11]),
    }

    test_set["retest_3_practice_right"] = {
        "time": float(data[9][8]),
        "deduction_tally": float(data[9][9]),
        "total_deducted": float(data[9][10]),
        "final_total": float(data[9][11]),
    }
    test_set["retest_3_first_left"] = {
        "time": float(data[10][8]),
        "deduction_tally": float(data[10][9]),
        "total_deducted": float(data[10][10]),
        "final_total": float(data[10][11]),
    }

    test_set["retest_3_first_right"] = {
        "time": float(data[11][8]),
        "deduction_tally": float(data[11][9]),
        "total_deducted": float(data[11][10]),
        "final_total": float(data[11][11]),
    }
    test_set["retest_3_second_left"] = {
        "time": float(data[12][8]),
        "deduction_tally": float(data[12][9]),
        "total_deducted": float(data[12][10]),
        "final_total": float(data[12][11]),
    }

    test_set["retest_3_second_right"] = {
        "time": float(data[13][8]),
        "deduction_tally": float(data[13][9]),
        "total_deducted": float(data[13][10]),
        "final_total": float(data[13][11]),
    }

    formatted_data.append(test_set)

    return formatted_data


# realData = [
#     [
#         "Pre-Training Test DATE",
#         "Side",
#         "Time (seconds)",
#         "Deduction Tally",
#         "Total Deducted     (# of faults X 0.1)",
#         "Final Total (time+total deduction)",
#         "Retest 1 DATE",
#         "Side",
#         "Time (seconds)",
#         "Deduction Tally",
#         "Total Deducted      (# of faults X 0.1)",
#         "Final Total (time+total deduction)",
#     ],
#     [
#         "Practice",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "Practice",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
#     [
#         "One",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "One",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
#     [
#         "Two",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "Two",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
#     [
#         "Retest 2 DATE",
#         "Side",
#         "Time (seconds)",
#         "Deduction Tally",
#         "Total Deducted      (# of faults X 0.1)",
#         "Final Total (time+total deduction)",
#         "Retest 3 DATE",
#         "Side",
#         "Time (seconds)",
#         "Deduction Tally",
#         "Total Deducted      (# of faults X 0.1)",
#         "Final Total (time+total deduction)",
#     ],
#     [
#         "Practice",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "Practice",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
#     [
#         "One",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "One",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
#     [
#         "Two",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#         "Two",
#         "Left",
#         "1.2",
#         "1.3",
#         "1.4",
#         "1.1",
#     ],
#     ["", "Right", "1.2", "1.3", "1.4", "1.1", "", "Right", "1.2", "1.3", "1.4", "1.1"],
# ]


# formatted_result = format_data(realData)


# for item in formatted_result:
#     print(item)
