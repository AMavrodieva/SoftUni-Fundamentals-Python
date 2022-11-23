command = input()
notes = [0] * 10
while command != "End":
   importance, note = command.split("-")
   current_index = int(importance) - 1
   notes[current_index] = note
   command = input()
print([el for el in notes if el != 0])

#while command != "End":
  # importance, note = command.split("-")
   #notes.pop(int(importance))
  # notes.insert(int(importance), note)
  # command = input()
#print([el for el in notes if el != 0])