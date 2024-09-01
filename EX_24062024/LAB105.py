letters = ['a', 'b', 'c', 'e', 'f', 'i', 'j', 'k', 'o']
def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

after_filter = filter(filter_vowel, letters)
print(list(after_filter))