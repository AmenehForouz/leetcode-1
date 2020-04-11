class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_reps = set()
        
        letters = {'a':".-", 'b':"-...", 'c':"-.-.",'d':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-",'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        
        for word in words:
            morse_string = ''
            for letter in word:
                morse_string += letters[letter]
            unique_reps.add(morse_string)
        
        return len(unique_reps)