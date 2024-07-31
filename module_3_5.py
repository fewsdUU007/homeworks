def get_multiplied_digits(number):
    str_num = str(number)
    first = int(str_num[0])
    if len(str_num) > 1:
        return first * get_multiplied_digits(int(str_num[1:]))
    else:
        return first

print(get_multiplied_digits(20304))