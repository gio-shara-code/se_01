diamonds = [[2, 1, 1, 1], [1, 5, 1, 0], [5, 4, 1, 3], [5, 3, 4, 4]]


def print_diamonds():
    print("")
    for sub_list in diamonds:
        print(sub_list)
    print("")


def get_end_number_pos():
    amount_one = 0
    column_index = 0

    for row_index in range(len(diamonds) - 1):

        for sub_list_number in diamonds[row_index]:

            if sub_list_number == 1:
                amount_one = amount_one + 1
                if(amount_one == 3):
                    return {"row_index": row_index, "column_index": column_index}
            else:
                amount_one = 0

            column_index = column_index + 1


def check_column_one(column_index, row_index):
    for c_index in range(column_index + 2):

        is_letter = True

        for r_index in range(row_index + 1):
            next_child = diamonds[r_index + 1][c_index]
            current_child = diamonds[r_index][c_index]
            if next_child != current_child:
                is_letter = False

        if is_letter:
            if (column_index + 1) == c_index:
                return "T"
            return "L"

    return False


def check_letter_validation():
    end_pos = get_end_number_pos()

    if(end_pos == None):
        return -1

    column_start_index = end_pos["column_index"] - 2
    row_start_index = end_pos["row_index"] + 1

    return check_column_one(column_start_index, row_start_index)


print_diamonds()
res = check_letter_validation()


def check_horizontal_validation():
    for sub_list in diamonds:
        is_same = is_all_same_numbers(sub_list)
        if is_same:
            return True
    return False


def check_vertical_validation():

    for column_index in range(len(diamonds) - 1):
        is_legal_move = True

        for row_index in range(len(diamonds) - 1):
            next_sub_list = diamonds[row_index + 1]
            current_sub_list = diamonds[row_index]

            if(next_sub_list[column_index] != current_sub_list[column_index]):
                is_legal_move = False

        if(is_legal_move):
            return True

    return False


def is_all_same_numbers(sub_list):
    for i in range(len(sub_list) - 1):
        next_child = sub_list[i + 1]
        current_child = sub_list[i]
        if next_child != current_child:
            return False
    return True


def get_diamon_by_position(current_position):
    pos = 1
    for sub_diamonds in diamonds:
        for diamond in sub_diamonds:
            if(pos == current_position):
                return diamond
            pos = pos + 1


def change_position(element, position):
    pos = 1
    for sub_diamonds in diamonds:
        for i in range(len(sub_diamonds)):
            if(pos == position):
                sub_diamonds[i] = element
                return
            pos = pos + 1


print_diamonds()

input = input("Change position: ")

positions = input.split(" ")

diamond1 = get_diamon_by_position(int(positions[0]))
diamond2 = get_diamon_by_position(int(positions[1]))


change_position(diamond2, int(positions[0]))
change_position(diamond1, int(positions[1]))

is_legal_h = check_horizontal_validation()
is_legal_v = check_vertical_validation()

print_diamonds()

if(is_legal_h or is_legal_v):
    print("Legal move")
else:
    print("Not legal")
