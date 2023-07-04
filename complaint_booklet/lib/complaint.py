import json
from pathlib import Path
from typing import List


class Complaint:

    current_id = 0

    def __init__(self, title, text) -> None:
        self.__id = Complaint.current_id
        self.__title = title
        self.__text = text
        self.__resolved = False

        Complaint.current_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @property
    def title(self):
        return self.__title

    @property
    def resolved(self):
        return self.__resolved

    def mark_as_resolved(self):
        self.__resolved = True

    def __str__(self) -> str:
        return f"Title: {self.title}\nText: {self.text}"

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "text": self.__text,
            "resolved": self.__resolved,
        }

    def from_dict(self, d_in):
        pass


class Booklet:

    def __init__(self, data_store_path: Path) -> None:
        self.__complaints: List[Complaint] = []
        self.__data_store_path = data_store_path

    @property
    def complaints(self):
        return self.__complaints

    @property
    def unsolved_complaints(self):
        return [x for x in self.__complaints if not x.resolved]

    def add(self, complaint: Complaint):
        self.__complaints.append(complaint)

    def mark_solved(self, id: int):
        for i in self.__complaints:
            if id == i.id:
                i.mark_as_resolved()

    def __len__(self):
        return len(self.__complaints)

    def load_json(self) -> None:
        """
        Raises:
            OSError: if the path is not accessible
            json.JSONDecodeError: if json can not be parsed
        """
        with open(self.__data_store_path, 'r') as fin:
            objects = json.load(fin)
        self.__complaints = objects

    def save_json(self):
        with open(self.__data_store_path, "w") as fout:
            json.dump([x.to_dict() for x in self.__complaints], fout, indent=4)