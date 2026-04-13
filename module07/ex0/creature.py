from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, cr_type: str) -> None:
        self.name = name
        self.cr_type = cr_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.cr_type} type Creature"
