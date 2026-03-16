import sys
from pathlib import Path
import streamlit as st

root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path))

from knn.backend.__main__ import predict_message,knn,scaler
from knn.backend.dataset_builder import build_dataset
from knn.backend.evaluation_metric import evaluate
from knn.backend.extract_features import extract_features

# PAGE CONFIG

st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📨",
    layout="centered",
)

# HEADER

st.title("📨 Spam Classifier")
st.markdown("Enter a message below to see if it's classified as **SPAM** or **NOT SPAM** by our KNN model.")
st.divider()

# MAIN — MESSAGE INPUT

st.subheader("Enter Your Message")

msg = st.text_area(
    label="Type or paste your message below:",
    placeholder="e.g. Congratulations! You've won a free prize. Claim now!",
    height=120,
)

col1, col2, col3 = st.columns([1,1,2])
predict_btn = col1.button("🔍 Predict", type="primary", use_container_width=True)
clear_btn   = col2.button("🗑️ Clear",   use_container_width=True)

if predict_btn:
    if msg.strip() == "":
        st.warning("Please enter a message first.")
    else:
        result = predict_message(msg)

        st.divider()
        st.subheader("🔎 Result")
 
        if result["prediction"] == 1:
            st.error(f"## {result['label']}")
            bar_color = "🔴"
        else:
            st.success(f"## {result['label']}")
            bar_color = "🟢"
 
        confidence = result['confidence']
        st.markdown(f"**Confidence:** {confidence:.0f}%")
        st.progress(confidence / 100)

        st.markdown("---")
        st.markdown("**How the KNN voted (K=3 neighbors):**")

        vote_col1, vote_col2 = st.columns(2)
 
        vote_col1.metric(
            label="❌ Spam votes",
            value=f"{result['spam_votes']} / {result['k']}"
        )
        vote_col2.metric(
            label="✅ Not Spam votes",
            value=f"{result['not_spam_votes']} / {result['k']}"
        )

        st.divider()
        st.subheader("🔬 Feature Breakdown")
        st.markdown("*These are the 3 numbers your message was converted into:*")

        raw_features = extract_features(msg)

        feat_col1, feat_col2, feat_col3 = st.columns(3)
        feat_col1.metric("📏 Message Length",    f"{int(raw_features[0])} chars")
        feat_col2.metric("🔑 Spam Keywords",     f"{int(raw_features[1])} found")
        feat_col3.metric("❗ Exclamation Marks", f"{int(raw_features[2])} found")

with st.sidebar:
    st.header("📚 About This Model")
    st.markdown(
        """
        This classifier was built **from scratch using NumPy**!
        
        **Algorithm:** K-Nearest Neighbors (K=3)
        
        **How it works:**
        1. Your message → 3 numeric features
        2. Scaled to [0, 1] range
        3. Distance compared to 30 training examples
        4. 3 nearest neighbors vote
        5. Majority wins → prediction
        
        **Features used:**
        - `length` → character count
        - `keyword_count` → spam word matches
        - `exclamation_count` → ! marks
        """
    )
    st.divider()
    st.header("📊 Model Performance")
    st.markdown("*Evaluated on training data:*")

    X_raw, y_true = build_dataset()
    X_scaled_eval = scaler.transform(X_raw)
    y_pred = knn.predict(X_scaled_eval)
    metrics = evaluate(y_true, y_pred)

    m1, m2 = st.columns(2)
    m1.metric("Accuracy",  f"{metrics['accuracy']}%")
    m2.metric("F1 Score",  f"{metrics['f1']}%")
    m1.metric("Precision", f"{metrics['precision']}%")
    m2.metric("Recall",    f"{metrics['recall']}%")

    st.divider()
    st.header("🧮 Confusion Matrix")

    st.markdown(
        """
        | | **Predicted Spam** | **Predicted Not Spam** |
        |---|---|---|
        | **Actually Spam** | TP = {TP} ✅ | FN = {FN} ❌ |
        | **Actually Not Spam** | FP = {FP} ❌ | TN = {TN} ✅ |
        """.format(**metrics))
 
    st.caption(
        """
        - **TP** = Caught spam correctly
        - **TN** = Correctly passed ham
        - **FP** = False alarm (ham flagged as spam)
        - **FN** = Missed spam (spam got through)
        """)