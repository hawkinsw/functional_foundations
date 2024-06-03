seasons = ['winter', 'spring', 'summer', 'fall']

first, *rest = seasons

print(f"{first=}")
print(f"{rest=}")

def is_empty(lst):
    if len(lst) == 0:
        return True
    return False

seasons = ['winter', 'spring', 'summer', 'fall']
if is_empty(seasons):
    print("There is only emptiness.")
else:
    print("Happy day!")

def length(lst):
    list_length = 0
    while not is_empty(lst):
        first, *lst = lst
        list_length += 1
    return list_length

print(f"{length(seasons)=}")

def recursive_length(lst):
    if is_empty(lst):
        return 0
    first, *rest = lst
    return 1 + recursive_length(rest)

print(f"{recursive_length(seasons)=}")
print(f"{recursive_length([])=}")

def do_recursive_length(lst, yet):
    if is_empty(lst):
        return yet
    first, *rest = lst
    return do_recursive_length(rest, yet + 1)

print(f"{do_recursive_length(seasons, 0)=}")
print(f"{do_recursive_length([], 0)=}")

def recursive_length_improved(lst):
    def do_recursive_length(lst, yet):
        if is_empty(lst):
            return yet
        first, *rest = lst
        return do_recursive_length(rest, yet + 1)
    return do_recursive_length(lst, 0)

print(f"{recursive_length_improved(seasons)=}")
