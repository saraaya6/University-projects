def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input('Enter a word: ')
if is_palindrome(word):
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')



#https://twitter.com/Sara_amrey/status/1684435582984880128?s=20