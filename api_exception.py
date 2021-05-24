from dataclasses import dataclass


@dataclass
class ApiException(Exception):
    message: str
