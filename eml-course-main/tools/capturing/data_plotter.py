"""
data_plotter.py

Data plotting functions.

Authors:    Jeroen Veen
            Hugo Arends
Date:       October 2023

Copyright:  2023 HAN University of Applied Sciences. All Rights Reserved.
"""
import sys
from os.path import join, dirname, realpath
sys.path.append(join(dirname(realpath(__file__)), '..'))

from custom_bunch import CustomBunch
import config as cfg
from glob import glob
import matplotlib.pyplot as plt
from os.path import join

def plot_single(filename=''):
    """
    Load a single bunch from a CSV file and plot it.
    """

    if filename == '':
        filenames = glob(join(cfg.CAPTURED_DIR_PATH, '*.csv'))
        assert len(filenames) != 0, 'No CSV files'

        # Get first CSV file from the folder
        filename = filenames[0]
    else:
        filename = join(cfg.CAPTURED_DIR_PATH, filename)

    print(filename)
    bunch = CustomBunch.load_csv(filename)
    bunch.plot()
    plt.show()


def plot_all():
    """
    Load several bunches from all CSV files in a folder. Add all these bunches
    into a new bunch and plot this new bunch.
    """
    filenames = glob(join(cfg.CAPTURED_DIR_PATH, '*.csv'))
    assert(len(filenames) != 0), 'No CSV files'

    # Add all bunches into one new bunch
    bunch = CustomBunch.load_csv(filenames[0])
    for filename in filenames[1:]:
        bunch = bunch + CustomBunch.load_csv(filename)
    
    # Give the new bunch a more meaningful name
    bunch.name = 'all_raw'

    # Plot the bunch
    bunch.plot()

    # Save plot
    filename = join(cfg.CAPTURED_DIR_PATH, bunch.name+'_time_series_data.png')
    plt.savefig(filename, dpi=300)

    print('Files written:')
    print(filename)

    if __name__ == "__main__":
        plt.show()

def plot_singleCPR(filename=''):
    """
    Load a single bunch from a CSV file and plot it.
    """

    if filename == '':
        filenames = glob(join(cfg.CAPTURED_DIR_PATH, '*.csv'))
        assert len(filenames) != 0, 'No CSV files'

        # Get first CSV file from the folder
        filename = filenames[0]
    else:
        filename = join(cfg.CAPTURED_DIR_PATH, filename)

    print(filename)
    bunch = CustomBunch.load_csv(filename)
    
    df = bunch.to_dataframe()

    # Plot 1
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    
    for attr in bunch.attributes:
        if attr.startswith('FP'):
            plt.plot(df.index, df[attr], linestyle='-', label=attr)

    plt.title('Finger Placement Indexes')
    plt.ylabel('FP Values')
    plt.legend()
    plt.tight_layout()
    plt.grid(True)

    # Plot 2 ToF
    plt.subplot(2, 1, 2)
    # plt.stem(df.index, df['ToF'], markerfmt=None, linefmt='darkblue')
    plt.plot(df.index, df['ToF'], color='darkblue')
    plt.title('ToF Over Intervals')
    plt.ylabel('ToF Value')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # # plot_single('14524-testCPR.csv')
    # plot_all()
    plot_singleCPR('14524-testCPR.csv')