def mediatype():
    file = input()
    list_of_types = ["gif","jpg","jpeg","png","pdf","txt","zip"]
    file = file.strip().lower()

    for type in list_of_types:
        if type in file[-5:]:
            if type == "txt":
                return f"plain{type}"
            elif type == 


print(mediatype())
