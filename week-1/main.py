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


def main(file_path):
    items = read_file(file_path)
    parsed_items = parse_items(items)
    item_set = create_term_set(parsed_items)

    dataset_map = list(map(set, parsed_items))

    support_data = scan(dataset_map, item_set, 0.01)

    save_part_1(support_data)


if __name__ == "__main__":
    main("./data.txt")
