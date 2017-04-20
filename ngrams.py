table = {ord(char): None for char in string.punctuation}
# suspect ngrams in ngram_list[0], original ngrams in ngram_list[1]
ngram_list = [[] for x in range(2)]
for indx, text in enumerate([suspect, original]):
	word_list = text.translate(table).split()
	ngram = []
	# go through all words up until 3rd to last word
        	for i in range(0, len(word_list)-2 if len(word_list)>2 else len(word_list)):
                        s_ngram = []
                        # get n=3 gram starting at word i
                        for j in range(i, i+3 if len(word_list)>2 else len(word_list)-i):
                                s_ngram.append(word_list[j])
                        ngram.append(s_ngram)
                ngram_list[indx] = ngram
