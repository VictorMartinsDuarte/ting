from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    if processed_file in instance._data:
        return None

    instance.enqueue(processed_file)
    print(processed_file)


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    file_name = instance._data[0]["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
