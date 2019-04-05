import random
import string


# Function for initializing the random sentence generator
def initializeWordList():

	# Passage text for the markov chain
	with open('data.txt', 'r') as f:
		passage = f.read().replace("\n", " ").lower()

	# Generate word list from the passage
	punctuations = string.punctuation.translate(str.maketrans('', '', ",./'")) + "/" # Define unwanted punctuations
	passage = passage.translate(str.maketrans(punctuations, ' ' * len(punctuations))) # Remove punctuations from passage text
	words = passage.replace(",", ", ").replace(".", ". ").split(" ") # Get list of word from the passage

	# Clean up the word list
	words = [word.strip("'") for word in words]
	words = ["I" if word == 'i' else word for word in words if len(word) > 0]

	wordDict = {} # The dictionary storing words

	# Generate markov chain dictionary
	for i in range(len(words) - 3):

		word1, word2, word3 = words[i], words[i + 1], words[i + 2] # First and second word of the key
		key = " ".join([word1, word2, word3]) # The key of the dictionary
		wordNext = words[i + 3] # A possible value of the key

		if key in wordDict.keys():
			wordDict[key].append(wordNext) # Add value to key if the key exists in the dictionary

		else:
			wordDict[key] = [wordNext] # Create a new key if the key is not in the dictionary

	return wordDict


# Function for generating a random sentence with random length
def randomSentence(wordDict, minWords, maxWords): # Minimum/maximum number of words of the sentence

	# Initialize and define variables
	numWords = random.randrange(minWords, maxWords + 1) # Set the number of words of the sentence
	word1, word2, word3 = "", "", "" # Initializing the first and second word for the markov chain
	result = "" # The resulting sentence

	# Walk through the markov chain
	for i in range(numWords):

		key = " ".join([word1, word2, word3]) # Key of the dictionary

		# Get random words from the dictionary when the chain ends
		if key not in wordDict:
			while not word1.endswith('.') and i == 0: # First word is after a period
				key = random.choice(list(wordDict.keys())) # Get random key
				word1, word2, word3 = key.split(" ") # Get first and second word from the key

		if i > 0:
			result += " " # Add space after each word in result string

		result += word2.capitalize() if word1.endswith('.') or i == 0 else word2  # Add word to string and capitalize the word after a period
		word1, word2, word3 = word2, word3, random.choice(wordDict[key]) # Move to the next state of the markov chain

	return result


chain = initializeWordList(); # Dictionary for storing markov chain

print(randomSentence(chain, 900, 1000)) # Generate a random sentences with length 900 to 1000
