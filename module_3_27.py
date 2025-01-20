def calculate_structure_sum(data_structure):
    total_sum = 0
    total_len = 0

    for element in data_structure:
        if isinstance(element, (list, tuple, set)):
            for sub_element in element:
                result = calculate_structure_sum([sub_element])
                total_sum += result
        elif isinstance(element, dict):
            for key, value in element.items():
                if isinstance(key, (int, float)):
                    total_sum += key
                elif isinstance(key, str):
                    total_len += len(key)
                if isinstance(value, (int, float)):
                    total_sum += value
                elif isinstance(value, str):
                    total_len += len(value)
        elif isinstance(element, str):
            total_len += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element

    return total_sum + total_len


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)