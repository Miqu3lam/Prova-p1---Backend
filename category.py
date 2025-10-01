from dataclasses import dataclass, field
from datetime import datetime
import uuid
from typing import List, Dict, Any

from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)


@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    events: List[Any] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.events.append(CategoryCreated(category_id=self.id, name=self.name, description=self.description))

    def update(self, name: str = None, description: str = None):
        changes = {}
        if name and name != self.name:
            changes["name"] = (self.name, name)
            self.name = name
        if description and description != self.description:
            changes["description"] = (self.description, description)
            self.description = description
        if changes:
            self.events.append(CategoryUpdated(category_id=self.id, changes=changes))

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.events.append(CategoryActivated(category_id=self.id))

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.events.append(CategoryDeactivated(category_id=self.id))

    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Category":
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            is_active=data["is_active"]
        )