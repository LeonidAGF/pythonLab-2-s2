from uuid import UUID

from errors import ValidationError


class IdAttribute:
    """

    """
    def __set_name__(self, owner, name):
        """

        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """

        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value:UUID):
        """

        """
        if isinstance(value, UUID):
            setattr(instance, self.name, value)
        else:
            raise ValidationError

class PriorityAttribute:
    """

    """
    def __set_name__(self, owner, name):
        """

        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """

        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value:int):
        """

        """
        if isinstance(value, int) and (value==1 or value==2):
            setattr(instance, self.name, value)
        else:
            raise ValidationError


class StatusAttribute:
    """

    """
    def __set_name__(self, owner, name):
        """

        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """

        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value:str):
        """

        """
        if isinstance(value, str) and (value=='ready' or value=='in processing'):
            setattr(instance, self.name, value)
        else:
            raise ValidationError