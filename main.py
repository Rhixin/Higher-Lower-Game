import art
import game_data
import random 
import os

def get_random_data(game_data):
    random_num = random.randint(1, len(game_data)-1)
    
    #return a dictionary
    return game_data[random_num]

def check_greater(compare_two_holder):
    followers_1 = compare_two_holder[0]['follower_count']
    followers_2 = compare_two_holder[1]['follower_count']
    
    if followers_1 > followers_2:
        return "A"
    
    return "B"

def next_contestants():
    global compare_two_holder
    global game_data
    
    compare_two_holder.pop(0)
    
    next_person = get_random_data(game_data)
    
    compare_two_holder.append(next_person) 
    
def play_game():
    print(art.logo)
    compare_two_holder = []
    score = 0
    game_end = False

    for i in range(0,2):
            compare_two_holder.append(get_random_data(game_data.data))

    while game_end == False:
        
        print(f"Compare A: {compare_two_holder[0]['name']}, a {compare_two_holder[0]['description']}, from {compare_two_holder[0]['country']}")
        print(art.vs)
        print(f"Against B: {compare_two_holder[1]['name']}, a {compare_two_holder[1]['description']}, from {compare_two_holder[1]['country']}")

        answer_key = check_greater(compare_two_holder)
        player_answer = input("Who has more followers in Instagram 'A' or 'B'? ")

        if answer_key == player_answer:
            score += 1
            print("Current Score:", score)
            compare_two_holder.pop(0)
            compare_two_holder.append(get_random_data(game_data.data))
        else:
            game_end = True
            os.system('cls||clear')
            print("Game Over! Final Score:", score)
            
while( input("Do you want to Play Higher or Lower Game? y/n \n") == "y"):
    os.system('cls || clear')
    play_game()