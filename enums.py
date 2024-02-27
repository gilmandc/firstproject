from enum import Enum

class RedMeat(Enum):
    BEEF: str = "beef"
    LAMB: str = "lamb"
    GAME: str = "game"

class Poultry(Enum):
    CHX: str = "chicken"
    TURKEY: str = "turkey"
    GOOSE: str = "goose"

class Protein(Enum):
    RED_MEAT: RedMeat 
    POULTRY: Poultry = Poultry.TURKEY

