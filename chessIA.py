import pandas as pd
import math
from processing import *

"""
Creates training and test datasets from an Excel file with header
Returns a dupla of pandas.DataFrame

Arguments:
- filename of the data source
- size of training dataset from the total
"""
def get_dataset(filename, size):
    data_df = pd.read_excel(filename, header=0)
    # removal of null values
    data_df = data_df[data_df.apply(
        lambda row: pd.notnull(row['moves']), axis=1)]
    total = data_df.shape
    ds_size = math.ceil(total*size)
    training = data_df['moves'].values[:ds_size]
    test = data_df['moves'].values[ds_size+1:]
    return training, test

"""
Deep learning algorithm
Returns a model capable of identifying the moves allowed for a given chess piece
"""
def main():
    games, games_test = get_dataset("echec.xlsx", 2/3)
    training = list(games)
    test = list(games_test)

    parced_training = []
    parced_test = []

    for game in training:
        encoded = parse_movements(game)
        parced_training.append(encoded)

    for game in test:
        encoded = parse_movements(game)
        parced_test.append(encoded)


if __name__ == "__main__":
    main()
