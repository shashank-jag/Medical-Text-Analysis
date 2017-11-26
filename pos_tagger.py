from nltk.tokenize import PunktSentenceTokenizer
from geniatagger import GeniaTagger

tagger = GeniaTagger('~/qwerty/shashank/geniatagger-3.0.2/geniatagger')
print(tagger.parse('This is a pen.'))
#print(tagger.parse('tis is  pen'))

#print(data)
med_tokenizer = PunktSentenceTokenizer(train_data)

