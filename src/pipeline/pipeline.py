from sklearn.pipeline import make_pipeline
from .transformers.general import DataFrameSelector
from sklearn.preprocessing import StandardScaler


def create_pipeline():
    return make_pipeline(DataFrameSelector(['a', 'b' 'c']), StandardScaler)
