# coding: utf-8
import MeCab

def main():
    with open('neko.txt') as in_file, open('neko.txt.mecab', mode='w') as out_file:
        text = in_file.read()             
        mecab = MeCab.Tagger()
        mecab.parse('')
        node = mecab.parseToNode(text)
        outlines = []
        while node:
            outlines.append(node.surface + ',' + node.feature)
            #次の単語に進める
            node = node.next
        out_file.write('\n'.join(outlines))

if __name__ == "__main__":
    main()