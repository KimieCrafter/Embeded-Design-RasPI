def read_from_memory():
    try:
        with open("nvm_storage.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No memory yet!"

print("Recovered memory:", read_from_memory())
