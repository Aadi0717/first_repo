word = "donkey"

with open("demo.txt", "r") as f:
    content = f.read()
    
contentnew = content.replace(word, "#####")

with open("demo.txt", "w") as f:
    f.write(contentnew)