# This is the main executable for the prediction model
# making a change to test commit
# Imports
import datetime
import subprocess


def get_user_input():
    # Open a new command prompt window for user input, does not work on ios devices
    subprocess.call(["cmd", "/c", "start", "cmd"])

    # Prompt the user for input
    user_input = input("Enter the sport you want to predict (football/basketball): ")

    return user_input


def print_to_console(message):
    # Function to print to the console
    print(message)


def main():

    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%m-%d-%Y")
    print("Pulling all available matches for:", formatted_date)
    print("")

# prompt user for the action
# user provides sport as abbreviation CBB(College Basketball)
    sport_user_selection = input("Enter the sport you would like to receive prediction results for (CBB)?")
    print("")

# make decision
    if sport_user_selection == "CBB":
        from CBB_Prediction_Algo1 import predict_cbb
        predict_cbb()

    else:
        print("Invalid input!")

# print each game to console with recommendation
# store recommendation with a value to indicate if it was verified or not
# run a script to check outcomes of games
# print a W/L of previous results at the beginning of this script

# provide the user a command to add a new version for W/L standings of the script
# each version will show the model changes over time

# Executable (this runneth the codeth)


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
