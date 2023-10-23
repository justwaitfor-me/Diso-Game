import json
from modules import *
from game import main

# DEF
def start(name):
    with open('courrent.json', 'r') as f:
        data = json.load(f)
    data = {"playing":False, "game":None, "name":None} 
    with open('courrent.json', 'w') as f:
        json.dump(data, f)
    refresh(name="Menue")

    out = menue(["Load Game", "New Game", "Options"], "Select an Option:")
    refresh(name=out)

    #return the return bool from selection()
    return selection(out, name)
    
def selection(arg, username):
    if arg == "Load Game":
        # getting json
        with open('games.json', 'r') as games:
            games_saved = json.load(games)
        games = []
        for i in games_saved:
            games.append(i)
        game = menue(games, "Select a saved Game:")
        refresh(name=f"load {game}?")
        out = menue(['yes', 'no'], f"Do you really want to load the game {game}?")
        if out == 'yes':
            refresh(name="Loading Game")
            load(["Loading Game"], end="load was successful", duration=0.2)
            with open('courrent.json', 'r') as f:
                data = json.load(f)
            data = {"playing":True, "game":game, "name":username} 
            with open('courrent.json', 'w') as f:
                json.dump(data, f)
            return True
            #TODO: DateTime update
        else:
            return False
        
    elif arg == "New Game":
        isok = None
        while not isok in ["yes", "y", "j"]:
            refresh(name = "New Game")
            print("Create New Game\n")
            Name = input("Enter Name:\n> ").lower()
            refresh(name="New Game", arg=f"Name: {Name}\n")
            GameMode = None
            while not GameMode in ["hard", "medium", "easy"]:
                GameMode = input("Enter Game Mode: (Hard, Medium, Easy)\n> ").lower()
                refresh(name="New Game", arg=f"Name: {Name}\n\nPlease Enter an valid Game Mode!")
            refresh(name="New Game", arg=f"Name: {Name}\nGame Mode: {GameMode}\n")
            isok = input("Save? (yes, no)\n> ").lower()
        with open('games.json', 'r') as f:
            data = json.load(f)
        data[Name] = {"gamemode":GameMode, "datetime":{"date":"#einfügen", "time":"#einfügen"}, "score":0} #TODO: datetime
        with open('games.json', 'w') as f:
            json.dump(data, f)
        return False
        
    elif arg == "Options": 
        #TODO: Options
        ...
        
    
# MAIN
refresh(arg="Welcome to this little Game <3\n")
#load(['booting up', 'reading data', 'codeing an new user', 'starting game.py'])

username = str(input("Enter your Name: ")) #waiting...

while start(username) == False:
    pass

main()
