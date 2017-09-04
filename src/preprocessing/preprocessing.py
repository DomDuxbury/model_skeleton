import os
import pandas as pd


def get_from_root_dir(path):
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.join(current_dir, os.path.pardir, os.path.pardir)
    return os.path.join(root_dir, path)


def get_data(nrows=None):
    data_path = get_from_root_dir('data/data.csv')
    return pd.read_csv(data_path, nrows=nrows)
