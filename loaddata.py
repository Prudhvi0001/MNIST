import mnist as MNIST
import cv2


class LoadData():
    def __init__(self):
        self.mndata = MNIST(path="data/", )

    def train_data(self):
        xtrain, ytrain = mndata.load_training()
        return xtrain, ytrain

    def test_data(self):
        xtest, ytest = mndata.load_testing()
        return xtest, ytest
