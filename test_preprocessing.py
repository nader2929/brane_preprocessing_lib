import preprocessing
import os
import shutil
from pandas import util as putil
import pandas as pd
from functools import wraps
import sys


def with_data_folder(func):
    @wraps(func)
    def create_data_run_rm_data(*args, **kwargs):
        data_folder = "./data"
        os.makedirs(data_folder, exist_ok=True)

        func(*args, **kwargs)
        shutil.rmtree(data_folder)
    return create_data_run_rm_data

@with_data_folder
def test_analyse_column():
    df = putil.testing.makeDataFrame()
    input_data_path = "./data/test_df.csv"
    df.to_csv(input_data_path)

    output_df_path = "./data/col_analysed.csv"
    output = preprocessing.analyse_column(df.columns[0], False, "./data/test_df.csv", output_df_path)
    assert output == "Results saved to file: ./data/col_analysed.csv, in data directory"

    output_df = pd.read_csv(output_df_path)
    # print(output_df.columns, file=sys.stdout)
    assert len(output_df) > 0
    assert list(output_df.columns) == ['A', 'A_counts', 'A_perc']

@with_data_folder
def test_train_and_test_classifier():
    df = putil.testing.makeMixedDataFrame()
    df.drop(columns=["D"], inplace=True)
    input_data_path = "./data/test_df.csv"
    df.to_csv(input_data_path)
    output_model_path = "./data/model.pkl"
    output = preprocessing.train_and_test_classifier("C", 0.1, "mlp", True, False, input_data_path, output_model_path)
    assert output is not None
    assert os.path.exists(output_model_path)

@with_data_folder
def test_load_classifier_and_predict():
    test_train_and_test_classifier.__wrapped__()
    df = putil.testing.makeMixedDataFrame()
    df.drop(columns=["D","C"], inplace=True)
    input_data_path = "./data/test_df.csv"
    df.to_csv(input_data_path)
    output_data_path = "./data/predictions.csv"

    output = preprocessing.load_classifier_and_predict("./data/model.pkl", input_data_path, "", False, True, output_data_path)
    assert output is not None
    assert os.path.exists(output_data_path)