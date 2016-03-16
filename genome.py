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
