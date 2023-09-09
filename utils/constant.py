import enum

class PositionsType(enum.Enum):
    LONG = 1
    SHORT = 0

class DirectionType(enum.Enum):
    IN = 1
    OUT = 0

class PositionStatus(enum.Enum):
    OPEN = 1
    CLOSED = 0

class DataCreator(enum.Enum):
    FIXTURE = 1
    POPULATE = 2

