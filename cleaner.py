import string
import re

def remove_emojis(text):    #removes all emojis
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"  # miscellaneous symbols
        "\U000024C2-\U0001F251"  # enclosed characters
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

def remove_punctuation(text):   #removes all punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_numbers(text):   #removes all digits 0-9
    return re.sub(r'\d+', '', text)

def remove_empty_lines(text):   #removes all empty lines
    return '\n'.join(line for line in text.splitlines() if line.strip())

def clean(file_path):   #runs all functions on target file and overwrites
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    
    cleanedtxt = remove_emojis(text)
    cleanedtxt = remove_punctuation(cleanedtxt)
    cleanedtxt = remove_numbers(cleanedtxt)
    cleanedtxt = remove_empty_lines(cleanedtxt)
    
    # Overwrite the modified content onto the same file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleanedtxt)