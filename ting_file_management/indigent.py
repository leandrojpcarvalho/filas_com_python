from dataclasses import dataclass, asdict


class Indigent:
    def __init__(self, path: str, lines: list[str]) -> None:
        self.__path = path
        self.__lines = lines

    def __len__(self):
        return len(self.__lines)

    def __dict__(self):
        return {
            "nome_do_arquivo": self.__path,
            "qtd_linhas": len(self),
            "linhas_do_arquivo": self.__lines,
        }

    def __str__(self) -> str:
        return str(
            {
                "nome_do_arquivo": self.__path,
                "qtd_linhas": len(self),
                "linhas_do_arquivo": self.__lines,
            }
        )

    @property
    def path(self):
        return self.__path

    @property
    def lines(self):
        return self.__lines

    def find_words(self, word: str):
        for index, line in enumerate(self.__lines):
            if word.lower() in line.lower():
                return index
        return False

    def find_word_at_lines(self, word: str, is_search=False):
        list_word = list()
        for index, line in enumerate(self.__lines):
            if word.lower() in line.lower():
                list_word.append(
                    Info(index + 1, line) if is_search else Lines(index + 1)
                )
        return asdict(SearchLines(word, self.path, list_word))


@dataclass
class Lines:
    linha: int


@dataclass
class Info(Lines):
    conteudo: str

    def __init__(self, line: int, conteudo: str):
        super().__init__(line)
        self.conteudo = conteudo


@dataclass
class SearchLines:
    palavra: str
    arquivo: str
    ocorrencias: list[Lines] | list[Info]
