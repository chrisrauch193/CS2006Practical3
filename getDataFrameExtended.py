import pandas as pd
import numpy as np
import os
import csv

def getData():
    path = './TestingFiles/'
    filelist = os.listdir(path)
    frame = pd.DataFrame()
    venue = 0
    matchno = 0;
    winner = ''
    team1 = ''
    team2 = ''
    for file in filter(lambda file: '.csv' in file, filelist):
        with open(path + file, "r") as f:
            csvObj = csv.reader(f)
            csvObj = list(csvObj)
            matchno = csvObj[7][2]
            venue = csvObj[8][2]
            winner = csvObj[18][2]
            team1 = csvObj[1][2]
            team2 = csvObj[2][2]
        df = pd.read_csv(path + file, skiprows=20,names=["Type", "Innings", "Ball No.", "Batting Team", "Striker", "Non - Striker", "Bowler", "Runs","Extras", "How Out", "Batsman Out"])
        df.insert(0, 'Match Number', matchno)
        df.insert(1, 'Winner', winner)
        df.insert(2, 'Venue', venue)
        del df['Type']
        df.insert(4, 'Bowling Team', team1)
        df.loc[df['Batting Team'] == team1, 'Bowling Team'] = team2
        frame = pd.concat([frame, df], ignore_index=True)

    frame = frame.replace(np.nan, '-', regex=True)
    frame = frame.sort_values(['Match Number', 'Innings', 'Ball No.'], ascending=[1, 1, 1])
    frame = frame[frame["Ball No."] != 'D/L']
    frame['Runs'] = frame['Runs'].astype(int)
    frame['Ball No.'] = frame['Ball No.'].astype(float)
    frame['Extras'] = frame['Extras'].astype(int)
    frame['Innings'] = frame['Innings'].astype(int)
    frame['Match Number'] = frame['Match Number'].astype(int)
    return frame
