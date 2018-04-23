# -*- coding: utf-8 -*-
#pyhon2.7
#Thu 12 Apr
#progrming nawaf almansour
# IPND Stage 2 Final Project
#Game has 3 or more levels and each level contains 4 or more blanks to fill in

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

import os
os.system("clear")
# IPND Stage 2 Final Project

# The list of correct answers
words_easy = ['fourth', 'Solar', 'Roman', 'Red']
words_medium = ['Asia', 'Mandeb', 'Valley', 'red']
words_hard = ['fourth', '16th', 'Ancon', '15']

number_options = ['___1___', '___2___', '___3___', '___4___']

Error_level = '''Invalid selection Please make sure to check (easy // medium // hard) : '''

welcome_message = '''
    Welcome to this game!
In this game you will be given a text minus some words
 and the requirement of guessing to test your public
 information and there are several levels you can choose from them
'''
questions = ["What is the right word for __1__? ",
             "What is the right word for __2__? ",
             "What is the right word for __3__? ",
             "What is the right word for __4__? ",]

level = ''' You have chosen the level '''

correct_text = '''
That's correct!
'''

Continuing_question = '''
Congratulations I have won this level
Would you like to continue to another level? (yes/no) '''

incorrect_text = ''' The input is incorrect Please try again '''


# The correct answers /fourth/  /Solar/  /Roman/  /Red/
easy_text = '''
Mars is the ___1___ planet from the Sun and the second-smallest
 planet in the ___2___ System after Mercury. In English, Mars
 carries a name of the ___3___ god of war, and is often referred
 to as the ___4___ Planet because the reddish iron oxide prevalent
 on its surface gives it a reddish appearance that is distinctive
 among the astronomical bodies visible to the naked eye.

'''
# The correct answers /Asia/ /Mandeb/ /Valley/ /red/
medium_text = '''
The Red Sea is a seawater inlet of the Indian Ocean, lying between
 Africa and ___1___. The connection to the ocean is in the south
 through the Bab el ___2___ strait and the Gulf of Aden. To the
 north lie the Sinai Peninsula, the Gulf of Aqaba, and the Gulf
 of Suez (leading to the Suez Canal). The Red Sea is a Global 200
 ecoregion. The sea is underlain by the Red Sea Rift which is
 part of the Great Rift ___3___. Red Sea The name of the sea may
 signify the seasonal blooms of the ___4___-coloured Trichodesmium
 erythraeum near the water's surface. A theory favored by some
 modern scholars is that the name red is referring to the direction
 south, just as the Black Sea's name may refer to north. The basis
 of this theory is that some Asiatic languages used color words
 to refer to the cardinal directions. Herodotus on one
occasion uses Red Sea and Southern Sea interchangeably.
'''
# The correct answers /fourth/  /16th/ /Ancon/  /15/
hard_text = '''
The potato is a starchy, tuberous crop from the perennial nightshade .
 Potatoes have become a staple food in many parts of the world and an
 integral part of much of the world's food supply. Potatoes are the
 world's ___1___-largest food crop, following maize (corn), wheat,
 and rice. In the Andes, where the species is indigenous, some other
 closely related species are cultivated. Potatoes were introduced to
 Europe in the second half of the ___2___ century by the Spanish. Wild
  potato species can be found throughout the Americas from the United
  States to southern Chile. The potato was first domesticated in the
   region of modern-day southern Peru and extreme northwestern Bolivia
    between 8000 and 5000 BC. It has since spread around the world
    and become a staple crop in many countries. The earliest
    archaeologically verified potato tuber remains have been found
     at the coastal site of ___3___ (central Peru), dating to 2500 BC.
      The most widely cultivated variety, Solanum tuberosum tuberosum,
      is indigenous to the Chiloé Archipelago, and has been cultivated
       by the local indigenous people since before the Spanish conquest.
        Potatoes are generally grown from seed potatoes, tubers
        specifically grown to be free from disease and to provide
        consistent and healthy plants. To be disease free, the areas
         where seed potatoes are grown are selected with care. In the US,
          this restricts production of seed potatoes to only ___4___ states
          out of all 50 states where potatoes are grown. These locations
           are selected for their cold, hard winters that kill pests and
           summers with long sunshine hours for optimum growth. In the UK,
            most seed potatoes originate in Scotland, in areas where westerly
            winds prevent aphid attack and thus prevent spread of potato virus
'''


def welcome():
    print welcome_message,
    print "--------------------------------------------------------"
    print " " * 10 + "easy" + " " * 7  + "medium" +  " " * 7 + "hard"
    print "--------------------------------------------------------"
    print
    user_input = raw_input("Please select a level: ")
    return levelSelection(user_input)

def levelSelection(user_input):
# Choose the level you want to start from the three levels by typing the same level name to allow the game to play and if what is written incorrectly the question is asked once again.
    print level + user_input + "!"
    if user_input == 'easy':
        print easy_text
        return levelGame(easy_text, words_easy)
    elif user_input == 'medium':
        print medium_text
        return levelGame(medium_text, words_medium)
    elif user_input == 'hard':
        print hard_text
        return levelGame(hard_text, words_hard)
    else:
        user_input = raw_input(Error_level)
        return levelSelection(user_input)


def continue_end():
# Check the user's wallet if they continue and go to the next level or exit the game
    user_input = raw_input(Continuing_question)
    if user_input == "yes":
    	welcome()
    if user_input == "no":
        return None

def levelGame(levelText, answers):
# Make sure that the user chooses the level correctly and if the input is not defined, the ask is returned. If a shout is made,  thane the user is asked to user the health answer from the text for the level .
    count = 0
    for word in levelText:
        user_input = raw_input(questions[count])
        if user_input == answers[count]:
            print correct_text
            levelText = levelText.replace(number_options[count], answers[count])
            print levelText
            count = count + 1
            if len(answers) == count:
            	continue_end()
        else:
        	while user_input != answers[count]:
        		print incorrect_text, '\n', levelText
        		break


welcome() # The start of the program.
