def isPalindrome(string):
    if len(string) < 2: return True
    else:
        if string[0] != string[len(string)-1]: return False
        else: return isPalindrome(string[1:len(string)-1])

while True:
    input_str = input()
    if input_str == '0': break

    if isPalindrome(input_str): print('yes')
    else: print('no')