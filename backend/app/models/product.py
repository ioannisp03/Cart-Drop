from sqlalchemy import Column, Integer, String, Datetime, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    name = Column(String)
    current_price = Column(Numeric(10, 2))
    last_scraped = Column(Datetime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    tracked_products = relationship("TrackedProduct", back_populates="product")
    prices = relationship("Price", back_populates="product")
