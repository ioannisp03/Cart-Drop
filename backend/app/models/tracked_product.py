from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class TrackedProduct(Base):
    __tablename__ = "tracked_products"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    clerk_user_id = Column(String, nullable=False)
    target_price = Column(Numeric(10, 2))  # User's desired price
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Create composite index for efficient queries
    __table_args__ = (Index("ix_user_product", "clerk_user_id", "product_id"),)
