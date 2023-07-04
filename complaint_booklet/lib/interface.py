import sys
from typing import List
from abc import abstractmethod, ABC
from lib.complaint import Booklet, Complaint
from lib import data_store


class MenuItem(ABC):

    def __init__(self, title) -> None:
        super().__init__()
        self.title = title

    @abstractmethod
    def execute(self):
        pass


class MenuActionItem(MenuItem):

    def __init__(self, title, booklet) -> None:
        super().__init__(title)
        self.booklet: Booklet = booklet


class ListUnsolved(MenuActionItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        for obj in self.booklet.unsolved_complaints:
            print(obj)
            print()
        print(f"\nTOTAL: {len(self.booklet.unsolved_complaints)} elemente")
        input("Apasa orice tasta pentru a reveni la meniul principal.")


class AddItem(MenuActionItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        self.booklet.add(Complaint(
            input("Title: "),
            input("Text: ")
        ))
        self.booklet.save_json()
        input("Reclamatie adaugata. Apasa orice tasta pentru a reveni.")

class SolveOne(MenuActionItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        for obj in self.booklet.unsolved_complaints:
            print(f"{obj.id} - {obj.title}")
        self.booklet.mark_solved(
            int(input("Introdu id-ul reclamatiei pentru a o rezolva."))
        )
        
class MenuUserChoice(MenuItem):

    def __init__(self, title) -> None:
        super().__init__(title)
        self.__commands: List[MenuItem] = []

    def execute(self):
        user_choice = -1
        print(f"{self.title:-^50}")

        while user_choice not in range(1, len(self.__commands) + 1):
            for i, command in enumerate(self.__commands, start=1):
                print(f"{i} -> {command.title}")
            try:
                user_choice = int(
                    input("Alege un numar din lista de mai sus: "))
            except ValueError:
                print("EROARE: Te rog sa alegi un numar din numerele de mai sus.")

        self.__commands[user_choice - 1].execute()

    def add_choice(self, choice: MenuItem) -> None:
        self.__commands.append(choice)


class ExitItem(MenuItem):

    def execute(self):
        sys.exit(0)