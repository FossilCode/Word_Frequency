from WordFrequency import countwords, format_most_common
from cleaner import clean
import os

# Automatically get all .txt files in the subfolder
texts = [os.path.join('Texts/', file) for file in os.listdir('Texts/') if file.endswith('.txt')]

numWords = int(input("how many words would you like information about? (default 5): ") or 5)
filtered_input = input("would you like to filter out 'stopwords'? (y/n, default y): ").lower() or 'y'

for text in texts:
    if filtered_input == 'y':
        filtered = True
    else:
        filtered = False
    
    clean(text)
    
    common_words = countwords(text, numWords, filtered)

    filename = os.path.basename(text)
    
    print(f"\nMost Common Words in {filename}:")
    print(format_most_common(common_words))