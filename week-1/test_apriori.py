from apriori import read_file, parse_items, create_term_set, scan, apriori_gen

file_path = "./sample.txt"

#
# https://adataanalyst.com/machine-learning/apriori-algorithm-python-3-0/
#


def test_read_file():
    items = read_file(file_path)

    assert len(items) == 8
    assert items[0] == "Brasseries;American (Traditional);Restaurants"


def test_parse_items():
    items = read_file(file_path)
    parsed_items = parse_items(items)

    expected_item_0 = ["Brasseries", "American (Traditional)", "Restaurants"]
    expected_item_7 = ["Brasseries", "Restaurants"]

    assert len(parsed_items) == 8
    assert parsed_items[0] == expected_item_0
    assert parsed_items[7] == expected_item_7


def test_create_term_set():
    items = read_file(file_path)
    parsed_items = parse_items(items)

    assert len(create_term_set(parsed_items)) == 10


def test_scan():
    items = read_file(file_path)
    parsed_items = parse_items(items)
    term_set = create_term_set(parsed_items)
    dataset_map = list(map(set, parsed_items))

    results = scan(dataset_map, term_set, 0.5)

    assert results == {"Restaurants": 5, "Brasseries": 5}


def test_apriori():
    items = read_file(file_path)
    parsed_items = parse_items(items)
    term_set = create_term_set(parsed_items)
    dataset_map = list(map(set, parsed_items))

    result = apriori_gen(parsed_items, 0.5)
    assert result == False
