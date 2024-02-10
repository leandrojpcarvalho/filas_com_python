from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    response = instance.search_by_text(word)
    if any([len(value["ocorrencias"]) == 0 for value in response]):
        return []
    return response


def search_by_word(word, instance: Queue):
    response = instance.search_by_text(word, True)
    if any([len(value["ocorrencias"]) == 0 for value in response]):
        return []
    return response
