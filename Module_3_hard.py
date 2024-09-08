def calculate_structure_sum(list_):
    summa = 0
    for i in list_:
        if type(i) == int:
            summa += i
        elif type(i) == str:
            summa += int(len(i))
        elif type(i) == dict:
            i = list(i.items())
            summa += calculate_structure_sum(i)
        else:
            summa += calculate_structure_sum(i)


    return summa

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)