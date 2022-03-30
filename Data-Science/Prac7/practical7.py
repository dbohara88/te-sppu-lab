import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""

#Sentence Tokenization
tokenized_text=sent_tokenize(text)
print("\n#Sentence Tokenization")
print(tokenized_text)


#Word Tokenization
tokenized_word=word_tokenize(text)
print("\n#Word Tokenization")
print(tokenized_word)


#Removing Stopwords
print("\n#Removing Stopwords")
stop_words=set(stopwords.words("english"))
filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_word)
print("\nFilterd Sentence:",filtered_sent)


#Stemming
ps =PorterStemmer()
stemmed_words=[]
for w in tokenized_word:
    stemmed_words.append(ps.stem(w))
print("\nStemmed Sentence:",stemmed_words)

#Lemmatization
lemmed_words = []
lem = WordNetLemmatizer()
for w in tokenized_word:
    lemmed_words.append(lem.lemmatize(w))
print("\nLemmatized Sentence:",lemmed_words)

#POS Tagging
sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)
pos_tagging = nltk.pos_tag(tokens)
print("\nPOS Tagging:",pos_tagging)