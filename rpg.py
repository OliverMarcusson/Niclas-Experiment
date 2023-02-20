import random
from time import sleep

def rprint(text, delay=0.03):
    for i in range(0, len(text)):
        print(text[i], end="", flush=True)
        sleep(delay)
    print()
    sleep(0.5)
    
def dialogue(speaker, text):
    for i in range(0, len(speaker)):
        print(speaker[i], end="", flush=True)
        sleep(0.025)
    print(": ", end="", flush=True)
    rprint(text)
    sleep(0.5)

def main():
    while True:
        score = 0
        rprint("You arrive at a road junction. There is a road to the left and a road to the right. Which road do you want to take?")
        answer = input(":")
        
        if answer == "left":
            score += 1
            rprint("You choose to take the left road... While pondering around, you find a coin on the ground. (+1 Score)")
        else:
            rprint("You choose to take the right road...")
        
        sleep(1)
        rprint("An eerie feeling spreads through your body...")
        sleep(1)
        rprint("Suddenly, a gang of roadmen ambush you!")
        dialogue("Roadman", "Oy man! Imma bosch your head in yea!")
        rprint("You can either run or fight these roadmen. What do you want to do?")
        answer = input(":")
        
        if answer == "run":
            score += 1
            rprint("You fear the roadmen and run away from them. While running, one of them throws a coin at the back of your head. (+1 Score)")
        else:
            rprint("You are not afraid of the roadmen, and you fight them. They bash your head in, yea.")
        sleep(1)
        
        rprint("After your encounter, you arrive at a small tavern on a tall, but narrow hill.")
        rprint("Inside, the headmistress, Elizabeth, greet you.")
        dialogue("Elizabeth", "Welcome dear traveler. What might bring you here at this late time? What room can I offer you?")
        rprint("You get to choose between a private room or the allroom. Which do you choose?")
        answer = input(":")
        
        if answer == "private":
            score += 1
            rprint("You accept a private room from Elizabeth. Under your pillow, you find a coin. (+1 Score)")
        else:
            rprint("You decide to stay in the allroom together with all the other travelers.")
        sleep(1)
        
        rprint("While grabbing some supper, you encounter another woman. Her name is Daisy, and she wants to spend dinner with you. Do you accept?")
        
        if answer == "yes":
            score += 1
            rprint("You eat dinner with Daisy. While sitting down in your chair, you notice that you've accidentally sat on a coin. (+1 Score)")
        else:
            rprint("You eat dinner alone. That Daisy girl weren't all that you'd hoped she'd be.")
        sleep(1)
        
        rprint("Suddenly, you encounter a witch!")
        dialogue("Witch", "*Evil laugh* I've cursed you with the most curseful of all curses! The only way to save yourself is to guess the number that I'm thinking of!")
        rprint("Your senses tell you that the number the witch is thinking of is in the range between one and three... Which number do you choose?")
        right_guess = random.randint(1, 10)
        answer = input(":")
        
        if int(answer) == right_guess:
            print(f"Wow right number yes! Score: {score}")
            break
        else:
            rprint("No right score. Do it again.")
        sleep(1)
    
if __name__ == "__main__":
    main()