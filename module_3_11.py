def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(b = 25, c = [1, 2, 3])

values_list = ['string', False, 18]
values_dict = {'a': 'first', 'b': 'second', 'c': 'third'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'two']

print_params(*values_list_2, 3)
