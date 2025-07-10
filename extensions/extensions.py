def mediatype(file):
    list_of_types = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]
    file = file.strip().lower()

    for type in list_of_types:
        if type in file[0:5:-1]:
            print("yes")

mediatype("jnvdksajvnijvfi.jpg")
