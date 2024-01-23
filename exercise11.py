# create a function, that take integer as a parameter
def space_reverse_int(num):
    # convert the given parameter to a string
    # use string indexing technique to reverse the given sting
    reverse_str = str(num)[::-1]
    # add spaces to each item
    return ' '.join(reverse_str)


print(space_reverse_int(7536))