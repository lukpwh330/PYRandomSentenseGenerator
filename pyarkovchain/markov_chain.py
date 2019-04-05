import random
import string


class MChain:
	def __init__(self, DEPTH=2):
		self.DEPTH = DEPTH
		self.wordDict = {}

	def init(self, data):
		# Generate word list from the passage
		punctuations = string.punctuation.translate(str.maketrans('', '', ",./'")) + "/" # Define unwanted punctuations
		passage = data.translate(str.maketrans(punctuations, ' ' * len(punctuations))) # Remove punctuations from passage text
		words = passage.replace(",", ", ").replace(".", ". ").split(" ") # Get list of word from the passage

		# Clean up the word list
		words = [word.strip("'") for word in words]
		words = ["I" if word == 'i' else word for word in words if len(word) > 0]

		# Generate markov chain dictionary
		for i in range(len(words) - self.DEPTH):
			word_list = []
			for j in range(self.DEPTH):  # Go trough depth and append that many words to list
				word_list.append(words[i + j]) # Depth number of words of the key

			key = " ".join(word_list) # The key of the dictionary
			wordNext = words[i + self.DEPTH] # A possible value of the key

			if key in self.wordDict.keys():
				self.wordDict[key].append(wordNext) # Add value to key if the key exists in the dictionary

			else:
				self.wordDict[key] = [wordNext] # Create a new key if the key is not in the dictionary

	def predict(self, min_words, max_words):

		# Initialize and define variables
		numWords = random.randrange(min_words, max_words + 1) # Set the number of words of the sentence
		result = "" # The resulting sentence
		word_list = []
		for i in range(self.DEPTH):
			word_list.append("") # Initializing the word list for the markov chain

		# Walk through the markov chain
		for i in range(numWords):

			key = " ".join(word_list) # Key of the dictionary
			# Get random words from the dictionary when the chain ends
			if key not in self.wordDict:
				for k in range(self.DEPTH):
					while not word_list[k].endswith('.') and i == 0: # First word is after a period
						key = random.choice(list(self.wordDict.keys())) # Get random key
						word_list = list(key.split(" ")) # Get words from the key

			if i > 0:
				result += " " # Add space after each word in result string

			result += word_list[1].capitalize() if word_list[0].endswith('.') or i == 0 else word_list[1]# Add word to string and capitalize the word after a period

			del word_list[0]
			word_list.append(random.choice(self.wordDict[key])) # Move to the next state of the markov chain


		return result
