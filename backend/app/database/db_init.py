from app.database.db import Base, engine
# Import all models as engine needs these imported to work
from app.models import product, tracked_product, user, price, notification # noqa: F401

if __name__ == "__main__":
    print("Creating all tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")