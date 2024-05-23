import functools

def less_than(this, that):
    if this < that:
        return -1
    elif this == that:
        return 0
    return 1

if __name__=="__main__":
    list = [8,4,1,3,7]
    result = sorted(list, key=functools.cmp_to_key(less_than))
    print(f"{result=}")