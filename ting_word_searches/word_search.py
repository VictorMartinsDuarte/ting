def all_processed_files(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": file["linhas_do_arquivo"],
        }
        for file in instance._data
    ]


def exists_word(word, instance):
    files_data = all_processed_files(word, instance)
    for file in files_data:
        file["ocorrencias"] = [
            {"linha": i + 1}
            for i, line in enumerate(file["ocorrencias"])
            if word.lower() in line.lower()
        ]
    if not file["ocorrencias"]:
        return []

    file_info = []
    file_info.append(file)
    return file_info


def search_by_word(word, instance):
    files_data = all_processed_files(word, instance)
    for file in files_data:
        file["ocorrencias"] = [
            {"linha": i + 1, "conteudo": line}
            for i, line in enumerate(file["ocorrencias"])
            if word.lower() in line.lower()
        ]
    if not file["ocorrencias"]:
        return []

    file_info = []
    file_info.append(file)
    return file_info
