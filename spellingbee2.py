# spelling bee
# Concept based on MIT 6.0001 hangman.py problem set
import string
WORDLIST_FILENAME = "words_alpha.txt"
# WORDLIST_FILENAME = "The_Oxford_3000.txt" #Smaller set of words
non_game_letters = []
new_wordlist = []
allSeven = []


def load_words():
	# code attribute: The loading of the word file is based on MIT 6.0001 ps2 hangman.py
	# The list comprehensions were made into one liners by chatGPT
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = inFile.readlines()
    wordlist = [item[:-1] for item in wordlist] # removes '\n' escape character
    wordlist = [' '.join(item.split()) for item in wordlist] # removes any spaces
    wordlist = [item for item in wordlist if len(item) >= 5] # removes words less than 5 char long
    print("  ", len(wordlist), "words loaded.")
  #   print(wordlist)
    input("continue...")
    return wordlist

wordlist = load_words()

###########################################################

def all_game_letters(others):
	"""
    0. Defines the unused 19 letters from the alphabet
    """
	game_letters = others
	
	print(f"{game_letters} are the letters in this game")
	for char in string.ascii_lowercase:
		if char in game_letters:
			pass
		else:
			non_game_letters.append(char)
	print(f"{non_game_letters} are not in use and will be deleted from the dictionary.")
	return non_game_letters		


def spellingbee_mainLetter(mainLetter):
	for item in wordlist:
		if mainLetter in item:
			new_wordlist.append(item)
	print("  ", len(new_wordlist), "words remaining that all have the letter", mainLetter)
	return new_wordlist


def spellingbee_cutLetter(nonLetter):
	new_wordlist = [item for item in new_wordlist if nonLetter not in item]
# 	for item in new_wordlist:
# 		if nonLetter in item:
# 			new_wordlist.remove(item)
	print("  ", len(new_wordlist), "words remaining after cutting", nonLetter)
	print(new_wordlist)
	return new_wordlist

def nonLetterLoop(nonChar, new2wordlist):
	non_Letter = ''.join(nonChar)
	print(non_Letter)
	for char in non_Letter:
		new2wordlist = [item for item in new2wordlist if char not in item]
		print(len(new2wordlist), char)
	# 	print(new2wordlist)
	return new2wordlist

# def spellingbee_other_letters(nonCharacters):
# 	for char in nonCharacters:
# 		for item in new_wordlist:
# 			if char in item:
# 				new_wordlist.remove(item)
# 			else:
# 				pass
# 	print("  ", len(new_wordlist), "words with only game letters.")
# 	return new_wordlist

# def allSeven(game_letters):
# 	for item in new_wordlist:
# 		if char in item:
# 			if game_letters in char:
# 				return True
# 			else:
# 				False
# 	pass
	
	
		

#Program inputs
center_letter = input("Center letter: ")
other_letters = input("Enter the other 6 letters lowercase and no spaces: ")
# center_letter = "w"
# other_letters = "obledf"

#puts 6 non-center letters into a list
other_letter_list = []
for char in other_letters:
	other_letter_list.append(char)
other_letter_list.append(center_letter)
#test
print(other_letter_list)

all_game_letters(other_letter_list)
spellingbee_mainLetter(center_letter)
# delete_shorts(new_wordlist)
final_list = (nonLetterLoop(non_game_letters, new_wordlist))
print(final_list)


# final_list = new2wordlist
# print(final_list)
# allSeven(new_wordlist)