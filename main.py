from WordFrequency import countwords, format_most_common
from cleaner import clean
import os
subfolder = 'Texts/'
# Automatically get all .txt files in the subfolder
texts = [os.path.join(subfolder, file) for file in os.listdir(subfolder) if file.endswith('.txt')]

numWords = 5    #how many words would you like information about?
filtered = True #would you like to filter out 'stopwords'


for text in texts:
    
    clean(text)
    
    common_words = countwords(text, numWords, filtered)

    filename = os.path.basename(text)
    
    print(f"\nMost Common Words in {filename}:")
    print(format_most_common(common_words))