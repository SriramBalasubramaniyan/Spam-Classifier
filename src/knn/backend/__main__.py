from . import Custom_MinMaxScaler as cmms
from . import KNNClassifier as knnc
from . import dataset_builder as db
from . import extract_features as ef
from . import evaluation_metric as em

X_raw, y = db.build_dataset()
 
scaler = cmms.CustomMinMaxScaler()
X_scaled = scaler.fit_transform(X_raw)
 
knn = knnc.KNNClassifier(k=3)
knn.fit(X_scaled, y)

def predict_message(message:str) -> dict:
    features = ef.extract_features(message)
    features_scaled = scaler.transform(features.reshape(1, -1))[0]
    return knn.predict_with_confidence(features_scaled)

if __name__ == "__main__":
    print("=" * 50)
    print("MODEL SELF-TEST")
    print("=" * 50)

    y_pred = knn.predict(X_scaled)
    metrics = em.evaluate(y, y_pred)

    print(f"\n📊 Evaluation Metrics:")
    print(f"  Accuracy  : {metrics['accuracy']}%")
    print(f"  Precision : {metrics['precision']}%")
    print(f"  Recall    : {metrics['recall']}%")
    print(f"  F1 Score  : {metrics['f1']}%")

    print(f"\n  Confusion Matrix:")
    print(f"  TP={metrics['TP']}  FP={metrics['FP']}")
    print(f"  FN={metrics['FN']}  TN={metrics['TN']}")

    print("\n📨 Sample Predictions:")

    test_cases = [
        ("win free money now!!!", "should be SPAM"),
        ("team lunch at noon today", "should be NOT SPAM"),
        ("claim your free prize", "should be SPAM"),
        ("can we reschedule the meeting", "should be NOT SPAM"),
    ]

    for msg, expected in test_cases:
        result = predict_message(msg)
        print(f"\n  Message  : '{msg}'")
        print(f"  Expected : {expected}")
        print(f"  Got      : {result['label']} ({result['confidence']:.0f}% confident)")