import string
def upgrade_m_number(existing: str) -> str:
    new = existing
    if len(new) == 6:
        new = "000000" + new
    return "M" + new

if __name__=="__main__":
    existing_m_numbers = ['020982', '041485', '091749']
    updated_m_numbers = list(map(upgrade_m_number, existing_m_numbers))
    print(f"{updated_m_numbers=}")


def multiply_by_2(input: int) -> int:
    return input * 2

print(f"{list(map(multiply_by_2, [2,4,6]))=}")

def upper(input: str) -> str:
    return input.upper()

print(f"{list(map(upper, ['s', 'c', 'r', 'e', 'a', 'm']))=}")