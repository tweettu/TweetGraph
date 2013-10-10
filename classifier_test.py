from pattern.vector import Document, NB
from pattern.db import Datasheet

data = Datasheet.load('reviews.csv', headers=True)
print data
datalist = [(review, int(rating)) for review, rating in data]
print datalist
datadocs = [Document(review, type=rating, stopwords=True) for review, rating
            in datalist]
print datadocs

#naive Bayes
#training set
nb = NB(train=datadocs[:500])
print nb.distribution
print nb.features
print nb.majority
print nb.minority
#test set
accuracy, precision, recall, f1 = nb.test(data[500:])
print accuracy

nb2 = NB()
for review, rating in csv('reviews.csv'):
    v = Document(review, type=int(rating), stopwords=True)
    nb2.train(v)

print nb2.classes
print nb2.classify(Document('A good movie!'))