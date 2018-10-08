def isPalindrome(s):
    '''
    Returns true if a (s) word is a palindrome.
    s: an inputed string
    '''
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False


inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")
