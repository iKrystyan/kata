def create_phone_number(arr):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*arr)


# Test
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))