import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    bad_tweets = 0
    clean_tweets = []
    for t in tweets:
        text = t.get('Text')
        likes = t.get('Likes')
        retweets = t.get('Retweets')
        if text is None or str(text).strip() == "":
            bad_tweets += 1
            continue
        if likes is None or str(likes).strip() == "":
            t['Likes'] = 0
            bad_tweets += 1
        if retweets is None or str(retweets).strip() == "":
            t['Retweets'] = 0
            bad_tweets += 1

        clean_tweets.append(t)
    print(f"The number of bad rows is {bad_tweets}")
    return clean_tweets
                

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    max_likes = 0
    best_tweet = None
    for t in tweets:
        likes = int(t.get('Likes', 0))
        if likes > max_likes:
            max_likes = likes
            best_tweet = t

    if best_tweet:
        print(f"The tweet with the highest likes is: ")
        print(f"Username: {best_tweet['Username']}")
        print(f"Text: {best_tweet['Text']}")
        print(f"Likes: {max_likes}")
    else:
        print("No tweet found")


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    sorted_tweets = tweets.copy()
    n = len(sorted_tweets)

    for i in range(10):
        max_index = i

        for j in range (i + 1, n):
            if int(sorted_tweets[j].get('Likes', 0)) > int(sorted_tweets[max_index].get('Likes', 0)):
                max_index = j
        sorted_tweets[i], sorted_tweets[max_index] = sorted_tweets[max_index], sorted_tweets[i]
        
    top_10 = sorted_tweets[:10]
    print("Top 10 Most Liked Tweets:")
    for rank, tweet in enumerate(top_10, 1):
        print(f"Rank #{rank}")
        print(f"  Username: {tweet['Username']}")
        print(f"  Likes: {tweet['Likes']}")
        print(f"  Text: {tweet['Text']}")

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matched_tweets = []
    for t in tweets:
        text = t.get('Text', '')
        if keyword.lower() in text.lower():
            matched_tweets.append(t)
    print(f"\nFound {len(matched_tweets)} tweets containing '{keyword}':")

    for tweet in matched_tweets:
        print(f"Username : {tweet['Username']}")
        print(f"Likes    : {tweet['Likes']}")
        print(f"Text     : {tweet['Text']}")

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # Call your functions here to complete the quests!
    # Example: clean_dataset = clean_data(dataset)
    clean_dataset = clean_data(dataset)
    input("/nPress Enter to continue to quest 2")
    find_viral_tweet(clean_dataset)
    input("/nPress Enter to continue to quest 3")
    custom_sort_by_likes(clean_dataset)
    input("/nPress Enter to continue to quest 4")
    keyword = input("Enter a keyword to search for: ")
    search_tweets(clean_dataset, keyword)
    