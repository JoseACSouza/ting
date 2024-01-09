import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r") as file:
            if not path_file.lower().endswith('.txt'):
                raise ValueError()
            file_read = file.read()
            lines = file_read.split('\n')
            return lines
    except FileNotFoundError:
        sys.stderr.write("Arquivo " + path_file + " não encontrado\n")
        return None
    except ValueError:
        sys.stderr.write("Formato inválido")
        return None
