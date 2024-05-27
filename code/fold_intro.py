import functools
def summer(ip: str, next: int) -> int:
    print(f"{ip=}")
    print(f"{next=}")
    return ip + next

def concatenater(ip: int, next: str) -> str:
    print(f"{ip=}")
    print(f"{next=}")
    return ip + next

if __name__=="__main__":
    result = functools.reduce(concatenater, ['a', 'b', 'b', 'a'], "")
    print(f"{result=}")
    result = functools.reduce(summer, [1,2,3,4,5], 0)
    print(f"{result=}")