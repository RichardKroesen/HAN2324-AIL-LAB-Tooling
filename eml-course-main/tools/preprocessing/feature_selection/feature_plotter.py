"""
feature_plotter.py

Feature plotting functions.

Authors:    Jeroen Veen
            Hugo Arends
Date:       October 2023

Copyright:  2023 HAN University of Applied Sciences. All Rights Reserved.
"""
import sys
from os.path import join, dirname, realpath
sys.path.append(join(dirname(realpath(__file__)), '..', '..'))

from custom_bunch import CustomBunch
import config as cfg
from glob import glob
import matplotlib.pyplot as plt

def plot_single(filename=''):
    """
    Load a single bunch from a CSV file and plot it.
    """

    if filename == '':
        filenames = glob(join(cfg.PREPROCESSING_FEATURES_DIR_PATH, '*.csv'))
        assert len(filenames) != 0, 'No CSV files'

        # Get first CSV file from the folder
        filename = filenames[0]
    else:
        filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, filename)

    print(filename)
    bunch = CustomBunch.load_csv(filename)
    bunch.plot()
    plt.show()


def plot_all():
    """
    Load several bunches from all CSV files in a folder. Add all these bunches
    into a new bunch and plot this new bunch.
    """
    filenames = glob(join(cfg.PREPROCESSING_FEATURES_DIR_PATH, '*.csv'))
    assert(len(filenames) != 0), 'No CSV files'

    # Add all bunches into one new bunch
    bunch = CustomBunch.load_csv(filenames[0])
    for filename in filenames[1:]:
        bunch = bunch + CustomBunch.load_csv(filename)
    
    # Give the new bunch a more meaningful name
    bunch.name = 'all_features'

    # Plot and save the bunch features
    bunch.plot()
    filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, bunch.name+'_time_series_data.png')
    plt.savefig(filename, dpi=300)

    bunch.plot_label_distribution()
    filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, bunch.name+'_label_distribution.png')
    plt.savefig(filename, dpi=300)

    bunch.plot_pairs()
    filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, bunch.name+'_pairs.png')
    plt.savefig(filename, dpi=300)

    bunch.plot_correlation_heatmap()
    filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, bunch.name+'_correlation_heatmap.png')
    plt.savefig(filename, dpi=300)

    bunch.plot_boxplots()
    filename = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, bunch.name+'_boxplots.png')
    plt.savefig(filename, dpi=300)

    print('Files written:')
    print(filename)

    if __name__ == "__main__":
        plt.show()


if __name__ == "__main__":
    #  plot_single('19524-testCPR-stationary.csv')
    plot_all()
