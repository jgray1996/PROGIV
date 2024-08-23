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
        return

    def transform_data(self, object):
        return

    def save_predictions(self, object):
        return

    def save_plots(self, object):
        return
