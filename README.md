# Text Cleaner and Reddit Scraper

This repository contains Python scripts that provide functionality for cleaning text files and scraping titles from various subreddits on Reddit. The scripts are designed to help users prepare text data for analysis and gather popular topics from the Reddit community.

## Usage

### Text Cleaning

The text cleaning functionality is found in the `cleaner.py` script. This script removes emojis, punctuation, numbers, and empty lines from text files located in the `Texts` directory.

#### Steps to Use:

1. **Prepare your text files:**  
   Place the text files you want to clean in a folder named `Texts` within the project directory.

2. **Run the cleaner:**  
   Execute the script that uses the cleaner.

### Word Frequency Analysis

The frequency analysis functionality is handled in the same script. It counts and formats the most common words in the cleaned text files.

#### Adjust Parameters:

- **Number of Words:**  
  Change the `numWords` variable to set the number of words to analyze.

- **Filter Stopwords:**  
  Modify the `filtered` variable to determine whether to filter out stopwords.

#### View Output:

After cleaning, the script will print the most common words in each file, along with their frequency and percentage.

### Reddit Scraping

The `scrape_subreddits.py` script allows you to scrape the top titles from specified subreddits.

#### Steps to Use:

1. **Modify Subreddit List:**  
   Update the subreddit list in the script to include any additional subreddits you wish to scrape.

2. **Run the Scraper:**  
   Execute the Reddit scraper.

## Features

- **Text Cleaning:**  
  Remove emojis, punctuation, numbers, and empty lines from text files.

- **Word Frequency Analysis:**  
  Identify and display the most common words in cleaned text files, with options to filter out stopwords.

- **Reddit Scraping:**  
  Scrape popular titles from specified subreddits and save them to a text file.
