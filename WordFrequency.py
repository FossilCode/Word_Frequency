from collections import Counter
from nltk.corpus import stopwords
import nltk
import math

def countwords(txt, numWords, filter=True):
    with open(txt, "r", encoding="utf-8") as f:
        words = f.read().lower().split()
    
    global totallength
    totallength = len(words)

    # removes stopwords
    if filter:
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

    # dict like object of words and their frequency, ordred by freq. takes the top n words
    word_counts = Counter(words) 
    most_common_words = word_counts.most_common(numWords)

    # returns an arr of len numWords, filled with tuples
    return most_common_words

# format the most common words into a table
def format_most_common(most_common_words):
    formatted_output = f"{'Word':<15}{'Frequency':<15}{'Percentage':<15}{'Total wordcount: '+str(totallength)}\n"
    formatted_output += '—' * 50 + '\n'
    # gets the two values from the tuple pairs as 'word , freq'
    for word, freq in most_common_words:
        formatted_output += f"{word:<15}{freq:<15}{round(freq/totallength,5)}\n"
    return formatted_output