# Replace this comment with an appropriate header comment.

# Replace this comment with your function definitions.



## Evaluation

##def evaluate(word_sentiment_dict, filename):
##    f = open(filename, "r")
##    correct = 0
##    incorrect = 0
##    for line in f:
##        line = line.strip()
##        score = int(line[0])
##        words = line[2:]
##        predicted_positive = is_positive(words, word_sentiment_dict)
##        if score > 2 and predicted_positive:
##            correct += 1
##        elif score <= 2 and not predicted_positive:
##            correct += 1
##        else:
##            incorrect += 1
##    f.close()
##    print("predicted correctly:", correct, "("+str(correct/(correct+incorrect))+")")
##    print("predicted incorrectly:", incorrect, "("+str(incorrect/(correct+incorrect))+")")


### DO NOT DELETE THIS LINE: beg testing
    
word_sentiment_dictionary = make_word_sentiment_dictionary("movie_reviews_training.txt")

print("nice", word_sentiment_dictionary["nice"])
print("story", word_sentiment_dictionary["story"])

# print(predict_sentiment_score("This movie is awesome !", word_sentiment_dictionary))

# evaluate(word_sentiment_dictionary, "movie_reviews_dev.txt")
