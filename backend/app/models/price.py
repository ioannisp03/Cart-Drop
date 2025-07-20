from sqlalchemy import Column, Integer, Numeric, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    
    product = relationship("Product", back_populates="prices")