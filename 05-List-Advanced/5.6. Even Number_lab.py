number = list(map(int, input().split(", ")))
even_number = [i for i in range(len(number)) if number[i] % 2 == 0]
print(even_number)

#numbers = list(map(int, input().split(", ")))
#even_indices = []

#for i in range(len(numbers)):
   # if numbers[i] % 2 == 0:
      #  even_indices.append(i)

#print(even_indices)

