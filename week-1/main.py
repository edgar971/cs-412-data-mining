from apriori import read_file, parse_items, create_term_set, scan


def main(file_path):
    items = read_file(file_path)
    parsed_items = parse_items(items)
    item_set = create_term_set(parsed_items)

    dataset_map = list(map(set, parsed_items))

    results, support_data = scan(dataset_map, item_set, 0.01)
    print(support_data)


if __name__ == "__main__":
    main("./data.txt")
