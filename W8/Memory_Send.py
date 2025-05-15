# write_data.py
def save_to_memory(data):
    with open("nvm_storage.txt", "w") as file:
        file.write(str(data))

save_to_memory("KimieWasHere")
print("Memory saved!")
