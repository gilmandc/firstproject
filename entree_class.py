from dataclasses import dataclass
from enums import Protein

@dataclass
class Entree:
    name: str
    meal_type: str
    protein: Protein
    cuisine: str
    time_req: int



