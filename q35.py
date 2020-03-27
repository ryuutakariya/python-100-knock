# coding: utf-8
from q30 import read_parse_txt

def main():
    for sentence in read_parse_txt():
        connect_word = ''
        for index,word in enumerate(sentence):
            if word['pos'] == '名詞':
                connect_word += word['surface'] 
            else:
                if connect_word != '':
                    print(connect_word)
                    connect_word = ''

if __name__ == "__main__":
    main()