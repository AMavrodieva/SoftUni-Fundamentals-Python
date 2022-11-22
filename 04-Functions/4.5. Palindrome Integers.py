def palindrome(text):
    list_of_palindrome = text.split(", ")
    result = []
    for el in list_of_palindrome:
        if el == el[::-1]:
            result.append('True')
        else:
            result.append("False")
    return result

text = input()
palindrome_check = palindrome(text)
print(*palindrome_check, sep='\n')

# вариант 2
def palindrome(el):
    if el == el[::-1]:
        return True
    return False


text = input().split(", ")
for el in text:
    palindrome_check = palindrome(el)
    print(palindrome_check)
