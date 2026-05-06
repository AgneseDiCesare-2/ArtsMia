from dataclasses import dataclass

from model.objects import Object


@dataclass
class Arco:
    u: Object
    v: Object
    peso: float