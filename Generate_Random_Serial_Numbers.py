import string
import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)


def generate_serial(count):

    all_chars = string.ascii_letters + string.digits
    # print(all_chars)

    chars_count = len(all_chars)
    # print(chars_count)

    serial_list = []

    while count > 0:

        random_num = random.randint(0, chars_count -1)

        random_chars = all_chars[random_num]

        serial_list.append(random_chars)

        count -= 1

    print("".join(serial_list))


        

generate_serial(58)