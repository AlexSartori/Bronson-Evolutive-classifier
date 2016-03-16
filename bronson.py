import nltk, random, sys
import matplotlib.pyplot as plt
from nltk.corpus import names
from genome import Genome
from feature_functions import *


def get_features(w, f):
    r = {}
    for ff in f:
        r.update(ff(w))
    return r

#     # features['last-2-cons'] = (w[-1] not in 'aeiou' and w[-2] not in 'aeiou')

# ----------------------------------------------------------------------------------------------------------- Inizio ---
names = ([(name, 'male')   for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)
test_set = names[:500]
train_set = names[500:]

N_GENOMI = 100
N_GENERAZIONI = 100
geni = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23,
        f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36]    # Possibili geni
genomi = []

averages, maxes = [], []    # Statistical data...

# ------------------------------------------------------------------------------------------------ Genera genomi ---
for i in range(N_GENOMI):
    fset = []
    for j in range(random.randint(1, 10)):  # len(geni))):
        index = random.randint(0, len(geni) - 1)
        if geni[index] not in fset:
            fset.append(geni[index])
    genomi.append(Genome(fset, 0))
    # print "    Genoma %d:" % i, fset


for n_generazione in range(1, N_GENERAZIONI + 1):
    print "Generazione %3d: %4s" % (n_generazione, ' '),

    # --------------------------------------------------------------------------- Per ogni genoma calcola precisione ---
    for i, g in enumerate(genomi):
        classifier = nltk.NaiveBayesClassifier.train((get_features(n, g.featureset()), tag) for (n, tag) in train_set)
        a = float(nltk.classify.accuracy(classifier, [(get_features(n, g.featureset()), tag) for (n, tag) in test_set]))
        g.set_accuracy(float(a))
        print "\rGenerazione %3d: %3s %3d/%3d" % (n_generazione, ' ', i + 1, N_GENOMI),
        sys.stdout.flush()
        # print "    Genoma %d:  %.3f  ->  %s" % (i, a, [f.__name__ for f in g.featureset()])

    # print [g.accuracy() for g in genomi]
    averages.append(sum([g.accuracy() for g in genomi]) / N_GENOMI)
    maxes.append(max([g.accuracy() for g in genomi]))
    print "    AVG: %.3f" % averages[-1],
    print "    MAX: %.4f" % maxes[-1]
    genomi = sorted(genomi, key=lambda x: x.accuracy(), reverse=True)
    genomi = genomi[:(N_GENOMI/2)]

    # -------------------------------------------------------------------------------------- Combina genomi migliori ---
    l = len(genomi)
    for i in range(l):
        for j in range(i, l):
            s, m, mj = 0, 0, 0        # sigma, max_sigma, max_sigma_j
            s = genomi[i].sigma(genomi[j])
            if s > m: m, mmj = s, j
        genomi.append(genomi[i].combina(genomi[j], geni))

    # for i, g in enumerate(genomi):
        # print "    Genoma %d:  %.3f  ->  %s" % (i, g.accuracy(), [f.__name__ for f in g.featureset()])

print "\nPlotting results..."
plt.plot(averages, 'b-', label="Average accuracy")
plt.plot(maxes, 'r-', label="Max accuracy")
plt.plot([0, N_GENERAZIONI - 1], [1, 1], 'k--', label="Perfection")
plt.xlabel("Generations")
plt.ylabel("Accuracy")
plt.ylim(ymin=0.5, ymax=1.1)
plt.show()
