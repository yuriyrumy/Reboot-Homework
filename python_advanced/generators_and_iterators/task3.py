# Напишіть функцію-генератор перестановок, яка отримує список елементів і видає усі можливі перестановки цих елементів.

def permutations(lst: list):
    if len(lst) == 0 or len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in permutations(lst[:i] + lst[i + 1:]):
                yield [lst[i]] + perm


for i_perm in permutations([1, 2, 3]):
    print(i_perm)
