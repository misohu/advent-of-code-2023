INPUT_FILE1="input1.txt"
INPUT_FILE2="input2.txt"

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

def get_single_digit_integer_from_string(input_string):
    digit_mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for digit_str, value in digit_mapping.items():
        if input_string.startswith(digit_str):
            return value

    return None

def is_there_digit(string):
    if string[0].isdigit():
        return string[0]
    return get_single_digit_integer_from_string(string)

def solve_file(file_path):
    sum = 0
    first = ""
    last = ""

    file = read_file(file_path)
    for index, char in enumerate(file):
        if char == "\n":
            sum += int(first + last)
            first = ""
            last = ""
        digit = is_there_digit(file[index:])
        if digit:
            if first == "":
                first = digit
                last = digit
            else:
                last = digit

    return  sum

if __name__ == '__main__':
    print(solve_file(INPUT_FILE1))
    print(solve_file(INPUT_FILE2))