#!/usr/bin/env python3

import os
import json
import sys

def format_triples(triples):
    input_tokens = [ "{} | {} | {}".format(t['subject'], t['property'], t['object']) for t in triples]
    return '<s> ' + ' </s> <s> '.join(input_tokens) + ' </s>'

def process_file(file, out_dir):
    fname = os.path.basename(file)

    out_file_src = os.path.join(out_dir, fname)+'.triples'
    out_file_dest = os.path.join(out_dir, fname)+'.en'

    with open(file) as f, \
        open(out_file_src, 'w') as src, \
        open(out_file_dest, 'w') as dest:
        data = json.load(f)

        for entry in data:
            i = format_triples(entry['triples'])
            sentences = entry['lexicalisations']

            for s in sentences:
                src.write(i + '\n')
                dest.write(s + '\n')
            

def main():
    files = sys.argv[1:]
    out_dir = 'data/v2_cooked'

    os.makedirs(out_dir, exist_ok=True)

    for file in files:
        process_file(file, out_dir)

if __name__ == "__main__":
    main()