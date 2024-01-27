from utils import generate_date, generate_password
from models import db, User, Product, Order
from config import *
import random
import logging


# Create and Config logger
logging.basicConfig(
    format="%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]",
    datefmt="%H:%M:%S",
    encoding="utf-8",
    level=logging.WARNING
)
logger = logging.getLogger(__name__)


class CreateUser:
    def __init__(self):
        self.first_name = random.choice(FIRST_NAMES)
        self.last_name = random.choice(LAST_NAMES)
        self.password = generate_password()

    def create(self) -> User:
        created_user = User.create(first_name=self.first_name, last_name=self.last_name, password=self.password)
        created_user.save()
        return created_user


class CreateProduct:
    def __init__(self):
        self.title = random.choice(TITLES)
        self.price = random.choice(PRICES)

    def create(self) -> Product:
        created_product = Product.create(title=self.title, price=self.price)
        created_product.save()
        return created_product


class CreateOrder:
    def __init__(self, user: User, product: Product):
        self.user = user
        self.product = product
        self.quantity = random.randint(1, 10)
        self.total_price = self.quantity * self.product.price
        self.created_date = generate_date()

    def create(self) -> Order:
        order = Order.create(user=self.user, product=self.product, quantity=self.quantity,
                             total_price=self.total_price, created_date=self.created_date)
        order.save()
        return order


if __name__ == '__main__':
    logger.warning('Creating tables: "users", "products", "orders"')
    db.create_tables([User, Product, Order])

    logger.warning(f'Creating {NUMBER_OF_USERS} users...')
    users = [CreateUser().create() for _ in range(NUMBER_OF_USERS)]

    logger.warning(f'Creating {NUMBER_OF_PRODUCTS} products...')
    products = [CreateProduct().create() for _ in range(NUMBER_OF_PRODUCTS)]

    for i in range(NUMBER_OF_ORDERS):
        random_user = random.choice(users)
        random_product = random.choice(products)
        logger.warning(f'Creating {i+1}/{NUMBER_OF_ORDERS} orders with user: {random_user}, product: {random_product}')
        CreateOrder(random_user, random_product).create()

    logger.warning('Closing connection...')
    db.close()
    logger.warning('Done!')
