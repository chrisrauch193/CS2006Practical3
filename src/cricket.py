"""Module to read in IPL match data."""

import pandas as pd
import numpy as np
import os
import csv


def get_data(cricket_path):
    """Return pandas DataFrame containing IPL data."""

    # Initialise variables to be used.
    filelist = os.listdir(cricket_path)
    frame = pd.DataFrame()
    venue = 0
    match_num = 0;
    winner = ''
    team1 = ''
    team2 = ''

    # Loop through each file.
    for cricket_file in filter(lambda file: '.csv' in file, filelist):

        full_path = cricket_path + '/' + cricket_file

        # Read .csv data into a 2D list.
        with open(full_path, "r") as f:
            csv_file = csv.reader(f)
            csv_data = list(csv_file)

        # Access cells and retrieve information from specified cells.
        match_num = csv_data[7][2]
        venue = csv_data[8][2]
        winner = csv_data[18][2]
        team1 = csv_data[1][2]
        team2 = csv_data[2][2]

        # Use pandas functionality to read remainder of file.
        df = pd.read_csv(full_path, skiprows=20, names=["Type", "Innings", "Ball No.", "Batting Team",
            "Striker", "Non - Striker", "Bowler", "Runs","Extras", "How Out", "Batsman Out"])
        df.insert(0, 'Match Number', match_num)
        df.insert(1, 'Winner', winner)
        df.insert(2, 'Venue', venue)
        del df['Type']
        df.insert(4, 'Bowling Team', team1)
        df.loc[df['Batting Team'] == team1, 'Bowling Team'] = team2

        # Add the frame read to the bottom of the current DataFrame.
        frame = pd.concat([frame, df], ignore_index=True)

    # Clean up uninformative values.
    frame = frame.replace(np.nan, '-', regex=True)
    frame = frame.sort_values(['Match Number', 'Innings', 'Ball No.'], ascending=[1, 1, 1])
    frame = frame[frame["Ball No."] != 'D/L']
    frame['Runs'] = frame['Runs'].astype(int)
    frame['Ball No.'] = frame['Ball No.'].astype(float)
    frame['Extras'] = frame['Extras'].astype(int)
    frame['Innings'] = frame['Innings'].astype(int)
    frame['Match Number'] = frame['Match Number'].astype(int)

    return frame
