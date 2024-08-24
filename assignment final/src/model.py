import pickle
import sklearn as sk
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest


class Model:
    """
    A class to handle model-related operations including data scaling, training, 
    saving, loading, and anomaly detection using an Isolation Forest.
    """

    def scale_data(self, df_object):
        """
        Scale the data using StandardScaler to normalize the features.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame to scale.

        Returns:
        numpy.ndarray: The scaled data.
        """
        scaler = StandardScaler()
        return scaler.fit_transform(df_object)

    def calculate_anomoly_cutoff(self, df_object, normal_rows):
        """
        Calculate the contamination rate for the Isolation Forest model, 
        based on the proportion of normal rows.

        Parameters:
        df_object (pandas.DataFrame): The entire dataset.
        normal_rows (pandas.DataFrame): The subset of normal rows.

        Returns:
        float: The calculated contamination rate.
        """
        return 1 - (len(normal_rows) / (len(df_object)))

    def train_model(self, object, contaminations, n_jobs=-1):
        """
        Train an Isolation Forest model to detect anomalies.

        Parameters:
        object (numpy.ndarray): The data to train the model on.
        contaminations (float): The contamination rate (proportion of outliers in the data).
        n_jobs (int, optional): The number of parallel jobs to run. Default is -1 (use all processors).

        Returns:
        IsolationForest: The trained Isolation Forest model.
        """
        ifm = IsolationForest(contamination=contaminations, n_jobs=n_jobs)
        print("fitting model...")
        return ifm.fit(object)

    def load_model(self, path="src/model.fit"):
        """
        Load a pre-trained model from a file.

        Parameters:
        path (str, optional): The file path to the saved model. Default is "src/model.fit".

        Returns:
        IsolationForest: The loaded Isolation Forest model.
        """
        with open(path, "rb") as model_in:
            return pickle.load(model_in)

    def save_model(self, model, path="src/model.fit"):
        """
        Save a trained model to a file.

        Parameters:
        model (IsolationForest): The trained model to save.
        path (str, optional): The file path where the model will be saved. Default is "src/model.fit".

        Returns:
        None
        """
        with open(path, "wb") as model_out:
            pickle.dump(model, model_out)

    def classify(self, model, np_object):
        """
        Use the trained model to classify data points as normal or anomalies.

        Parameters:
        model (IsolationForest): The trained model to use for classification.
        np_object (numpy.ndarray): The data to classify.

        Returns:
        numpy.ndarray: The classification results, where -1 indicates anomalies and 1 indicates normal points.
        """
        return model.predict(np_object)
