from termcolor import colored
import os, sys, time

def refresh(arg = "", name="Disco Game", duration=0):
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
    sys.stdout.write(f"\x1b]2;{name}\x07")
    print(arg)
    time.sleep(duration)
    
def menue(options, titel):
    while True:
        print(titel)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = input("> ")
        if choice.isdigit() and int(choice) in range(1, len(options)+1):
            choice_index = int(choice) - 1
            return options[choice_index]
        else:
            refresh(arg="Invalid input. Please choose one of the available options.")
            
def load(list, end="successful", duration=0.1):
    for boot in list:
        for i in range(1, 21):
            msg = f"{boot}: " + colored(f"{'#' * i} {str(i*5)}%", "green")
            print(msg, end='\r')
            time.sleep(duration)
        print(colored(f"{msg} ~{end}", "blue"))