from apriori import read_file, parse_items, create_term_set

def main(file_path):
    items = read_file(file_path)
    parsed_items = parse_items(items)
    item_set = create_term_set(parsed_items)
    
    print(item_set)

if __name__ == "__main__":
    main("./data.txt")
