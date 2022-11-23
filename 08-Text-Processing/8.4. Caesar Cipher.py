text = input()
encrypted_version = []
for char in text:
     encrypted_version.append(chr(ord(char) + 3))
print(f'{"".join(encrypted_version)}')
