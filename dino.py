import re

def open_text():
    with open('dino.html','r',encoding ='utf-8') as f:
        text = f.read()
    return text
def search(text):
    dino = re.findall(r'\b[Дд]инозавр\w?\w?\w?\b', text)
    return dino
def tags(text):
    m = re.sub('<.*?>','', text, flags = re.DOTALL)
    #udalyaem tegi
    m = re.sub(r'(\n| ){2,}','',m, flags = re.DOTALL)
    m = re.sub(r'\bдинозавр(\w?\w?\w?)\b','кот\\1',m)
    m = re.sub(r'\bДинозавр(\w?\w?\w?)\b','Кот\\1',m)
    return m
def imagen(text):
    m = re.findall('<img.*?alt ?= ?"(.*?)"',text, flags = re.DOTALL)
    return m
def pyatoe(text):
    m = re.sub('[аыуеёоияю]','[о]')
    m = re.sub
    
    
print(search(open_text()))
print(tags(open_text()))
print(imagen(open_text()))
