import random


def print_hashed_movie(guesses, random_movie):
    print_hashed = ''
    for r in random_movie:
        if r == ' ':
            print_hashed = print_hashed + ' '
        elif r.lower() in guesses:
            print_hashed = print_hashed + r
        else:
            print_hashed = print_hashed + '-'

    return print_hashed


def start_game(movie, guesses):
    while random_movie != print_hashed_movie(guesses, random_movie):
        new_letter = input('Enter a letter:')
        guesses = guesses + str(new_letter)
        print('guesses', guesses)
        print(print_hashed_movie(guesses, random_movie))


def header():
    print('===========================')
    print('     Welcome to HANGMAN    ')
    print('===========================')


# Hangman game
# guess movie/tv show list
# create a list of movies/shows
movie_list = ['Terminator','Jumanji','James Bond','Star Wars','A Beautiful Mind','Clueless','Mission Impossible','Breakfast at Tiffanys','Lawrence of Arabia','The God Father','The Hobbit','The Lord of the Rings','The Patriot','Lord of the Rings', 'Titanic', 'Saving Private Ryan', 'The Last Samurai', 'Beauty and the Beast', 'Gangs of New York', 'Bourne Ultimatum','The Frontier', 'Mr Sunshine', 'Marco Polo', 'Merlin', 'oh my Ghost', 'The Physician', 'Lovebird',
              'Gladiator', 'Braveheart']
# start the game 
guesses = ''
header()

#loop thru the movi list (never ends? you say)
while len(movie_list)>0:
    #print(movie_list)
    # randomly get one from the list
    random_movie = movie_list[random.randint(1, len(movie_list) - 1)]
    #print (random_movie)
    #remove this movie from the list
    movie_list.remove(random_movie)
    #print(movie_list)

    print(' Guess this movie/show:    ')
    # printing the hashed movie name
    print(print_hashed_movie(guesses, random_movie))

    # looping thru asking the player to 
    # enter a letter
    start_game(random_movie, guesses)

    # player have guessed message
    print('You got it!')

