from peewee import (SqliteDatabase, Model, CharField, IntegerField, DateTimeField,
                    SmallIntegerField, ForeignKeyField)

db = SqliteDatabase('data.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    password = CharField(max_length=32)

    class Meta:
        db_table = 'users'


class Product(BaseModel):
    title = CharField(max_length=128)
    price = IntegerField()

    class Meta:
        db_table = 'products'


class Order(BaseModel):
    user = ForeignKeyField(User, backref='orders', on_delete='CASCADE')
    product = ForeignKeyField(Product, backref='orders', on_delete='CASCADE')
    quantity = SmallIntegerField()
    total_price = IntegerField()
    created_date = DateTimeField()

    class Meta:
        db_table = 'orders'
