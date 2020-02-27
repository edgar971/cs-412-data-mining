import re
import time
import math 
from prefixspan import PrefixSpan

class pyprefixspan:
    def __init__(self, pattern, minsup=2, len=1):
        self.minsup = minsup
        self.seq = pattern
        self.len = len
        self.out = {}

    def extract(self, minsup, seq):
        items = dict()

        for i, item in enumerate(seq):
            dist = re.split(' +', item)
            for j in dist:
                if j in items:
                    items[j] += 1
                else:
                    items[j] = 1
                
        for k in list(items):
            if items[k] < minsup:
                del items[k]
        return items

    def projection(self, seq, b):
        h = []
        for i, item in enumerate(seq):
            list = re.split(' +', item)
            if b in list:
                dist = list[list.index(b)+1:]
                if len(dist) > 0:
                    h.append(" ".join(dist))
        return h

    def _prefixspan(self, prefix, seq):
        minsup = self.minsup
        pattern = self.extract(minsup, seq)

        for key, value in pattern.items():
            p = prefix + " " + key

            count = len(re.findall(' +', p))
            if count >= self.len:
                p = p.strip()
                self.out.update({p:value})
            j = self.projection(seq, key)
            self._prefixspan(p, j)
        return

    def run(self):
        self._prefixspan("", self.seq)
        return

def read_file(filepath) -> [str]:
    rows = []
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            rows.append(line.replace("\r", "").replace("\n", ""))

    return rows


def write_output(sequence_patterns, filename):
    output = ""
    for seq, support in sequence_patterns.items():
        seq_format = ';'.join(re.split(' +', seq))
        line = f"{support}:{seq_format}\n"
        output += line

    with open(filename, "w") as filetowrite:
        filetowrite.write(output)
    
def write_output_2(sequence_patterns, filename):
    output = ""
    for support, seq in sequence_patterns:
        seq_format = ';'.join(seq)
        line = f"{support}:{seq_format}\n"
        output += line

    with open(filename, "w") as filetowrite:
        filetowrite.write(output)
    


def main(file_path):
    start_time = time.time()
    data = read_file(file_path)
    
    min_support = 100
    print('min_support', min_support)

    # v1
    p = pyprefixspan(data,minsup=min_support,len=1)
    p.run()
    write_output(p.out,"patterns.txt")

    # # v2
    # db = [d.split(' ') for d in data]
    # print('getting seq patterns')
    # ps = PrefixSpan(db)
    # ps.maxlen = 1
    # seq_pattersn = ps.frequent(min_support, closed=True)
    # print('writting to file')
    # write_output_2(seq_pattersn,"patterns-2-closed.txt")


    elapsed_time = time.time() - start_time
    print('time', elapsed_time)


if __name__ == "__main__":
    main("./reviews_sample.txt")
