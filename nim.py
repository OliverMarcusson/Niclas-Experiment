from os import system

def print_piles(piles: list):
    pile_iter = 1
    for i in piles:
        print(f"{pile_iter}. ", end="", flush=True)
        for j in range(i):
            print("| ", end="", flush=True)
        print()
        pile_iter += 1
    print()

def main():
    piles_amount = int(input("Antal högar: "))
    piles = list()
    for i in range(piles_amount):
        piles.append(int(input(f"Antal stickor i hög {i + 1}: ")))
    
    player = 2
    while True:
        # Changes player every turn
        if player == 2:
            player = 1
        else:
            player = 2
    
        print_piles(piles)
        while True:
            pile_to_draw = int(input(f"Player {player}, which pile do you want to draw from: ")) - 1
            amount_to_draw = int(input(f"Player {player}, how many sticks do you want to draw [1-3]: "))
            
            # Checks if there is enough sticks in the piles
            if not piles[pile_to_draw] < amount_to_draw:
                piles[pile_to_draw] -= amount_to_draw
                
                # Removes pile if it's empty
                if piles[pile_to_draw] == 0:
                    piles.pop(pile_to_draw)
                break
            else:
                print("There is not enogh sticks to draw in this pile!")
        
        # Checks if there's only one pile left and if it only has a single stick in it    
        if len(piles) == 1 and piles[0] == 1:
            print(f"Player {player} wins!")
            break 
        system("cls")
    

if __name__ == "__main__":
    main()