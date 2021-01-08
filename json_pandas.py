import numpy as np
import pandas as pd
import os
import json

class JsonPandas () :
    
    def import_FIFA():
        """
        Import FIFA data from FIFA09 -> FIFA21

        Imports all the data into a list of pandas dataframes. Secondary stats are only available on the FIFA21 dataset.

        @params: none
        @return: a list of dataframes, oredered from 2009 to 2021.

        """

        current_directory = os.path.dirname(os.path.abspath(__file__))
        fifa_versions = ['FIFA09', 'FIFA10', 'FIFA11', 'FIFA12', 'FIFA13', 'FIFA14', 'FIFA15', 'FIFA16', 'FIFA17', 'FIFA18', 'FIFA19', 'FIFA20', 'FIFA21']
        pandas_dataframes = []

        for version in fifa_versions:
            player_file = os.path.join(current_directory, '{}/players_stats.json'.format(version))
            pandas_dataframes.append(pd.read_json(player_file, orient='records'))

        return pandas_dataframes

    def create_team_dict():
        """
        Creates a list of dictionaries with the seasons and the teams that have played during that season.

        @params: none
        @return: a list containing two dictionaries. key: season, value: teams
        """
        seasons_list_one = ['08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '08_09', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '09_10', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '10_11', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '11_12', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '12_13', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '13_14', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '14_15', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '15_16', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17', '16_17']
        teams_list_one = ['Arsenal', 'Aston Villa', 'Blackburn Rovers', 'Bolton Wanderers', 'Chelsea', 'Everton', 'Fulham', 'Hull City', 'Liverpool', 'Manchester City', 'Manchester United', 'Middlesbrough', 'Newcastle United', 'Portsmouth', 'Stoke City', 'Sunderland', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Wigan Athletic', 'Arsenal', 'Aston Villa', 'Birmingham City', 'Blackburn Rovers', 'Bolton Wanderers', 'Burnley', 'Chelsea', 'Everton', 'Fulham', 'Hull City', 'Liverpool', 'Manchester City', 'Manchester United', 'Portsmouth', 'Stoke City', 'Sunderland', 'Tottenham Hotspur', 'West Ham United', 'Wigan Athletic', 'Wolverhampton Wanderers', 'Arsenal', 'Aston Villa', 'Birmingham City', 'Blackburn Rovers', 'Blackpool', 'Bolton Wanderers', 'Chelsea', 'Everton', 'Fulham', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Stoke City', 'Sunderland', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Wigan Athletic', 'Wolverhampton Wanderers', 'Arsenal', 'Aston Villa', 'Blackburn Rovers', 'Bolton Wanderers', 'Chelsea', 'Everton', 'Fulham', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Queens Park Rangers', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'West Bromwich Albion', 'Wigan Athletic', 'Wolverhampton Wanderers', 'Arsenal', 'Aston Villa', 'Chelsea', 'Everton', 'Fulham', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Queens Park Rangers', 'Reading', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Wigan Athletic', 'Arsenal', 'Aston Villa', 'Cardiff City', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Hull City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Arsenal', 'Aston Villa', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Hull City', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Queens Park Rangers', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Arsenal', 'Aston Villa', 'Bournemouth', 'Chelsea', 'Crystal Palace', 'Everton', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United', 'Arsenal', 'Bournemouth', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Hull City', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Middlesbrough', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United']
        seasons_list_two = ['17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '17_18', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '18_19', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '19_20', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21', '20_21']
        teams_list_two = ['Arsenal', 'Bournemouth', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield Town', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Southampton', 'Stoke City', 'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United', 'Arsenal', 'Bournemouth', 'Brighton & Hove Albion', 'Burnley', 'Cardiff City', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers', 'Arsenal', 'Aston Villa', 'Bournemouth', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers', 'Arsenal', 'Aston Villa', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Wolverhampton Wanderers']
        final_dict_one = {}
        final_dict_two = {}
        for i in range(len(seasons_list_one)):
            if seasons_list_one[i] in final_dict_one:
                final_dict_one[seasons_list_one[i]].append(teams_list_one[i])
            else:
                final_dict_one[seasons_list_one[i]] = [teams_list_one[i]]
        
        for i in range(len(seasons_list_two)):
            if seasons_list_two[i] in final_dict_two:
                final_dict_two[seasons_list_two[i]].append(teams_list_two[i])
            else:
                final_dict_two[seasons_list_two[i]] = [teams_list_two[i]]
        return [final_dict_one, final_dict_two]

    def create_average_dicts():
        """
        Creates dictionaries containing the average rating for each team in a season.

        @params: none
        @return: a touple of dicts. key: season, val: a dict with key: team, val: average rating
        """
        fifa_dataframes = JsonPandas.import_FIFA()
        seasons_teams = JsonPandas.create_team_dict()
        seasons_one = ['08_09', '09_10', '10_11', '11_12', '12_13', '13_14', '14_15', '15_16', '16_17']
        seasons_two = ['17_18', '18_19', '19_20', '20_21']
        averages_seasons_one = {}
        averages_seasons_two = {}
        for i in range(len(seasons_one)):
            fifa_values = fifa_dataframes[i]
            teams_in_season = seasons_teams[0][seasons_one[i]]
            average_teams = JsonPandas.find_average(fifa_values, teams_in_season)
            averages_seasons_one[seasons_one[i]] = average_teams
        offset = len(seasons_one) - 1
        for i in range(len(seasons_two)):
            fifa_values = fifa_dataframes[offset + i]
            teams_in_season = seasons_teams[1][seasons_two[i]]
            average_teams = JsonPandas.find_average(fifa_values, teams_in_season)
            averages_seasons_two[seasons_two[i]] = average_teams
        return (averages_seasons_one, averages_seasons_two)


    def find_average(fifa_dataframe, teams_in_season):
        """
        Finds the average rating for all teams in a season.

        @params: fifa_dataframe: the FIFA data for that season, teams_in_season: the teams that have played that season
        @return: a dict with key: team, val: average rating
        """
        averages = {}
        for team in teams_in_season:
            filtered_dataset = fifa_dataframe[fifa_dataframe["Team"] == team]
            primary_stats = filtered_dataset["Primary Stats"].to_list()
            overall_ratings = []
            for stat in primary_stats:
                overall_ratings.append(stat["Overall Rating"])
            averages[team] = np.round_(np.mean(np.array(overall_ratings).astype(np.int)), decimals=2)
        return averages

    def return_averages_in_pd():
        """
        Returns the averages as pandas dataframes. Converts the names of the teams to align the data to the naming scheme.

        @params: none
        @return: a touple of pandas dataframes.
        """
        averages_seasons_one, averages_seasons_two = JsonPandas.create_average_dicts()
        avg_seasons_one_pd = pd.DataFrame.from_dict(averages_seasons_one)
        avg_seasons_two_pd = pd.DataFrame.from_dict(averages_seasons_two)
        new_team_names_one = ['Birmingham', 'Blackburn', 'Bolton', 'Cardiff', 'Hull', 'Leicester', 'Man City', 'Man United', 'Newcastle', 'Norwich', 'QPR', 'Stoke', 'Swansea','Tottenham', 'West Brom', 'West Ham', 'Wigan', 'Wolves']
        curr_team_names_one = ['Birmingham City','Blackburn Rovers','Bolton Wanderers','Cardiff City','Hull City','Leicester City','Manchester City','Manchester United','Newcastle United','Norwich City','Queens Park Rangers','Stoke City','Swansea City','Tottenham Hotspur','West Bromwich Albion','West Ham United','Wigan Athletic','Wolverhampton Wanderers']
        index_one_as_list = avg_seasons_one_pd.index.tolist()
        for i in range(len(curr_team_names_one)):
            idx = index_one_as_list.index(curr_team_names_one[i])
            index_one_as_list[idx] = new_team_names_one[i]
        avg_seasons_one_pd.index = index_one_as_list
        new_team_names_two =  ['Brighton', 'Cardiff', 'Huddersfield', 'Leeds', 'Leicester', 'Man City', 'Man United', 'Newcastle', 'Norwich','Stoke', 'Swansea','Tottenham', 'West Brom', 'West Ham', 'Wolves']
        curr_team_names_two = ['Brighton & Hove Albion','Cardiff City','Huddersfield Town','Leeds United','Leicester City','Manchester City','Manchester United','Newcastle United','Norwich City','Stoke City','Swansea City','Tottenham Hotspur','West Bromwich Albion','West Ham United','Wolverhampton Wanderers']
        index_two_as_list = avg_seasons_two_pd.index.tolist()
        for i in range(len(curr_team_names_two)):
            idx = index_two_as_list.index(curr_team_names_two[i])
            index_two_as_list[idx] = new_team_names_two[i]
        avg_seasons_two_pd.index = index_two_as_list
        return (avg_seasons_one_pd, avg_seasons_two_pd)
        
    def export_to_csv():
        """
        Exports the dataframes to CSV.
        """
        avg_seasons_one_pd, avg_seasons_two_pd = JsonPandas.return_averages_in_pd()
        avg_seasons_one_pd.to_csv("avg_seasons_one.csv", encoding="utf-8", index=True)
        avg_seasons_two_pd.to_csv("avg_seasons_two.csv", encoding="utf-8", index=True)






