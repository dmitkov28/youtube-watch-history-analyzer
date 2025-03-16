import pandas as pd


def load_json_as_df(file_path: str) -> pd.DataFrame:
    return pd.read_json(file_path)
