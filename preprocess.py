#!/usr/bin/env python3

import os
import json
import sys

def process_entry(e):
    if len(e) > 1:
        print(e)

    assert len(e) == 1

    result = {
        'category': '',
        'lexicalisations': [],
        'triples': []
    }
    e = next(iter(e.values()))
    
    result['category'] = e['category']
    result['lexicalisations'].extend([x['lex'] for x in e['lexicalisations']])
    result['triples'].extend(e['modifiedtripleset'])

    return result

def process_file(file, out_dir):
    fname = os.path.basename(file)

    out_file = os.path.join(out_dir, fname)

    with open(file) as f:
        data = json.load(f)

        result = [process_entry(e) for e in data['entries']]

        with open(out_file, 'w') as of:
            json.dump(result, of)

def main():
    files = sys.argv[1:]
    out_dir = 'data/v2_processed'

    os.makedirs(out_dir, exist_ok=True)

    for file in files:
        process_file(file, out_dir)

if __name__ == "__main__":
    main()