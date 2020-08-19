from grocery.builtins_ext import list_ext


if __name__ == '__main__':
    test_list = list_ext([{'a': 1, 'b': 2}, {'a': 4, 'b': 3}, {'a': 3, 'b': 8}, {'a': 6, 'b': 10}, {'a': 2, 'b': 9}])
    for i in test_list.filter_dict(a__gt=3, b__ge=4):
        print(i)

    test_list = list_ext([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    for i in test_list.group(3):
        print(i)