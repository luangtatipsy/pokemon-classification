import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.layers import GlobalMaxPool2D


class ResNet50Vectorizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.model = ResNet50(
            input_shape=(None, None, 3), include_top=False, weights="imagenet"
        )
        self.preprocessing_fn = preprocess_input

    def __preprocess(self, img):
        return self.preprocessing_fn(img)

    def __vectorize(self, img):
        x = self.__preprocess(img)
        x = np.expand_dims(x, axis=0)
        x = self.model(x)
        x = GlobalMaxPool2D()(x)

        return x[0].numpy()

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X):
        return np.array([self.__vectorize(img) for img in X])
