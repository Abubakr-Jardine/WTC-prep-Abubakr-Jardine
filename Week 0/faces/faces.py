def faces(text):
    text = text.replace(":(","🙁")
    text = text.replace(":)","🙂")
    return text
def main():
    text = input()
    print(faces(text))

main()