
from sklearn.datasets import fetch_20newsgroups
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
news_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)
news_test = fetch_20newsgroups(subset='test', shuffle=True,categories=categories)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect',TfidfVectorizer()),
                    ('clf',MultinomialNB()),
                    ])

text_clf.fit(news_train.data,news_train.target)
predicted = text_clf.predict(news_test.data)

from sklearn import metrics
import numpy as np
print('Accuracy achieved is ' + str(np.mean(predicted == news_test.target)))
print(metrics.classification_report(news_test.target, predicted, target_names=news_test.target_names))
metrics.confusion_matrix(news_test.target, predicted)
