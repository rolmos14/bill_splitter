# put your python code here
double_alphabet = dict()
latin_alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
for letter in latin_alphabet:
    double_alphabet[letter] = letter * 2
