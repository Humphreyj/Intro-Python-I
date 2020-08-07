# """
# Print out each element of the following array on a separate line:
# ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.
# """

# a = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# for i in a:
#     print(i)

# Stretch:
# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:
# ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22


#loop through initial list
a = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


#if an items lenght > 1 loop through that item and print on own line.

def nested_print(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            nested_print(item)
        else: 
            print(item)

nested_print(a)