from enum import Enum, IntEnum
from pydantic import BaseModel

class CuisineEnum(str, Enum):
    AMERICAN='american'
    BRITISH= 'british'
    MEXICAN= 'mexican'
    GERMAN= 'german'
    FRENCH= 'french'
    ITALIAN= 'italian'
    SPANISH= 'spanish'
    POLISH= 'polish'
    INDIAN= 'indian'
    CHINESE= 'chinese'
    KOREAN= 'korean'
    JAPANESE= 'japanese'
    THAI= 'thai'
    HAWAIIAN= 'hawaiian'
    
class MealType(str, Enum):
    breakfast= 'b'
    lunch= 'l'
    dinner= 'd'

class RedMeat(str, Enum):
    BEEF= 'beef'
    PORK= 'pork'
    LAMB= 'lamb'
    MUTTON= 'mutton'
    VENISON= 'venison'
    VEAL= 'veal'
    GOAT= 'goat'

class Poultry(str, Enum):
    CHICKEN= 'chicken'
    TURKEY= 'turkey'
    QUAIL= 'quail'
    DUCK= 'duck'

class Seafood(str, Enum):
    FISH= 'fish'
    SHELLFISH= 'shellfish'



class TimeRequirement(IntEnum):
    QUICK= 1
    NORMALPREP= 2
    ADVANCEDPREP= 3


class Meal(BaseModel): 
    name: str
    cuisine: CuisineEnum
    meal_type: set[MealType]
    protein: RedMeat | Poultry | Seafood
    time_req: TimeRequirement


    




