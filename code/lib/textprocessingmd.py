# URLS ENGLISH RUSSIAN
import re
URL_REGEX=r'(http[s]?://){0,1}[-a-zA-ZА-я0-9@:%._\+~#=]{2,256}\.[a-zА-я]{2,6}\b([-a-zА-яA-Z0-9@:%_\+.~#?&//=]*)'
def FindURLS(text):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall(URL_REGEX, text)
    return url
def replaceURL(text):
    text = re.sub(URL_REGEX,' <URL> ', text)
    return text

def replaceDigits(text):
    text = re.sub(r'[0-9]','D', text)
    text = text.replace('D.D','DFD')
    for i in range(20,0,-1):
        text=text.replace('D'*i+'F','F')
    for i in range(20,0,-1):
        text=text.replace('F'+'D'*i,'F')
    for i in range(20,5,-1):
        text=text.replace('D'*i,'N')
    return text
