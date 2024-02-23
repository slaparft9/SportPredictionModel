# This file will pull college basketball game data and make a prediction of the result of each game for the user
# Todo: Do I need to pass date into the file or run that outside of the file?

# imports
import json
from espn_api import ESPNAPI


# handle separate console for inputs/outputs
def print_to_console(message):
    print(message)


def predict_cbb():
    print_to_console("Predicting your betting future for mens college basketball")


# Pull Data for the sport selected by performing CBB API calls for today's games
# Todo: How do i identify matches across sources of data?
    api_call = ESPNAPI("https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?date=20240222&limit=357")
    #todo: find out why the data here is not in the correct format
    todays_match_data_raw = api_call.get_data()
    todays_match_data = json.loads(todays_match_data_raw)
    if todays_match_data_raw:
        print_to_console(todays_match_data_raw)
        print_to_console(todays_match_data)
    else:
        print_to_console("Failed to fetch basketball data")
# GET these attributes (Date, Time, Home Team, Away Team, Fav/Dog, Spread, ESPN Power Ranking)


# use json.loads to import data. access nested data with parsed_data['person']['name']

# Run Algo, inside the function that is pulling each games data
# Algo 1 - Power Ranking Difference + Home field advantage. Home Field advantage = 3 points
