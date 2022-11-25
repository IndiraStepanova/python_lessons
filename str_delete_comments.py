num_of_strings = input()
item_to_del = '#'

for _ in range(int(num_of_strings[1:])):
    string = input()
    if item_to_del in string:
        end_string_index = string.index(item_to_del)
        string = string[:end_string_index].rstrip()
    print(string)