from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from transformers.general import DataFrameSelector


def create_pipeline():
    return make_pipeline(DataFrameSelector('a', 'b' 'c'), StandardScaler)
