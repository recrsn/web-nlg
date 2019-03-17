import os
import json
import sys
import spacy
from tqdm import tqdm

nlp = spacy.load('en_core_web_sm')

def main():
    lead = ['<unk>\n', '<s>\n', '</s>\n']

    out_dir = 'data/v2_cooked'
    out_vocab_triples = os.path.join(out_dir, 'vocab.triples')
    out_vocab_en = os.path.join(out_dir, 'vocab.en')
    
    vocab_triples = set()
    vocab_en = set()

    with open(sys.argv[1]) as f:
        data = json.load(f)

        for entry in tqdm(data):
            for triple in entry['triples']:
                vocab_triples.add(triple['subject'])
                vocab_triples.add(triple['property'])
                vocab_triples.add(triple['object'])

            for s in entry['lexicalisations']:
                doc = nlp(s)
                for word in doc:
                    vocab_en.add(word.text.lower())

        with open(out_vocab_triples, 'w') as tf:
            tf.writelines(lead)
            for word in vocab_triples:
                tf.write(word + '\n')

        with open(out_vocab_en, 'w') as of:
            of.writelines(lead)
            for word in vocab_en:
                of.write(word + '\n')


if __name__ == "__main__":
    main()