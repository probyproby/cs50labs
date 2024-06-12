
'''
prompts user for name file with is extension (.jpg).lower()
check if file type if in the system:
    print(file name)
else:
    file type not found

'''

filename = str(input("Filename: ")).lower()

if ".gif" in filename:
    print("image/gif")
elif ".png" in filename:
    print("image/png")
elif ".jpeg" in filename:
    print("image/jpeg")
elif ".pdf" in filename:
    print("application/pdf")
elif ".txt" in filename:
    print("text/plain")
elif ".jpg" in filename:
    print("image/jpeg")
elif ".zip" in filename:
    print("application/zip")
elif ".pdf" and ".txt" in filename:
    print("application/pdf")
else:
    print("application/octet-stream")