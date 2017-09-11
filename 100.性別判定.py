import numpy as np
from sklearn.cross_validation import train_test_split

np.random.seed(9)
txtbody = open('/Users/JUN/minpy4th-samplecodes/Chapter12/names.txt', encoding = 'utf-8')
jnames = np.array([x.split() for x in txtbody], dtype = 'U12')
names_train, gender_train, = jnames[:, 1], jnames[:, 0]

def split_in_2word(name):
    return [name[i:i + 2] for i in range(len(name) - 1)]

from sklearn.feature_extraction.text import CountVectorizer
bow_t = CountVectorizer(analyzer=split_in_2word).fit(names_train)

names_bow = bow_t.transform(names_train)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_t = TfidfTransformer().fit(names_bow)

from sklearn.naive_bayes import MultinomialNB
names_tfidf = tfidf_t.transform(names_bow)
namegender_detector = MultinomialNB().fit(names_tfidf,gender_train)

def predict_gender(name):
    bow = bow_t.transform([name])
    n_tfidf = tfidf_t.transform(bow)
    return namegender_detector.predict(n_tfidf)[0]

print(predict_gender(input('名前を入力してください：')))
