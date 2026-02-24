def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text.replace(" ", ""))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def longest_word(text):
    words = text.split()
    return max(words, key=len) if words else ""

def word_frequency(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))

def analyze_text(text):
    """Main analysis function - calls all others"""
    results = {
        'words': count_words(text),
        'chars': count_chars(text),
        'vowels': count_vowels(text),
        'palindrome': is_palindrome(text),
        'longest': longest_word(text),
        'frequency': word_frequency(text)
    }
    return results

def display_results(results, text):
    """Display all analysis results"""
    print("=== TEXT ANALYSIS ===")
    print(f"Words: {results['words']}")
    print(f"Characters: {results['chars']}")
    print(f"Vowels: {results['vowels']}")
    print(f"Palindrome: {'Yes' if results['palindrome'] else 'No'}")
    print(f"Longest word: {results['longest']}")
    print("Word frequency:", results['frequency'])


text = input("Enter text: ")
results = analyze_text(text)
display_results(results, text)
