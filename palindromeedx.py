word = 'Able was I, ere I saw Elba'

def isPalindrome(word):

    def toChars(word):
        word = word.lower()
        ans = ''
        for c in word:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans
    
    def isPal(word):
        if len(word) <= 1:
            return True
        else:
            return word[0] == word[-1] and isPal(word[1:-1])
    
    return isPal(toChars(word))


print(isPalindrome(word))
