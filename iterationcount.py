#SAMPLE CODE
print('SAMPLE CODE =====')
iteration = 0
count = 0
while iteration < 5:
    for letter in 'hello, world':
        count += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1

#TEST3
print('TEST 3 =====')
count = 0
phrase = 'hello, world'
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print('Iteration ' + str(iteration) + '; counts is: ' + str(count))

#PROBLEM 1
print('[PROBLEM 1] ==========')
s = 'this is a random text for counting vowels'
numOfVowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numOfVowels += 1
print('Number of vowels: ' + str(numOfVowels))

#PROBLEM 2
print('[PROBLEM 2] ==========')
s2 = 'this my friends is a philosophical dilemma bob for bobing bobob'
numOfOccur = 0
for i in range(len(s2)):
    if s2[i:i+3] == 'bob':
        numOfOccur += 1
print('Number of times bob occurs is: ' + str(numOfOccur))

#PROBLEM 3
print('[PROBLEM 3] ==========')
s = 'azcbobobegghakl'
tempStrings = []
for i in range(len(s)):
    badString = s[i:]
    tempStrings.append(badString)
print('Tablica wszystkie: ', tempStrings)

charCounter = 0
for i in range(len(tempStrings)-1):
    currentWord = tempStrings[i]
    for j in range(len(currentWord)):
        if j < len(currentWord)-1 and (currentWord[j] < currentWord[j+1] or currentWord[j] == currentWord[j+1]):
            charCounter += 1
        else:
            break
    tempStrings[i] = currentWord[:charCounter+1]
    charCounter = 0
print('Tablica sprawdzonych: ', tempStrings)
print('Longest substring in alpha order: ' + max(tempStrings, key=len))
