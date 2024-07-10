from prettytable import PrettyTable
from abc import abstractmethod, ABC


class OutputView(ABC):
    @abstractmethod
    def create_table(self, data):
        pass

    @abstractmethod
    def create_row(self, data):
        pass


class AddressBookView(OutputView):
    def create_table(self, data):
        result_view = PrettyTable()
        result_view.field_names = ['Name','Birthday','Email','Address','Phone']
        for i in data:
            result_view.add_row(i)
        return result_view

    def create_row(self, data):
        result_view = PrettyTable()
        result_view.field_names = ['Name','Birthday','Email','Address','Phone']
        result_view.add_row(data)
        return result_view


class NoteBookView(OutputView):
    def create_table(self, data):
        result_view = PrettyTable()
        result_view.field_names = ['Index', 'Tags', 'Note']
        for i in data:
            result_view.add_row(i)
        return result_view

    def create_row(self, data):
        result_view = PrettyTable()
        result_view.field_names = ['Index', 'Tags', 'Note']
        result_view.add_row(data)
        return result_view


class SortDirectoryView(OutputView):
    def create_row(self, data):
        result_view = PrettyTable()
        result_view.field_names = ['Known_extensions', "Unknown_extensions"]
        result_view.add_row(data)
        return result_view

    def create_table(self, data):
        pass
