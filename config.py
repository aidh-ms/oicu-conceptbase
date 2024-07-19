from typing import Any
from enum import StrEnum, auto
from dataclasses import dataclass
from pydantic import BaseModel


class ConceptCoding(StrEnum):
    """
    Enum to define the coding system for the concept identifiers.
    """
    SNOMED = auto()
    LOINC = auto()


@dataclass
class MapperConfig:
    """
    Dataclass to define the configuration for a mapper.
    """
    klass: str
    source: str
    unit: str
    # TODO - Declare fixed set of parameters if possible
    params: dict[str, Any]


class ConceptConfig(BaseModel):
    """
    Dataclass to define the configuration for a concept.
    """
    name: str
    description: str
    identifiers: dict[ConceptCoding, str]
    unit: str
    # TODO - We either need the schema attribute, or the klass attribute but not both
    # schema: str
    mapper: list[MapperConfig]
