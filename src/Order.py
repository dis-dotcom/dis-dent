from uuid import uuid4 as guid
from datetime import datetime


class Order:
    def __init__(self, id=None, created_at=None):
        if id is None:
            id = guid()
        if created_at is None:
            created_at = datetime.now()
        self.id = id
        self.created_at = created_at
