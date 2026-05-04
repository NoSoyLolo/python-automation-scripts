import os

def clean_temp_files(path):
    for file in os.listdir(path):
        if file.endswith(".tmp"):
            os.remove(os.path.join(path, file))
    return "Archivos temporales eliminados"

if __name__ == "__main__":
    print(clean_temp_files("./temp"))