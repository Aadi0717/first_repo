word = ["donkey","bad","ganda"]

with open("demo.txt", "r") as f:
    content = f.read()
    
for w in word:
    content = content.replace(w, "#####")

with open("demo.txt", "w") as f:
    f.write(content)