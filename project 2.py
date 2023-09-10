filename = input("Input the Filename: ")
parts = filename.split(".")
extension = parts[-1].lower()  # Convert to lowercase
print(f"The extension of the file is:'{extension}'")