import math
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def read_file(filepath) -> [str]:
    rows = []
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            rows.append(line.replace("\r", "").replace("\n", ""))

    return rows


def parse_items(items) -> [[str]]:
    return [item.split(";") for item in items]


def create_term_set(items) -> []:
    term_set = []
    for transaction in items:
        for item in transaction:
            if not item in term_set:
                term_set.append(item)

    term_set.sort()

    return list(term_set)


def apriori_gen(dataset, min_support):
    encoder = TransactionEncoder()
    te_ary = encoder.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=encoder.columns_)

    apriori(df, min_support=min_support, use_colnames=True).to_csv("test.csv")


def scan(dataset, candidate_set, min_support):
    dataset_size = float(len(dataset))
    threshold = math.floor(dataset_size * min_support)
    support_counts = {}
    support_data = {}

    for transaction in dataset:
        for candidate in candidate_set:
            if candidate in transaction:
                if candidate in support_counts:
                    support_counts[candidate] += 1
                else:
                    support_counts[candidate] = 1

    for item in support_counts:
        if support_counts[item] > threshold:
            support_data[item] = support_counts[item]

    sorted_vals = {
        k: v
        for k, v in sorted(support_data.items(), key=lambda item: item[1], reverse=True)
    }

    return sorted_vals
