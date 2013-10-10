from pattern.vector import Document, NB, SVM
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
print 'nb distribution = ', nb.distribution
print 'nb confusion matrix = ', nb.confusion_matrix(datadocs[500:])
print 'nb confusion matrix for each class = ', nb.confusion_matrix(datadocs[500:])(True) # (TP, TN, FP, FN)
print 'nb features = ', nb.features
#test set
accuracy, precision, recall, f1 = nb.test(datadocs[500:])
print 'nb accuracy = ', accuracy, 'nb precision =', precision, 'nbrecall = ', \
    recall

#test SVM
testsvm = SVM(train=datadocs[:500])
print 'svm features = ', testsvm.features
saccuracy, sprecision, srecall, sf1 = testsvm.test(datadocs[500:])
print 'svm accuracy =', saccuracy


#classifier training example with test classificaiton
nb2 = NB()
for review, rating in data:
    v = Document(review, type=int(rating))
    #print v.vector
    nb2.train(v)

print 'nb2 classes', nb2.classes
print 'test classification', nb2.classify(Document('A poor movie!'))

#cosine similarity example
from pattern.vector import Vector, distance
v1 = Vector({"curiosity": 1, "kill": 1, "cat": 1})
v2 = Vector({"curiosity": 1, "explore": 1, "mars": 1})
print 'cosine similarity between two vectors', 1 - distance(v1, v2)

# a model is a collection of Document objects

#todo now that we've built SVM, needs to create documents out of dummy tweets
#todo then add them to the SVM classifier as a training and test set
#todo build db schema to save tweets and relationships to db
#todo get some sample twitter data in db