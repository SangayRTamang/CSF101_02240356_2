from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

def longest_word(content):
    words = content.split()
    longest = max(words, key=len)
    return longest

def count_specific_word(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

def analyze_text(filename, target_word):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, count = most_common_word(content)
    longest = longest_word(content)
    specific_word_count = count_specific_word(content, target_word)
    avg_length = average_word_length(content)
    percent_longer_than_avg = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Occurrences of '{target_word}': {specific_word_count}")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than average: {percent_longer_than_avg:.2f}%")

analyze_text('C:\\Users\\VICTUS\\Desktop\\CSF101\\practial work 1\\sample.txt', 'your_target_word')
