import numpy as np

class KNNClassifier:
    def __init__(self,k:int=3):
        self.k = k
        self.x_train = None
        self.y_train = None

    def fit(self,x: np.ndarray,y: np.ndarray):
        self.x_train = x
        self.y_train = y    

    def ecuclidean_distance(self,a: np.ndarray,b: np.ndarray) -> float:
        """
        Euclidean distance = √Σ(aᵢ - bᵢ)²
        It's the straight-line distance between two points.
        """
        return np.sqrt(np.sum((a-b)**2)) 

    def predict_one(self,x: np.ndarray) -> int:
        """
        Predict the label for a single feature vector x.
        Returns 1 (spam) or 0 (not spam).
        """ 
        distance = [
            self.ecuclidean_distance(x,x_train) for x_train in self.x_train 
            # calculate the distance between the input and each point in the training set
        ]

        distance = np.array(distance) 
        # convert the list of distances to a numpy array

        nearest_indices = np.argsort(distance)[:self.k] # get the index of the k nearest neighbors
        nearest_labels = self.y_train[nearest_indices] # get the labels of the k nearest neighbors

        spam_votes = np.sum(nearest_labels == 1)
        not_spam_votes = np.sum(nearest_labels == 0)
        # count the number of spam and not-spam votes among the nearest neighbors

        # return 1 if there are more spam votes than not-spam votes, otherwise return 0
        return 1 if spam_votes > not_spam_votes else 0 
    
    def predict(self,X: np.ndarray) -> np.ndarray:
        return np.array([self.predict_one(x) for x in X])
    
    def predict_with_confidence(self,x: np.ndarray) -> dict:
        """
        Predict + return confidence score (what % of neighbors voted spam).
        This gives us a 0–100% certainty score to show in the UI.
        """
        distance = [
            self.ecuclidean_distance(x,x_train) for x_train in self.x_train 
            # calculate the distance between the input and each point in the training set
        ]
        k_nearest_indices = np.argsort(distance)[:self.k] # get the index of the k nearest neighbors
        k_nearest_labels = self.y_train[k_nearest_indices] # get the labels of the k nearest neighbors

        spam_votes = int(np.sum(k_nearest_labels == 1))
        not_spam_votes = int(np.sum(k_nearest_labels == 0))
        total_votes = spam_votes + not_spam_votes
        # count the number of spam and not-spam votes among the nearest neighbors

        prediction = 1 if spam_votes > not_spam_votes else 0
        confidence = (max(spam_votes, not_spam_votes) / total_votes) * 100 if total_votes > 0 else 0
        
        return {
            "prediction": prediction,
            "label": "❌ Spam" if prediction == 1 else "✅ Not Spam",
            "confidence": confidence,
            "spam_votes": spam_votes,
            "not_spam_votes": not_spam_votes,
            "k": self.k,
        }