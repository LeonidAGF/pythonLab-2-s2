from datetime import datetime
from typing import Any
from src.descriptors import IdAttribute, PriorityAttribute, StatusAttribute
from src.errors import ValidationError


class Task:
    """

    """

    id:int = IdAttribute()
    priority:int = PriorityAttribute()
    status:str = StatusAttribute()

    def __init__(self, id:int, description:str,payload:dict[str, Any], priority:int):
        """

        """
        if not isinstance(id, int):
            raise ValidationError
        if not isinstance(description, str):
            raise ValidationError
        if not isinstance(payload, dict):
            raise ValidationError
        if not isinstance(priority, int) or (priority!= 1 and priority !=2):
            raise ValidationError

        self.id = id
        self.description = description
        self.payload = payload
        self.priority = priority
        self.status = 'in processing'
        self.create_time = str(datetime.now())

    @property
    def description(self):
        """

        """
        return self._description

    @description.setter
    def description(self, value):
        """

        """
        if isinstance(value, str):
            self._description = value
        else:
            raise ValidationError

    @property
    def payload(self):
        """

        """
        return self._payload

    @payload.setter
    def payload(self, value):
        """

        """
        if isinstance(value, dict):
            self._payload = value
        else:
            raise ValidationError

    @property
    def is_ready(self) -> bool:
        """

        """
        return self.status=='ready'

    def __repr__(self):
        return "id = " + str(self.id) + ", description = " + self.description + ", payload = " + str(self.payload) + ", priority = " + str(self.priority) + ", status = " + self.status