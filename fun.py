import random

nba_players = ["LeBron James", "Kevin Durant", "Stephen Curry", "Kawhi Leonard", "Giannis Antetokounmpo"]


selected_player = random.choice(nba_players)

while True:
    
    guess = input("Guess the NBA player: ")

    
    if guess == selected_player:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Sorry, that's not correct. Try again.")
