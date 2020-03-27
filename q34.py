# coding: utf-8
from q30 import read_parse_txt

def main():
    for sentence in read_parse_txt():
        for index,word in enumerate(sentence):
            if word['pos'] == '名詞' and sentence[index+1]['surface'] == 'の' and sentence[index+2]['pos'] == '名詞':
                print(word['surface']  +sentence[index+1]['surface'] + sentence[index+2]['surface'])

if __name__ == "__main__":
    # 「——」がサ変接続として出てくるのは謎。Mecabの仕様
    main()