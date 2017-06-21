import re

def texting():
    with open ('text.xml','r',encoding = 'utf-8') as f:
        text = f.read()
    m = re.findall('<w>.*?</w>', text)
    return m

def counting(m):
    sum, words = 0,0
    for line in m:
        count = re.findall('<ana', line)
        sum += len(count)
    print ( sum / len(m) )
    
def morpho(m):
    d = {}
    for line in m:
        morph = re. findall ('[A-Z]+', line)
        for word in morph:
            if  word not in d:
                d[word] = 1
        else:
                d[word] += 1
    return d

def filing(d):
    with open('file.txt', 'w', encoding = 'utf - 8') as f:
        for key in d:
            string = key + '\t' + str(d[key]) + '\n'
            f.write(string)
            
def instrumentalis(m):
    arr = []
    for index, line in enumerate(m):
        if ('S' in line) and ('ins' in line):
            s = ''

            try:
                word = re.search('[а-яА-ЯЁё]+', m[index- 3])
                s = s + word.group()  + ' '
            except:
                continue
            try:
                word = re.search('[а-яА-ЯЁё]+', m[index- 2])
                s = s + word.group() + ' '
            except:
                continue
            try:
                word = re.search('[а-яА-ЯЁё]+', m[index- 1])
                s = s + word.group() + ' \t'
            except:
                continue

            word = re.search('[а-яА-ЯЁё]+', line)
            s += word.group()

            try:
                word = re.search('[а-яА-ЯЁё]+', m[index + 1])
                s = s + ' \t'  + word.group()
            except:
                continue
                
            try:
                word = re.search('[а-яА-ЯЁё]+', m[index + 2])
                s = s + ' ' + word.group()
            except:
                continue

            try:
                word = re.search('[а-яА-ЯЁё]+', m[index + 3])
                s = s + ' ' + word.group()
            except:
                continue
            
            arr.append(s)
    return arr

def written(arr):
    with open('write.txt', 'w', encoding = 'utf - 8') as f:
        for line in arr:
            f.write(line)
counting(texting())
filing(morpho(texting()))
written(instrumentalis(texting()))

