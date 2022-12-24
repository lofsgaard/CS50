def main():
    filename = input("File name: ")
    if filename.lower().strip().endswith('.gif'):
        print("image/gif")
    elif filename.lower().strip().endswith('.jpg') or filename.lower().strip().endswith('.jpeg'):
        print("image/jpeg")
    elif filename.lower().strip().endswith('.png'):
        print("image/png")
    elif filename.lower().strip().endswith('.pdf'):
        print("application/pdf")
    elif filename.lower().strip().endswith('.txt'):
        print("text/plain")
    elif filename.lower().strip().endswith('.zip'):
        print("application/zip")
    else:
        print("application/octet-stream")

main()