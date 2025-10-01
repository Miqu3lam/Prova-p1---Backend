from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CategoryCreated:
    category_id: str
    name: str
    description: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class CategoryUpdated:
    category_id: str
    changes: dict
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class CategoryActivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class CategoryDeactivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)