import numpy as np

# After building the model, we measure how good it is.
#
# Confusion Matrix Terms:
#   TP = True Positive  → predicted spam,   actually spam     ✅
#   TN = True Negative  → predicted not spam, actually not spam ✅
#   FP = False Positive → predicted spam,   actually not spam  ❌ (false alarm)
#   FN = False Negative → predicted not spam, actually spam    ❌ (missed spam)
#
# Accuracy  = (TP + TN) / total          → overall % correct
# Precision = TP / (TP + FP)             → of all predicted spam, how many were real spam?
# Recall    = TP / (TP + FN)             → of all real spam, how many did we catch?
 
def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    TP = int(np.sum((y_true == 1) & (y_pred == 1)))
    TN = int(np.sum((y_true == 0) & (y_pred == 0)))
    FP = int(np.sum((y_true == 0) & (y_pred == 1)))
    FN = int(np.sum((y_true == 1) & (y_pred == 0)))

    total = len(y_true)
    accuracy = (TP + TN) / total if total > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "TP": TP, "TN": TN, "FP": FP, "FN": FN,
        "accuracy":  round(accuracy * 100, 1),
        "precision": round(precision * 100, 1),
        "recall":    round(recall * 100, 1),
        "f1":        round(f1 * 100, 1),
    }