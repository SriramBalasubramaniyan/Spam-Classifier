from .data import SPAM_KEYWORDS
import numpy as np

def extract_features(message: str) -> np.ndarray:
    msg_lower = message.lower()
    words = msg_lower.split()

    length = len(message)
    keyword_count = sum(1 for word in words if word in SPAM_KEYWORDS)
    exclamation_count = message.count('!')

    return np.array([length, keyword_count, exclamation_count], dtype=float)