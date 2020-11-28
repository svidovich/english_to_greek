#!/usr/bin/env python
"""
Expects an unheaded CSV of the form
english_word,greek_word,english_definition
and outputs a json blob of the form
[
    {
        english: english_word,
        translated_version: greek_word
        language: greek,
        definition: english_definition
    }, ...
]
"""

import argparse
import csv
import json
from typing import List


def read_csv_to_list(file_path: str) -> List[dict]:
    csv_as_list = list()
    with open(file_path, 'r') as file_handle:
        reader = csv.reader(file_handle)
        for line in reader:
            csv_as_list.append(
                {
                    'english': line[0],
                    'translated_version': line[1],
                    'language': 'greek',
                    'definition': line[2]
                }
            )
    return csv_as_list


def write_list_to_file(file_path: str, list_to_write: List[dict]):
    with open(file_path, 'w') as file_handle:
        json.dump(list_to_write, file_handle, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', required=True, help="The file to read from")
    parser.add_argument('--output-file', required=True, help="The file to write to")

    args = parser.parse_args()

    csv_as_list: List[dict] = read_csv_to_list(args.input_file)
    write_list_to_file(args.output_file, csv_as_list)


if __name__ == '__main__':
    main()
