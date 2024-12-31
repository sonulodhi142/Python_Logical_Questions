#That is the funtion which takes a pragraph and find the maximun length palindrom word in the pragraph and max-length not-plindrom word

#Here the function that return the True or false as per the word
def is_palindrome(word):
    return word == word[::-1]



def find_longest_words(sentence):
    words = sentence.split()
    
    longest_word = ""
    longest_non_palindrome = ""
    
    for word in words:
        # Update the longest word
        if len(word) > len(longest_word):
            longest_word = word
        
        # Update the longest non-palindromic word
        if not is_palindrome(word) and len(word) > len(longest_non_palindrome):
            longest_non_palindrome = word
            
    print("long word::", longest_word)
    print("long_non_p::", longest_non_palindrome)

input_str = """A palindrome is a word  number phrase or other sequence of symbols that reads the same backwards as forwards such as the words madam or racecar or tattarrattat """

find_longest_words(input_str)