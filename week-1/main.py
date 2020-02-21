from efficient_apriori import apriori

from apriori import read_file, parse_items, create_term_set, scan


def save_part_1(data):
    output = ""
    for item in data:
        support = data[item]
        line = f"{support}:{item}\n"
        output += line

    file = "patterns-1.txt"
    with open(file, "w") as filetowrite:
        filetowrite.write(output)


def save_part_2(dataset_map):
    itemsets, rules = apriori(dataset_map, min_support=0.01)
    output = ""
    for number in itemsets:
        if number is not 3:
            for item, count in itemsets[number].items():
                line = f"{count}:{';'.join(item)}\n"
                output += line

    file = "patterns-2.txt"
    with open(file, "w") as filetowrite:
        filetowrite.write(output)


def main(file_path):
    items = read_file(file_path)
    parsed_items = parse_items(items)
    item_set = create_term_set(parsed_items)

    dataset_map = list(map(set, parsed_items))
    dataset_tuple = list(map(tuple, parsed_items))

    support_data = scan(dataset_map, item_set, 0.01)

    save_part_1(support_data)
    save_part_2(dataset_tuple)


if __name__ == "__main__":
    main("./data.txt")
