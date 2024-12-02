from secrets import token_urlsafe
from peewee import SqliteDatabase, Model, CharField


db = SqliteDatabase('data.db', pragmas={'journal_mode': 'wal'}, check_same_thread=False)

    
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(unique=True)
    token = CharField(default=token_urlsafe)


if __name__ == "__main__":
    db.connect()
    db.create_tables(BaseModel.__subclasses__())
