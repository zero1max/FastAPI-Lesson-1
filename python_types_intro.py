# Python Types Intro

def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name + " " + last_name
    return full_name.title()


# print(get_full_name("musharraf", "ibragimov"))

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


# print(get_name_with_age("Anna", 18))


from typing import List


def process_item(names: List[str]):
    for name in names:
        print(name)


# process_item(["Anna", "Jack", "Bobo"])

def process_items(names: list[str]):
    for name in names:
        print(name)


# process_items(["Jack", "Doe", "Sofia"])


from typing import Set, Tuple


def process_item_data(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s


def process_item_datas(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


from typing import Dict


def process_item_d(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item_dd(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


from typing import Union


def process_item_u(item: Union[int, str]):
    print(item)


def process_item_(item: int | str):
    print(item)

from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# say_hi("Hasan")

def say_hi_10(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# say_hi_10("Hasan")

from typing import Optional


def say_hi_o(name: Optional[str]):
    print(f"Hey {name}!")


say_hi_o(name=None)
