from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
import kss
from nltk.tag import pos_tag
from konlpy.tag import Okt, Kkma

tokenizer=TreebankWordTokenizer()

okt = Okt()

kkma = Kkma()

print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))  ## 모두 token 화

print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop.")) # ''' 단위는 띄움

print(text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop.")) #"don't 는 하나로 인식

text="Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own." # home-based 하나로 인식, does n't로 인식 --> 일반 word tokenizer와 동일

print(tokenizer.tokenize(text))


sentence="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."
print(sent_tokenize(sentence))

korean_sentence = "딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?"

print(kss.split_sentences(korean_sentence))

print(pos_tag(tokenizer.tokenize(text)))

print(okt.morphs(korean_sentence))

print(okt.pos(korean_sentence))

print(okt.nouns(korean_sentence))

print("====================================================")

print(kkma.morphs(korean_sentence))

print(kkma.pos(korean_sentence))

print(kkma.nouns(korean_sentence))