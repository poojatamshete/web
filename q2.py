inputStr = input("Enter String to check palindrome\n")


def isPalindrome(inStr):
    inStr = inStr.lower()
    return inStr == inStr[::-1]


print(isPalindrome(inputStr))


#output
'''
root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment# python3 q2.py 
Enter String to check palindrome
himalaya
False
root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment# python3 q2.py 
Enter String to check palindrome
abbccbba
True

'''