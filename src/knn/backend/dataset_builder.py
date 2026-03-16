from . import extract_features as ef
import numpy as np
from .data import messages, labels

def build_dataset():
    x = np.array([ef.extract_features(msg) for msg in messages])
    y = np.array(labels)
    return x, y