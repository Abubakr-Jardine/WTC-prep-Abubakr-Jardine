answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
correct = ["42","forty-two","forty two"]
answer = str(answer)

if answer.lower().strip() in correct:
    print("Yes")
else:
    print("no")
