from datetime import datetime
from uuid import UUID
from descriptors import IdAttribute, PriorityAttribute, StatusAttribute
from errors import ValidationError


class Task:
    """

    """

    id:UUID = IdAttribute()
    priority:int = PriorityAttribute()
    status:str = StatusAttribute()

    def __init__(self, id:UUID, description:str, priority:int):
        """

        """
        self.id = id
        self._description = description
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
        raise ValidationError

    @property
    def is_ready(self) -> bool:
        """

        """
        return self.status=='ready'

