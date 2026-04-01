Project Overview

This project is part of the Introduction to Python Programming and Databases lab.
It simulates real-world data analysis by working with a large and messy dataset of Twitter posts.

The goal is to:

Clean raw data
Analyze engagement
Implement custom algorithms (without using Python built-ins like .sort() or max())
Use Bash scripting for fast command-line analysis
Dataset
File name: twitter_dataset.csv
Source: Kaggle
Format: CSV with fields such as:
Username,Text,Likes,Retweets
Quest 1: Data Auditor (Cleaning Data)
Removes tweets with missing Text
Replaces missing Likes or Retweets with 0
Counts and prints number of "bad rows"
Function: clean_data(tweets)
Quest 2: Viral Post Finder
Finds the tweet with the highest number of likes
Implemented manually (NO max() used)
Function: find_viral_tweet(tweets)
Quest 3: Custom Sorting Algorithm
Uses a Selection Sort approach (partial optimization)
Sorts tweets by Likes in descending order
Displays Top 10 most liked tweets
Function: custom_sort_by_likes(tweets)
Quest 4: Content Filter (Search)
Takes user input keyword
Searches tweets (case-insensitive)
Stores matches in a new list
Displays:
Number of matches
Matching tweets
Function: search_tweets(tweets, keyword)
How to Run the Python Program
1. Ensure files are in the same folder:
twitter_dataset.csv
data-detective.py
2. Run the script:
python3 data-detective.py
3. Follow prompts:
Press Enter to move through quests
Input a keyword for search
Shell Script: feed-analyzer.sh
Purpose:
Find the Top 5 Most Active Users based on tweet frequency using Bash tools
How It Works
The script:
Filters valid rows
Extracts usernames
Counts occurrences
Sorts by highest activity
Run the Script
chmod +x feed-analyzer.sh
./feed-analyzer.sh
