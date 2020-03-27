# coding: utf-8
from q30 import read_parse_txt

def main():
    for sentence in read_parse_txt():
        for word in sentence:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                print(word['surface'])

if __name__ == "__main__":
    # 「——」がサ変接続として出てくるのは謎。Mecabの仕様
    main()