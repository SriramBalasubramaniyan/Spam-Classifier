import numpy as np

class CustomMinMaxScaler:
    def __init__(self):
        self.min_ = None
        self.max_ = None

    def fit(self, X: np.ndarray):
        self.min_ = X.min(axis=0)
        self.max_ = X.max(axis=0)

    def transform(self, X: np.ndarray) -> np.ndarray:
        range_ = self.max_ - self.min_
        range_[range_ == 0] = 1  # Avoid division by zero
        return (X - self.min_) / range_
    
    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        self.fit(X)
        return self.transform(X)