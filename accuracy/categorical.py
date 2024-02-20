import numpy
from .accuracy import Accuracy

class Categorical(Accuracy):
    def __init__(self, *, binary=False):
        self.binary = binary
    
    def init(self, y):
        pass
    
    def compare(self, predictions, y):
        if not self.binary and len(y.shape) == 2:
            y = numpy.argmax(y, axis=1)
        return predictions == y