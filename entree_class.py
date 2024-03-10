from dataclasses import dataclass
from enums import Protein

@dataclass
class Entree:
    name: str
    meal_type: str
    protein: str
    cuisine: str
    time_req: int

    def to_dict(self) -> dict:
        """Turns object to dictionary"""
        return {'name':self.name, 'meal_type':self.meal_type,
                 'protein':self.protein, 'cuisine':self.cuisine, 'time_req': self.time_req}
    

