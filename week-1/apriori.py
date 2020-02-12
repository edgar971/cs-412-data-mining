def read_file(filepath) -> [str]:
    rows = []
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            rows.append(line.replace("\r", "").replace("\n", ""))

    return rows


def parse_items(items) -> [[str]]:
    return [item.split(";") for item in items]


def create_term_set(items) -> [frozenset]:
    term_set = []
    for transaction in items:
        for item in transaction:
            if not [item] in term_set:
                term_set.append([item])

    term_set.sort()
    
    return list(map(frozenset, term_set))