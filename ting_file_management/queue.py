from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self._txt_processed = set()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value, name=""):
        self._data.append(value)
        if name:
            self._txt_processed.add(name)
        else:
            self._txt_processed.add(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index > len(self._data)-1 or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self._data[index]

    def get_txt_processed(self):
        return self._txt_processed
