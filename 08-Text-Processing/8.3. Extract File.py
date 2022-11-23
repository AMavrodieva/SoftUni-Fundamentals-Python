path = input().split(":")
text = (path[1].split("\\"))
file_name = text[-1].split(".")
print(f"File name: {file_name[-2]}")
print(f"File extension: {file_name[-1]}")

