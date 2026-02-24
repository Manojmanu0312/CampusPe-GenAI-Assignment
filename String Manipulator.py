
sentence = input("Enter a sentence: ")


print("Original sentence:", sentence)


total_chars = len(sentence)
print("Total characters (with spaces):", total_chars)


chars_no_spaces = len(sentence.replace(" ", ""))
print("Total characters (without spaces):", chars_no_spaces)


words = len(sentence.split())
print("Total words:", words)


first_word = sentence.split()[0]
print("First word:", first_word)


last_word = sentence.split()[-1]
print("Last word:", last_word)


title_case = sentence.title()
print("Title case:", title_case)


reversed_sentence = sentence[::-1]
print("Reversed sentence:", reversed_sentence)
