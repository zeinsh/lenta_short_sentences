# version 0
import nltk
####### Tokenizers #########
# follow instructions to use tokenizer for Russian sentences https://github.com/Mottl/ru_punkt
tokenizer_ru = nltk.data.load('tokenizers/punkt/russian.pickle')
def getTokenizer(lang):
    tokenizers={
        'ru': tokenizer_ru
    }
    return tokenizers.get(lang, tokenizer_ru)
def tokenize_sent(text, lang='ru'):
    tokenizer=getTokenizer(lang)
    return tokenizer.tokenize(text)

if __name__=="__main__":
    text = "Ай да А.С. Пушкин! Ай да сукин сын!"
    print(tokenize_sent(text))
