import sys


def txt_importer(path_file: str):
    if path_file.split(".")[1] != "txt":
        print("Formato inválido", file=sys.stderr)
        return
    try:
        with open(path_file, "r") as file_open:
            return file_open.read().split("\n")
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
