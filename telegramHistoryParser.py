import bs4
import re
import os

words = []

def findFiles():
    messages = []
    regex = re.compile('^messages[1-9|0-9]*.html$')
    for root, dirs, files in os.walk('../../'):
        for file in files:
            if regex.match(file):
                messages.append(file)

    print('Finded {} files with messages'.format(len(messages)))
    return messages


def scanFiles(messages):
    tmp = []

    for file in messages:

        with open('../' + file, 'r') as f:
            soup = bs4.BeautifulSoup(f, "html.parser")
            text = soup.find_all('div', class_='text')

            print('+ {} sanned'.format(file))

            for txt in text:
                tmp.append(txt.text.split())

            for i in tmp:
                for j in i:
                    j = re.findall('[а-яґєії|[А-ЯҐЄІЇ]|a-z|A-Z]+', j)

                    words.append(''.join(map(str, j)).lower())

            tmp.clear()
        f.close()


def writeInFile(fileName):
    with open(fileName, 'w') as f:
        for i in words:
            f.write(i + ' ')

    print('Result file is: {}'.format(fileName))


if __name__ == '__main__':
    files = findFiles()
    scanFiles(files)
    writeInFile('words.txt')
