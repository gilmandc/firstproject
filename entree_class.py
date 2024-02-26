from dataclasses import dataclass


@dataclass
class Entree:
    name: str
    meal_type: str
    protein: str
    cuisine: str
    time_req: int



