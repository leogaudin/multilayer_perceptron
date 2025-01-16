import pandas as pd
import numpy as np


def load_data(
    train_path: str = None,
    test_path: str = None,
):
    features = [
        "Radius",
        "Texture",
        "Perimeter",
        "Area",
        "Smoothness",
        "Compactness",
        "Concavity",
        "Concave points",
        "Symmetry",
        "Fractal dimension",

        "Radius SE",
        "Texture SE",
        "Perimeter SE",
        "Area SE",
        "Smoothness SE",
        "Compactness SE",
        "Concavity SE",
        "Concave points SE",
        "Symmetry SE",
        "Fractal dimension SE",
        "Radius worst",
        "Texture worst",
        "Perimeter worst",
        "Area worst",
        "Smoothness worst",
        "Compactness worst",
        "Concavity worst",
        "Concave points worst",
        "Symmetry worst",
        "Fractal dimension worst",
    ]

    X_train, y_train, X_test, y_test = None, None, None, None

    if train_path is not None:
        df_train = pd.read_csv(train_path, index_col=False, header=0)

        X_train = df_train.drop(columns=["Diagnosis"])
        X_train = X_train[features].values
        y_train = df_train["Diagnosis"].values

    if test_path is not None:
        df_test = pd.read_csv(test_path, index_col=False, header=0)
        X_test = df_test.drop(columns=["Diagnosis"])
        X_test = X_test[features].values
        y_test = df_test["Diagnosis"].values

    return X_train, y_train, X_test, y_test


def to_categorical(y):
    set = np.unique(y)
    y_one_hot = np.zeros((len(y), len(set)))
    for i, val in enumerate(y):
        y_one_hot[i, np.where(set == val)] = 1
    return y_one_hot
