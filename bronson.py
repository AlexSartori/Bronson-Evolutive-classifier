import nltk, random
from nltk.corpus import names
from genome import Genome


def f0(w):
    return {'last-letter': w[-1]}

def f1(w):
    return {'last-2-letters': w[-2:]}

def f2(w):
    return {'last-3-letters': w[-3:]}

def f3(w):
    return {'first-letter': w[0]}

def f4(w):
    return {'first-2-letters': w[:2]}

def f5(w):
    return {'first-3-letters': w[:3]}

def get_features(w, f):
    r = {}
    for ff in f:
        r.update(ff(w))
    return r

# Possibili geni
geni = [f0, f1, f2, f3, f4, f5]

# def gender_features(w):
#     features = {}
#     # features['last-letter']  = word[-1]
#     # for l in "abcdefghjklmnopqrstuvwxyz":
#     #     features['count %s' % l] = name.lower().count(l)
#     for l in "abcdefghjklmnopqrstuvwxyz":
#         features['has %s' % l] = (l in name.lower())
#     features['last-3'] = w[-3:]
#     features['first-3'] = w[:3]
#     # features['len'] = len(w)
#     # features['v_count'] = sum(w.count(l) for l in 'aeiou')
#     # features['c_count'] = sum(w.count(l) for l in 'qwrtyplkjhgfdszxcvbnm')
#     # features['last-2-cons'] = (w[-1] not in 'aeiou' and w[-2] not in 'aeiou')
#     return features

# ---------------------------------------------------------------------------------------------------------------------
names = ([(name, 'male')   for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)
test_set = names[:1000]
train_set = names[1000:]

# - Genera genomi
N_GENOMI = 10
genomi = []

print "Generazione N:"
for i in range(N_GENOMI):
    fset = []
    for j in range(random.randint(1, len(geni))):
        index = random.randint(0, len(geni) - 1)
        if geni[index] not in fset:
            fset.append(geni[index])
    genomi.append(Genome(fset, 0))
    # print "    Genoma %d:" % i, fset

# - Per ogni genoma calcola precisione
for i, g in enumerate(genomi):
    classifier = nltk.NaiveBayesClassifier.train((get_features(n, g.featureset()), tag) for (n, tag) in train_set)
    a = float(nltk.classify.accuracy(classifier, [(get_features(n, g.featureset()), tag) for (n, tag) in test_set]))
    g.set_accuracy(float(a))
    print "    Genoma %d:  %.3f  -->  %s" % (i, a, [f.__name__ for f in g.featureset()])


# - Combina genomi migliori e scarta peggiori
# - Ripeti










#
# print "Errors in dev_test set:"
# for (n, g) in dev_names:
#     guess = classifier.classify(gender_features(n))
#     if guess != g:
#         print "        Name: %-15s Correct: %-8s Guess: %-8s" % (n, g, guess)
#
# classifier.show_most_informative_features(20)
#
# print "Accuracy: %s" % (nltk.classify.accuracy(classifier, dev_set))
#
# for n in ['Luke', 'Ben', 'Leia', 'Neo']:
#     print "%-10s %s" % (n, classifier.classify(gender_features(n)))
#
# classifier.classify(gender_features('Ben'))
# classifier.show_most_informative_features(5)
# print nltk.classify.accuracy(classifier, dev_set)
