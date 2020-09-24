"""
Problem 804 - Unique Morse Code Words

International Morse Code defines a standard encoding where each letter is 
mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" 
maps to "-...", "c" maps to "-.-.", and so on.

Now, given a list of words, each word can be written as a concatenation of 
the Morse code of each letter. For example, "cba" can be written as 
"-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll 
call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_reps = set()

        letters = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        for word in words:
            morse_string = ""
            for letter in word:
                morse_string += letters[letter]
            unique_reps.add(morse_string)

        return len(unique_reps)


if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]
    print(Solution().uniqueMorseRepresentations(words))  # Should return 2
