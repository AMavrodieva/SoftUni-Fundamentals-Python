list_of_word = input().split(" ")
searched_palindrome = input()
palindromes = [word for word in list_of_word if word == word[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")


#list_of_word = input().split(" ")
#searched_palindrome = input()
#palindromes = []

#for word in list_of_word:
   # if word == "".join(reversed(word)):
    #    palindromes.append(word)
#print(f"{palindromes}")
#print(f"Found palindrome {palindromes.count(searched_palindrome)} times")