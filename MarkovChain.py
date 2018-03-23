import random, string

# function for initializing the random sentence generator
def initializeWordList():

	# passage text for the markov chain
	with open('data.txt', 'r') as f:
		passage = f.read().replace("\n", " ").lower()
	
	# generate word list from the passage
	punctuations = string.punctuation.translate(str.maketrans('', '', ",./'")) + "/" # define unwanted punctuations
	passage = passage.translate(str.maketrans(punctuations, ' ' * len(punctuations))) # remove punctuations from passage text
	words = passage.replace(",", ", ").replace(".", ". ").split(" ") # get list of word from the passage
	
	# clean up the word list
	words = [word.strip("'") for word in words]
	words = ["I" if word == 'i' else word for word in words if len(word) > 0]
	
	wordDict = {} # the dictionary
	
	#generate markov chain dictionary
	for i in range(len(words) - 2):
	
		word1, word2 = words[i], words[i + 1] # first and second word of the key
		key = word1 + " " + word2 # the key of the dictionary
		wordNext = words[i + 2] # a possible value of the key
		
		if key in wordDict.keys():
			wordDict[key].append(wordNext) # add value to key if the key exists in the dictionary
		else:
			wordDict[key] = [wordNext] # create a new key if the key is not in the dictionary
			
	return wordDict

# function for generating a random sentence with random length
def randomSentence(wordDict, minWords, maxWords): # minimum/maximum number of words of the sentence

	# initialize and define variables
	numWords = random.randrange(minWords, maxWords + 1) # set the number of words of the sentence	
	word1, word2 = "", "" # initializing the first and second word for the markov chain	
	result = "" # the resulting sentence
	
	# walk through the markov chain
	for i in range(numWords):
	
		key = word1 + " " + word2 # key of the dictionary
		
		# get random words from the dictionary when the chain ends
		if key not in wordDict:
			while not word1.endswith('.') and i == 0: # first word is after a period
				key = random.choice(list(wordDict.keys())) # get random key			
				word1, word2, = key.split(" ") # get first and second word from the key
		
		if i > 0:
			result += " " # add space after each word in result string
		
		result += word2.capitalize() if word1.endswith('.') or i == 0 else word2  # add word to string and capitalize the word after a period
		
		word1, word2 = word2, random.choice(wordDict[key]) # move to the next state of the markov chain
	
	return result

chain = initializeWordList(); # dictionary for storing markov chain

print(randomSentence(chain, 900, 1000)) # generate a random sentences with length 900 to 1000
