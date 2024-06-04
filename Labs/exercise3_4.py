'''Write a function pos(word, text) for finding the left-most appearance of a non-empty string word within a string 'text' at every second character. If such occurrence exists then the function should return the index within text of the first character of the found appearance otherwise, the function should return -1.

Try to use slices. What is the complexity of this algorithm?

Sample results of the function:

pos("a", "") == -1
pos("hsal", "Mary has a little lamb") == 5'''

def pos(word, text):
    if not word or not text:
        return -1
    for string in range(1, len(text), 2):
        if text[string:string+len(word)] == word:
            return string
print(pos("a", ""))
print(pos("hsal", "Marry has a little lamb"))