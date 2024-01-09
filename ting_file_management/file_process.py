from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in instance.get_txt_processed():
        return None

    file_lines = txt_importer(path_file)
    data = {}
    data["nome_do_arquivo"] = path_file
    data["qtd_linhas"] = len(file_lines)
    data["linhas_do_arquivo"] = file_lines

    instance.enqueue(data, path_file)

    print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
