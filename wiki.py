import re

def open_text():
    with open('moscow.html','r' , encoding = 'utf-8') as f:
        text = f.read()
    return text

def match(text):
    reg = r'<a\s+href="(.*?)">(.*?)</a>'
    links = re.findall(reg, text)
    print('task1')
    for link in links:
        print(linl[0])
    
    return links

print(open_text())
    
        
