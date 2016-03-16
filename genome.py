import random


class Genome:

    def __init__(self, featureset, accuracy):
        self.f = featureset
        self.a = float(accuracy)

    def set_accuracy(self, accuracy):
        self.a = float(accuracy)

    def accuracy(self):
        return float(self.a)

    def featureset(self):
        return self.f

    def sigma(self, other):
        a, b = self, other
        N = len(set(a.featureset() + b.featureset()))
        E = len(list(set(b.featureset()) - set(a.featureset())))
        D = len(list(set(a.featureset()) - set(b.featureset())))
        return float((D + E) / N)

    def combina(self, other, mutations):
        if self.accuracy() > other.accuracy(): a, b = self, other
        else: a, b = other, self
        f1, f2, f3 = a.featureset(), b.featureset(), []
        if self.accuracy() == other.accuracy: f3 = set(f1 + f2)
        else: f3 = f1[:]

        for i in range(random.randint(0, len(f3))):
            if random.randint(0, 3) >= 1:
                del f3[random.randint(0, len(f3) - 1)]
            if random.randint(0, 3) >= 1:
                rm = mutations[random.randint(0, len(mutations) - 1)]
                if rm not in f3: f3.append(rm)
        return Genome(f3, 0)

# nf = 37
# for l in 'abcdefghijklmnopqrstuvwxyz':
#       print "def f%d(w):" % nf
#       nf += 1
#       print "    return {'has-" + l + "': '" + l + "' in w}"
#       print ""
