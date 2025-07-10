def mediatype(file):
    list_of_types = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]
    file = file.strip().lower()

    if list_of_types in file[0:5:-1]:
        print("yes")

mediatype("jnvdksajvnijvfi.jpg")
