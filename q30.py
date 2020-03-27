# coding: utf-8
 
def read_parse_txt():
    result = []
    with open('neko.txt.mecab') as in_file:
        sentence_list = []
        for line in in_file.readlines():
            splits = line.split(',')
            dic = {"surface":splits[0], "base":splits[7], "pos":splits[1] , "pos1":splits[2]}
            sentence_list.append(dic)
            if splits[0] == '。':
                result.append(list(sentence_list))
                sentence_list = []

    return result

if __name__ == "__main__":
    for sentense in read_parse_txt():
        print(sentense)
        print('\n')