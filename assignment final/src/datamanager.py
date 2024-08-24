import os
import pandas as pd
from datetime import datetime


class DataManager:
    """
    A class to manage data-related operations such as file handling, data formatting, 
    and preprocessing for machine learning tasks.
    """

    def get_filenames(self, path):
        """
        Retrieve the list of filenames in the specified directory.

        Parameters:
        path (str): The directory path from which to list files.

        Returns:
        list: A list of filenames present in the specified directory.
        """
        return os.listdir(path)

    def remove_file(self, path, file):
        """
        Remove a specified file from the given directory.

        Parameters:
        path (str): The directory path where the file is located.
        file (str): The name of the file to remove.

        Returns:
        None
        """
        return os.remove(f"{path}{file}")

    def read_dataframe(self, object, path):
        """
        Read the last file in the given list of filenames into a pandas DataFrame.

        Parameters:
        object (list): A list of filenames.
        path (str): The directory path where the file is located.

        Returns:
        pandas.DataFrame: The loaded data as a pandas DataFrame.
        """
        data = pd.read_csv(path + object[-1])
        return data

    def format_dataframe(self, df_object):
        """
        Convert the 'timestamp' column to datetime format and set it as the DataFrame index.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame to format.

        Returns:
        pandas.DataFrame: The formatted DataFrame with 'timestamp' as the index.
        """
        df_object.timestamp = pd.to_datetime(df_object.timestamp)
        df_object = df_object.set_index("timestamp")
        return df_object

    def create_fractions(self, df_object):
        """
        Split the DataFrame into separate DataFrames based on the 'machine_status' column.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame to split.

        Returns:
        tuple: Three DataFrames corresponding to rows where 'machine_status' is 'BROKEN', 
               'RECOVERING', and 'NORMAL'.
        """
        broken_rows = df_object[df_object["machine_status"] == "BROKEN"]
        recovery_rows = df_object[df_object["machine_status"] == "RECOVERING"]
        normal_rows = df_object[df_object["machine_status"] == "NORMAL"]
        return broken_rows, recovery_rows, normal_rows

    def remove_machine_status(self, df_object):
        """
        Remove the 'machine_status' column from the DataFrame.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame from which to remove the column.

        Returns:
        pandas.DataFrame: The DataFrame without the 'machine_status' column.
        """
        m, n = df_object.shape
        return df_object.iloc[:, : n - 1]

    def fill_nans(self, df_object):
        """
        Fill NaN values in the DataFrame with the mean of each column.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame to process.

        Returns:
        pandas.DataFrame: The DataFrame with NaN values filled.
        """
        return df_object.fillna(df_object.mean())

    def drow_low_quality(self, df_object, cut_off=10):
        """
        Drop columns from the DataFrame where the percentage of missing values exceeds a cutoff.

        Parameters:
        df_object (pandas.DataFrame): The DataFrame to process.
        cut_off (int, optional): The maximum percentage of missing values allowed per column. 
                                 Columns exceeding this will be dropped. Default is 10%.

        Returns:
        pandas.DataFrame: The DataFrame with low-quality columns removed.
        """
        percentage_missing = df_object.isnull().sum() / len(df_object) * 100
        keep = df_object.columns[percentage_missing < cut_off]
        return df_object[keep]

    def save_predictions(self, np_object, df_object, predictions, path):
        """
        Save predictions along with the corresponding data to a CSV file.

        Parameters:
        np_object (numpy.ndarray): The processed data used for predictions.
        df_object (pandas.DataFrame): The original DataFrame.
        predictions (numpy.ndarray): The predictions made by the model.
        path (str): The directory path to save the CSV file.

        Returns:
        pandas.DataFrame: The DataFrame containing the data and predictions.
        """
        now = datetime.now().strftime("%H_%M_%S")
        df = pd.DataFrame(np_object)
        df.columns = df_object.columns
        df["predictions"] = predictions
        df.to_csv(f"{path}prediction_{now}.csv")
        return df
