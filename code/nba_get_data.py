import requests
import time
import pandas as pd
import sys 
from os import path
from nba_api.stats import endpoints

def get_game_id():
    
    # Here we access the leaguegamefinder module through endpoints & assign the class to "data"
    data = endpoints.leaguegamefinder.LeagueGameFinder() 

    # Our "data" variable now has built in functions such as creating a dataframe for our data
    df_game_finder = data.league_game_finder_results.get_data_frame()

    #save game ids to a list
    game_id_list = [i for i in df_game_finder['GAME_ID'][df_game_finder['GAME_ID'].str.startswith('0022')]]
    return game_id_list


def get_player_tracking():
    df_player_tracking = pd.DataFrame()
    game_id_list = get_game_id()

    for j, i in enumerate(game_id_list):
        # Here we access the box score player track module through endpoints & assign the class to "data"
        data = endpoints.boxscoreplayertrackv2.BoxScorePlayerTrackV2(i) 

        # Our "data" variable now has built in functions such as creating a dataframe for our data
        df_tracking_game = data.player_stats.get_data_frame()
        print(f'Tracking data from game {j+1} of {len(game_id_list)}')
        df_player_tracking = pd.concat([df_player_tracking, df_tracking_game])
        time.sleep(1.5)

    
    return df_player_tracking

def get_play_by_play():
    df_play_by_play = pd.DataFrame()
    game_id_list = get_game_id()

    for j, i in enumerate(game_id_list):
        # Here we access the box score player track module through endpoints & assign the class to "data"
        data = endpoints.playbyplayv2.PlayByPlayV2(i) 

        # Our "data" variable now has built in functions such as creating a dataframe for our data
        df_play_by_game = data.play_by_play.get_data_frame()
        print(f'Play by play from game {j+1} of {len(game_id_list)}')
        df_play_by_play = pd.concat([df_play_by_play, df_play_by_game])
        time.sleep(1.5)

    return df_play_by_play


def main():
    ''' Will check to see if the file exists before fetching data from NBA API'''
    
    if path.exists('../data/play_by_play.csv'):
        print('Play by play already exists')
        pass
    else:
        df_play_by_play = get_play_by_play()
        df_play_by_play.to_csv('../data/play_by_play.csv', index=False)

    if path.exists('../data/player_tracking.csv'):
        print('Player tracking already exists')
        pass
    else:        
        df_player_tracking = get_player_tracking()
        df_player_tracking.to_csv('../data/player_tracking.csv', index=False)

if __name__ == "__main__":
    main()