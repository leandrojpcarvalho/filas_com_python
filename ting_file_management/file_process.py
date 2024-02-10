from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
from ting_file_management.indigent import Indigent
import sys


def process(path_file: str, instance: Queue):
    if not instance.search_by_value(path_file):
        processed_file = txt_importer(path_file)
        new_data = instance.enqueue(Indigent(path_file, processed_file))
        print(new_data, file=sys.stdout)
    return ""


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    indigent_file = instance.dequeue()
    print(
        f"Arquivo {indigent_file.path} removido com sucesso",
        file=sys.stdout,
    )


def file_metadata(instance: Queue, position: int):
    try:
        indigent_element = instance.search(position)
        print(indigent_element, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
