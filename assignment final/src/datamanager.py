import os
import pandas as pd
from datetime import datetime


class DataManager:

    def get_filenames(self, path):
        return os.listdir(path)

    def remove_file(self, path, file):
        return os.remove(f"{path}{file}")

    def read_dataframe(self, object, path):
        data = pd.read_csv(path + object[-1])
        return data

    def format_dataframe(self, df_object):
        df_object.timestamp = pd.to_datetime(df_object.timestamp)
        df_object = df_object.set_index("timestamp")
        return df_object

    def create_fractions(self, df_object):
        broken_rows = df_object[df_object["machine_status"] == "BROKEN"]
        recovery_rows = df_object[df_object["machine_status"] == "RECOVERING"]
        normal_rows = df_object[df_object["machine_status"] == "NORMAL"]
        return broken_rows, recovery_rows, normal_rows

    def remove_machine_status(self, df_object):
        m, n = df_object.shape
        return df_object.iloc[:, : n - 1]

    def fill_nans(self, df_object):
        return df_object.fillna(df_object.mean())

    def drow_low_quality(self, df_object, cut_off=10):
        percentage_missing = df_object.isnull().sum() / len(df_object) * 100
        keep = df_object.columns[percentage_missing < cut_off]
        return df_object[keep]

    def save_predictions(self, np_object, df_object, preditions, path):
        now = datetime.now().strftime("%H_%M_%S")
        df = pd.DataFrame(np_object)
        df.columns = df_object.columns
        df["predictions"] = preditions
        df.to_csv(f"{path}prediction_{now}.csv")
        return df
