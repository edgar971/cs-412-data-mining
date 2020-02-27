import argparse
import logging
import random
import re

from gsp import GSP

logging.basicConfig(level=logging.DEBUG)

def read_file(filepath) -> [str]:
    rows = []
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            rows.append(line.replace("\r", "").replace("\n", "").split())

    return rows


transactions = read_file('test.txt')

result = GSP(transactions).search(0.1)

print("========= Status =========")
print("Transactions: {}".format(transactions))
print("GSP: {}".format(result))