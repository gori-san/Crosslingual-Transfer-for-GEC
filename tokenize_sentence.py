import random
from nltk.tokenize import ToktokTokenizer
from tqdm import tqdm
import argparse


def make_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('output_file', help='output file path')
    args = parser.parse_args()
    return args


def tokenize(i_file, o_file):
    toktok = ToktokTokenizer()
    with open(i_file, 'r') as i_f, open(o_file, 'w') as o_f:
        for line in tqdm(i_f):
            line = line.rstrip('\n')
            tokens = toktok.tokenize(line)
            print(' '.join(tokens), file=o_f)


def main():
    args = make_argparser()
    i_path = args.input_file
    o_path = args.output_file
    tokenize(i_path, o_path)


if __name__ == '__main__':
    main()
