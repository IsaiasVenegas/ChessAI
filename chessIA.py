import pandas as pd
import math
#import torch
#from torch.utils.data import DataLoader
#from sklearn import preprocessing
from processing import *
#from neuralNetwork import *


def get_dataset(filename, size):
    """
    Creates training and test datasets from an Excel file with header
    Returns a dupla of pandas.DataFrame

    Arguments:
    - filename of the data source
    - size of training dataset from the total
    """
    data_df = pd.read_excel(filename, header=0)
    # removal of null values
    data_df = data_df[data_df.apply(
        lambda row: pd.notnull(row['moves']), axis=1)]
    total, _ = data_df.shape
    ds_size = math.ceil(total*size)
    training = data_df['moves'].values[:ds_size]
    test = data_df['moves'].values[ds_size+1:]
    return training, test


# def create_tensor(dataset):
#     """
#     Creates a tensor from dataset

#     Arguments:
#     - dataset: coded movements array
#     """
#     le = preprocessing.LabelEncoder()
#     targets = le.fit_transform(dataset)
#     targets = torch.as_tensor(targets)
#     return targets


def main():
    """
    Deep learning algorithm
    Returns a model capable of identifying the moves allowed for a given chess piece
    """
    TRAINING_SIZE = 2/3
    games, games_test = get_dataset("echec.xlsx", TRAINING_SIZE)
    training = list(games)
    test = list(games_test)

    training_parsed = []
    test_parsed = []

    for game in training:
        encoded = parse_movements(game.split(' '))
        training_parsed.append(encoded)

    for game in test:
        encoded = parse_movements(game.split(' '))
        test_parsed.append(encoded)

    # training_tensor = create_tensor(parced_training)
    # test_tensor = create_tensor(parced_test)

    # BATCH_SIZE = 64
    # train_dataloader = DataLoader(all_moves[:15000], batch_size=BATCH_SIZE)
    # test_dataloader = DataLoader(all_moves[15001:], batch_size=BATCH_SIZE)

    # DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    # print("Using {} device".format(DEVICE))
    # model = NeuralNetwork().to(device)

    # loss_fn = torch.nn.CrossEntropyLoss()
    # optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    # model.do_train(train_dataloader, loss_fn, optimizer)
    # model.do_test(test_dataloader, loss_fn)


if __name__ == "__main__":
    main()
