from datetime import datetime
import peewee

from core.db import db


class Post(peewee.Model):
    name = peewee.CharField(max_length=50)
    title = peewee.CharField(max_length=50)
    description = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db
