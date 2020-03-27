# coding: utf-8
from q30 import read_parse_txt

def main():
    for sentence in read_parse_txt():
        for word in sentence:
            if word['pos'] == '動詞':
                print(word['base'])

if __name__ == "__main__":
    main()