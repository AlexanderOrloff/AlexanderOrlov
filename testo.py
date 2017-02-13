import csv
import re

def text():
    with open('rus.txt','r', encoding = 'utf-8') as f:
        text = f.read().lower()
        text = text.split()
        for i in range(len(text)):
            text[i] = text[i].strip('.,?*()«»!\'\":; ')
    return text
def dic(text):
    d ={}
    for i in range(len(text)):
        if text[i] not in d:
            d[text[i]] = 1
        else:
            d[text[i]] += 1
    return d
def write(d):
    with open('some.csv', 'w', encoding='utf-8') as f: ##8
        output = csv.writer(f, delimiter=',')
        header = ['слово', 'частота']
        output.writerow(header)
        for key in d:
            output.writerow([key, d[key]])
def search():
    with open('rus.txt','r', encoding = 'utf-8') as f:
        text = f.read()
        m = re.findall('(?:(?:[А-Яа-яіѢѣ])+[\s,.!\?:;"\(\)\'»\n\t—]+?){3}[А-Яа-яiѢѣ]+?аго [А-Яа-яiѢѣ]+?(?:а|и|я)[\s,.!\?:;"\(\)\'»\n\t—]{,5}(?:[А-Яа-яiѢѣ]+?[\s,.!\?;:—"\(\)\'»\n\t]+?){3}',text)
    with open('answer.txt','w', encoding = 'utf-8')as g:
            g.write('\n'.join(m))
    return

print(len(text()))
write(dic(text()))
search()
