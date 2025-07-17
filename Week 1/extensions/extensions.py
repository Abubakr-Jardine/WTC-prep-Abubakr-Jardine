def mediatype(file):
    list_of_types = ["gif","jpg","jpeg","png","pdf","txt","zip"]
    file = file.strip().lower()

    for type in list_of_types:
        if type in file[-5:]:
            if type == "txt":
                return f"plain/{type}"
            elif type == "pdf" or type == "zip":
                return f"application/{type}"
            elif type in "gif jpg jpeg png":
                return f"image/{type}"
            else:
                return "application/octet-stream"

file = input()

print(mediatype(file))
