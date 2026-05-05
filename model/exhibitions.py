from dataclasses import dataclass


@dataclass
class Exhibition:
    exhibition_id: int
    exhibition_department: str
    exhibition_title: str
    begin: float
    end: float

def __hash__(self):
    return hash(self.exhibition_id)

def __eq__(self, other):
    return self.exhibition_id == other.exhibition_id


