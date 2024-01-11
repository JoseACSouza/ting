def exists_word(word, instance, include_content=False):
    result = []

    for i in range(len(instance)):
        data = instance.search(i)
        occurrences = []

        occurrences = [
            {"linha": index + 1, "conteudo": line}
            if include_content
            else {"linha": index + 1}
            for index, line in enumerate(data["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        if len(occurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
