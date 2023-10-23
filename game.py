import json
from termcolor import colored
from modules import *

def main():
    #JSON DATA
    with open('games.json', 'r') as f:
        game_data = json.load(f)
    with open('courrent.json', 'r') as f:
        courrent_data = json.load(f)
        cou_playing = courrent_data["playing"]
        cou_game = courrent_data["game"]
        cou_name = courrent_data["name"]
    
    
    check = False
    if cou_playing == True:
        for name in game_data:
            if name == cou_game:
                game_data = game_data[name]
                play(cou_name, cou_game, game_data)
                check = True
                break
    
    if check == False:
        refresh(name="Error", arg=colored("We run into an Error :(\n", "red"), duration=0.5)
        input("Press Enter to go back")
        back()
    
def play(user, game, game_data):
    print(f"User_Name: {user}\nGame: {game}\n\n{game_data}") #Testing
    while True:
        2
    
def back():
    from main import start
    start("Player1")
    
# back to main.py
back()