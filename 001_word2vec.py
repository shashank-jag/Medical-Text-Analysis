#import gensim
#model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True) 


import gensim.models.keyedvectors as word2vec

embed_map = word2vec.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True) 

print("************************")

dog = embed_map['dog']
print(dog) 
