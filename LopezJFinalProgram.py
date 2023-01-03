#LopezJFinalProgram.py
"""
Name: Jason Lopez
Date: December 15th, 2022
Class: CSEC 1436
Purpose: Enter a number to populate a word list that has the same amount of characters and number of palindromes.

Pseudo Code:
            Create a function for ReadFile(size). This will read the text file, if validates, returns it.
            Create a function for GetPalindromes(Alist). This will check if the word is palindrome.
            Create a main function that outputs the size of the word, number of words of the size, and number of palindromes.
"""

#Function reads file word by word. If the length of the word matches the size parameter, is lowercase, and alpha, then it is returned.
def ReadFile(size):
    selectedword = []
    try:
        with open('EnglishLanguageDict.txt', 'r') as IFile: # Opens file and reads it. 
            for line in IFile:
                for word in line.split():
                    if len(word) == size:
                        if word.islower():
                            if word.isalpha():
                                selectedword.append(word)
            return selectedword
    except FileNotFoundError:
        print("File EnglishLanguageDict.tx was not found.")
        exit(0)

# Function checks if word in list is palindrome. List is printed afterwards.
def GetPalindromes(Alist):
    paliwords = []
    for word in Alist:
        if word == word[::-1]:
            paliwords.append(word)
    return paliwords

# Main function that will hold our outputs for size of word, num of words, and num of palindromes.
def main():
    while True:
        try:
            wordsize = int(input("Input the size of the word (5 to 20): "))                      # User input for input size of word.
            if wordsize >= 5 and wordsize <= 20:
                words = ReadFile(wordsize)
                numwords = len(words)
                print(f'The number of words of that size are: {numwords}')                       # Outputs number of words of that size.
                paliwords = GetPalindromes(words)
                numpali = len(paliwords)
                print(f'The number of palindromes of words of size 5 are: {numpali}. They are:') # Outputs number of palindromes of words
                print(*paliwords)                                                                # Returns words without brackets and commas
                break
            else:
                pass
        except ValueError:
            pass

if __name__ == "__main__":
    main()