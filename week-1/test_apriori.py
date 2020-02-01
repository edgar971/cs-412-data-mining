from apriori import read_file, parse_items, create_term_set

file_path = "./sample.txt"

#
# https://adataanalyst.com/machine-learning/apriori-algorithm-python-3-0/
#


def test_read_file():
    items = read_file(file_path)

    assert len(items) == 8
    assert items[0] == "Breakfast & Brunch;American (Traditional);Restaurants"


def test_parse_items():
    items = read_file(file_path)
    parsed_items = parse_items(items)

    expected_item_0 = ["Breakfast & Brunch", "American (Traditional)", "Restaurants"]
    expected_item_7 = ["Brasseries", "Restaurants"]

    assert len(parsed_items) == 8
    assert parsed_items[0] == expected_item_0
    assert parsed_items[7] == expected_item_7


def test_create_term_set():
    items = read_file(file_path)
    parsed_items = parse_items(items)

    create_term_set(parsed_items)
    assert False
