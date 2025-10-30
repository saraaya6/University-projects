


numbers = input('Enter a series of numbers separated by spaces: ')
numbers_list = numbers.split()
total = 0
for number in numbers_list:
    total += int(number)
print('The sum of the numbers is:', total)



'''
sentence = input('Enter your sentence : ')
words = sentence.split()
word_count = len(words)
print('total number of words : ', word_count)
'''