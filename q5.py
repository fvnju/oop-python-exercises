"""
Write a class called Wordplay. It should have a field that holds a list of words. 
The user of the class should pass the list of words they want to use to the class. 
There should be the following methods:
 => words_with_length(length) — returns a list of all the words of length length
 => starts_with(s) — returns a list of all the words that start with s
 => ends_with(s) — returns a list of all the words that end with s
 => palindromes() — returns a list of all the palindromes in the list
 => only(L) — returns a list of the words that contain only those letters in L
 => avoids(L) — returns a list of the words that contain none of the letters in L
"""

class Wordplay:
    def __init__(self, words: list):
        self.words = words

    def words_with_length(self, length) -> list:
        answer = []
        for word in self.words:
            if len(word) == length:
                answer.append(word)
        return answer

    def starts_with(self, s: str) -> list:
        answer = []
        for word in self.words:
            if word[0] == s:
                answer.append(word)
        return answer

    def ends_with(self, s: str) -> list:
        answer = []
        for word in self.words:
            if word[-1] == s:
                answer.append(word)
        return answer

    def palindromes(self) -> list:
        answer = []
        for word in self.words:
            if word[::-1] == word:
                answer.append(word)
        return answer

    def only(self, L: str) -> list:
        answer = []
        for word in self.words:
            if all(char in L for char in word):
                answer.append(word)
        return answer

    def avoids(self, L: str) -> list:
        answer = []
        for word in self.words:
            if all(char not in L for char in word):
                answer.append(word)
        return answer


# Test Usage
first = Wordplay(["ogo", "madam", "madman", "batman", "answer"])
print(first.only("madam"))
print(first.avoids("madam"))
print(first.starts_with("m"))
print(first.ends_with("n"))
print(first.palindromes())
print(first.words_with_length(6))
