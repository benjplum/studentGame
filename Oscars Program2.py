import random
#import the randomizer
counterScore = 0

class OscarGame: #creates the class


    def __init__(self, movie_titles, movie_winners): #defines a definition
        self.movie_titles = movie_titles #movie titles
        self.movie_winners = movie_winners #movie winners
        self.shuffled_titles = random.sample(movie_titles, len(movie_titles)) #creating a shuffled list of movie titles
        self.num_movies = len(movie_titles) #setting an instance variable named "num_movies" equal to the length of the list
        self.counter = 0 #increment the program by one
        self.counterNo = 0 #counts the wrong answers
        self.counterY = 0 #counts the right answers

        # Define lists of phrases for correct and incorrect answers
        self.correct_phrases = ["Good job!", "You got it right!", "Correct!", "Getting warmer"]
        self.incorrect_phrases = ["WOMP WOMP :-(", "Not it", "Incorrect", "That was wrong. Try again.", "Getting colder"]

        
    def play(self): #starts the game
        print("\n", "Welcome to the Oscars Game. This is a trivia game that asks you questions about which movies won an Oscar award.", "\n", "Try to guess if a movie won an Oscar or was just nominated. As you play the game you can enter Y for yes, N for", "\n", "no, or Q to quit. Press the Enter key to begin!")
        input()

        continue_game = True #initalize the continue game as true
        correct_streak = 0
        wrong_streak = 0

        while continue_game and self.counter < self.num_movies:
            title = self.shuffled_titles[self.counter]
            index = self.movie_titles.index(title)
            response = input("Did '{}' win an Oscar? ".format(title))

            if response.upper() == 'Q':
                if self.counter == 0:
                    print("You have chosen to quit the game.")
                    return
                else:
                    continue_game = False

            elif response.upper() == 'Y' and self.movie_winners[index] == 'Won':
                print("\n", random.choice(self.correct_phrases), "\n")
                self.counter += 1
                self.counterY += 1
                correct_streak += 1
                wrong_streak = 0
                if correct_streak >= 2:
                    print("You are on a roll!", "\n")

            elif response.upper() == 'N' and self.movie_winners[index] == 'Did not win':
                print("\n", random.choice(self.correct_phrases), "\n")
                self.counter += 1
                self.counterY += 1
                correct_streak += 1
                wrong_streak = 0
                if correct_streak >= 2:
                    print("You are on a roll!", "\n")

            elif response.upper() == 'N' and self.movie_winners[index] == 'Won':
                print("\n", random.choice(self.incorrect_phrases), "\n")
                self.counter += 1
                self.counterNo += 1
                wrong_streak += 1
                correct_streak = 0
                if wrong_streak >= 2:
                    print("(ノಠ益ಠ)ノ彡┻━┻", "\n")

            elif response.upper() == 'Y' and self.movie_winners[index] == 'Did not win':
                print("\n", random.choice(self.incorrect_phrases), "\n")
                self.counter += 1
                self.counterNo += 1
                wrong_streak += 1
                correct_streak = 0
                if wrong_streak >= 2:
                    print("(ノಠ益ಠ)ノ彡┻━┻", "\n")

            if self.counter == self.num_movies:
                continue_game = False

        counterTotal = self.counterY + self.counterNo   #add correct and incorrect votes
        counterScore = self.counterY / counterTotal ##get the average
        if counterScore == 1.0:
            print("You got every answer right!")
        elif counterScore == 0.0:
            print("You got everything wrong!")
        if counterScore != 0:            
            percentage = "{:.1%}".format(counterScore)  #format the percentage to one decimal place
            print("Your score is: {}".format(percentage)) #print the score
        else:
            print("Your score is 0.0%")

        return counterScore

# initalize all the movie names using a list
movie_titles = ["The Godfather: Part II (1974)", "Casablanca (1943)", "Lawrence of Arabia (1962)", "It's a Wonderful Life (1946)", "King Kong (1933)", "The Godfather (1972)", "It Happened One Night (1934)", "The French Connection (1971)", "Rebel Without a Cause (1955)", "Schindler's List (1993)", "Gone with the Wind (1939)", "One Flew Over the Cuckoo's Nest (1975)", "Marvin's Room (1996)", "Lord of the Rings: Return of the King (2003)", "Rocky (1976)", "The Hurt Locker (2009)", "No Country for Old Men (2007)", "The Shining (1980)", "Silence of the Lambs (1990)", "Memento (2000)", "Moonlight (2016)", "Unforgiven (1992)", "Drive (2011)", "Once Upon a Time in America (1984)", "Amadeus (1984)", "Don't Look Now (1973)", "The Apartment (1960)", "American Psycho (2000)", "Rear Window (1954)", "The Wolf of Wall Street (2013)", "Mean Streets (1973)", "Miller's Crossing (1990)", "The Good, the Bad, and the Ugly (1966)", "Leon: The Professional (1994)", "Halloween (1978)", "What's Eating Gilbert Grape (1993)", "West Side Story (1961)", "Psycho (1960)", "In the Mood for Love (2000)", "Stand by Me (1986)", "Midnight Cowboy (1969)", "Heat (1995)", "On The Waterfront (1954)", "Reservoir Dogs (1992)", "Punch-Drunk Love (2002)", "All About Eve (1952)", "The Shawshank Redemption (1994)", "Edward Scissorhands (1990)", "Tokyo Story (1953)", "The Bridge on the River Kwai (1957)", "Fight Club (1999)", "The Deer Hunter (1978)", "The Big Lebowski (1998)", "The Terminator (1984)", "Titanic (1997)"]

movie_winners = ["Won", "Won", "Won", "Did not win", "Did not win", "Won", "Won", "Won", "Did not win", "Won", "Won", "Won", "Did not win", "Won", "Won", "Won", "Won", "Did not win", "Won", "Did not win", "Won", "Won", "Did not win", "Did not win", "Won", "Did not win", "Won", "Did not win", "Did not win", "Did not win", "Did not win", "Did not win", "Did not win", "Did not win", "Did not win", "Did not win", "Won", "Did not win", "Did not win", "Did not win", "Won", "Did not win", "Won", "Did not win", "Did not win", "Won", "Did not win", "Did not win", "Did not win", "Won", "Did not win", "Won", "Did not win", "Did not win", "Won"]

# create an instance of OscarGame
game = OscarGame(movie_titles, movie_winners)

# play the game
game.play()

if counterScore == 1:
    print("\n", "Wow, a perfect score!!!")
elif counterScore >= .7 and counterScore < 1:
    print("\n", "That was a really good game you played.")
else:
    print()


