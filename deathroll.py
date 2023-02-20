from time import sleep
from random import randint
from os import system

def game(players, current_player, die_size):
    while True:
        _ = input(f"{current_player}, press ENTER to roll down.")
        roll = randint(1, die_size)
        sleep(1)
        if roll == 1:
            print(f"{current_player}, you rolled a {roll}. The game ends for you.")
            
            # Returns winner
            if players["p1"] == current_player:
                return players["p2"]
            else:
                return players["p1"]
        else:
            print(f"{current_player}, you rolled a {roll}. The game continues!")
            print()
            
            # Chooses next player
            if players["p1"] == current_player:
                current_player = players["p2"]
            else:
                current_player = players["p1"]
            sleep(1)
            
def main():
    players = {
        "p1": "",
        "p2": ""
    }
    
    if players["p1"] == "":
        player_names = input("Please input player names, separated by comma: ")
        player_names = player_names.split(", ")
        players["p1"] = player_names[0]
        players["p2"] = player_names[1]
    
    while True:
        print(f"""Who is going to start?
p1: {players['p1']}
p2: {players['p2']}""")
        
        current_player = input(":")
        current_player = players[current_player]
    
        die_size = int(input(f"{current_player}, please input your desired die size: "))
        print(f"Die size: {die_size} sides.")
        sleep(1)
        print("Let the games begin...")
        sleep(2)
        system("cls")
        
        winner = game(players, current_player, die_size)
        print(f"{winner} wins the deathroll!")
        play_again = input("Do you want to play again? (Y/N): ")
        system("cls")
        if play_again == "N":
            print("Thank you for playing Deathroll!")
            break
    
if __name__ == "__main__":
    main()