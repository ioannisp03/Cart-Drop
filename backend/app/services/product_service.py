from sqlalchemy.orm import Session
from ..models.product import Product
from ..models.tracked_product import TrackedProduct


def get_all_products_by_clerk_id(db: Session, clerk_id: str):
    return (
        db.query(Product)
        .join(TrackedProduct)
        .filter(TrackedProduct.clerk_user_id == clerk_id)
        .all()
    )
    
def create_new_product(db:Session, )
