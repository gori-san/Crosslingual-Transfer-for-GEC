import sys
import argparse
import json
from tqdm import tqdm
from spellchecker import SpellChecker


def make_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('output_file', help='output file path')
    parser.add_argument('-ld',
                        '--local_dictionary', help='spellcheck学習用のlocal辞書 (json) のpath (指定しない場合はspellchecker付随のen)')

    args = parser.parse_args()
    return args


def spellcheck(input_path, output_path, json_path):
    if json_path:
        spell = SpellChecker(language=None, local_dictionary=json_path)
    else:
        print('English spellcheck')
        spell = SpellChecker(language='en')

    with open(input_path, 'r', encoding='utf-8') as i_file, open(output_path, 'w', encoding='utf-8') as o_file:
        for line in tqdm(i_file):
            words = line.strip('\n').split()
            correct_spell = []
            for word in words:
                correct_spell.append(spell.correction(word))
            print(' '.join(correct_spell), file=o_file)


def main():
    args = make_argparser()
    i_path = args.input_file
    o_path = args.output_file
    json_dic_path = args.local_dictionary
    if json_dic_path:
        spellcheck(i_path, o_path, json_dic_path)
    else:
        spellcheck(i_path, o_path, None)


if __name__ == '__main__':
    main()
