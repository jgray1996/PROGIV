import os
import pandas as pd


class DataManager:

    def get_filenames(self, path):
        return os.listdir(path)

    # add logger
    def new_file(self, old, new):
        if old == new:
            return False
        elif len(old) < len(new):
            return True

    def remove_file(self, name):
        return

    def read_dataframe(self, object):
        data = pd.read_csv("input/" + object[0])
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
        percentage_missing = df_object.isnull().sum()/len(df_object)*100
        keep = df_object.columns[percentage_missing < cut_off]
        return df_object[keep]

    def save_predictions(self, object):
        return

    def save_plots(self, object):
        return
