from collections import UserDict
from output_view import NoteBookView
import pickle
import re


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self.index = 1
        self.ind_lst = []
        self.ov = NoteBookView()

    def read_file(self):
        with open('NoteBook.bin', 'rb') as reader:
            received_notebook = pickle.load(reader)
            self.data = received_notebook.data
            self.ov = received_notebook.ov
            self.index = received_notebook.index
            self.ind_lst = received_notebook.ind_lst

    def write_file(self):
        with open('NoteBook.bin', 'wb') as writer:
            pickle.dump(self, writer)

    def add_note(self, record):
        while self.index in self.ind_lst:
            self.index += 1
        self.ind_lst.append(self.index)
        self.ind_lst.append(self.index)
        self.data[max(self.ind_lst)] = record
        return self.index
    
    def edit_note(self, index, new_note):
        self.data[index].note = Note(new_note)
        return f"Note {index} successfully changed"

    def remove_note(self, index):
        self.data.pop(index, None)

    def search_note(self, symb):
        result = []
        for rec in self.data:
            if symb.lower() in str(self.data[rec].note).lower():
                result.append([rec, ", ".join(p.value for p in self.data[rec].tags), self.data[rec].note.value])
        if result:
            return self.ov.create_table(result)
        else:
            return 'No matches found'

    def sort_tags(self, symb):
        result = []
        for rec in self.data:
            for tag in self.data[rec].tags:
                if symb.lower() in str(tag).lower():
                    result.append([rec, ", ".join(p.value for p in self.data[rec].tags), self.data[rec].note.value])
        if result:
            return self.ov.create_table(result)
        else:
            return 'No matches found'

    def show_all(self):
        result = []
        for index, wr in self.data.items():
            result.append([index, ", ".join(p.value for p in wr.tags), wr.note.value])
        return self.ov.create_table(result)


class Field:
    def __init__(self, value):
        self.value = value


class Tag(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __str__(self):
        return str(self.value)


class Note(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, note, tag=None):
        self.note = Note(note)
        self.tags = []
        if tag:
            self.tag_list = re.split(" ", tag)
            for tag in self.tag_list:
                self.tags.append(Tag(tag))


NOTEBOOK = NoteBook()