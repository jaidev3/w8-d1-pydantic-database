from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, field_validator, model_validator, computed_field, Field
from enum import Enum
from typing import List, Optional
from decimal import Decimal
import re
from itertools import count
import uvicorn

class FoodCategory(str, Enum):
    APPETIZER = "appetizer"
    MAIN_COURSE = "main_course"
    DESSERT = "dessert"
    BEVERAGE = "beverage"
    SALAD = "salad"

class FoodItemBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    category: FoodCategory
    price: Decimal = Field(..., gt=0)
    is_available: bool = True
    preparation_time: int = Field(..., ge=1, le=120)
    ingredients: List[str] = Field(..., min_length=1)
    calories: Optional[int] = Field(None, gt=0)
    is_vegetarian: bool = False
    is_spicy: bool = False

    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z ]+$', v):
            raise ValueError('Name should contain only letters and spaces')
        return v

    @field_validator('price')
    @classmethod
    def validate_price(cls, v: Decimal) -> Decimal:
        if v.quantize(Decimal('0.01')) != v:
            raise ValueError('Price must have at most 2 decimal places')
        if v < Decimal('1.00') or v > Decimal('100.00'):
            raise ValueError('Price must be between $1.00 and $100.00')
        return v

    @model_validator(mode='after')
    def custom_validations(self) -> 'FoodItemBase':
        if self.category in [FoodCategory.DESSERT, FoodCategory.BEVERAGE] and self.is_spicy:
            raise ValueError('Desserts and beverages cannot be marked as spicy')
        if self.calories is not None and self.is_vegetarian and self.calories >= 800:
            raise ValueError('Vegetarian items should have calories < 800')
        if self.category == FoodCategory.BEVERAGE and self.preparation_time > 10:
            raise ValueError('Preparation time for beverages should be ≤ 10 minutes')
        return self

class FoodItem(FoodItemBase):
    id: int = Field(default_factory=lambda: next(id_generator))

    @computed_field
    @property
    def price_category(self) -> str:
        if self.price < Decimal('10'):
            return "Budget"
        elif self.price <= Decimal('25'):
            return "Mid-range"
        else:
            return "Premium"

    @computed_field
    @property
    def dietary_info(self) -> List[str]:
        info = []
        if self.is_vegetarian:
            info.append("Vegetarian")
        if self.is_spicy:
            info.append("Spicy")
        return info


# ////////////////////////////////////////////

app = FastAPI()
menu_db: dict[int, FoodItem] = {}
id_generator = count(1)

# api endpoints

@app.get("/menu", response_model=List[FoodItem])
def get_menu():
    return list(menu_db.values())

@app.get("/menu/{item_id}", response_model=FoodItem)
def get_item(item_id: int = Path(..., ge=1)):
    if item_id not in menu_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return menu_db[item_id]

@app.post("/menu", response_model=FoodItem)
def add_item(item: FoodItemBase):
    new_id = next(id_generator)
    new_item = FoodItem(id=new_id, **item.model_dump())
    menu_db[new_id] = new_item
    return new_item

@app.put("/menu/{item_id}", response_model=FoodItem)
def update_item(item_id: int = Path(..., ge=1), item: FoodItemBase = None):
    if item_id not in menu_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = FoodItem(id=item_id, **item.model_dump())
    menu_db[item_id] = updated_item
    return updated_item

@app.delete("/menu/{item_id}")
def delete_item(item_id: int = Path(..., ge=1)):
    if item_id not in menu_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del menu_db[item_id]
    return {"message": "Item deleted"}

@app.get("/menu/category/{category}", response_model=List[FoodItem])
def get_by_category(category: FoodCategory):
    items = [item for item in menu_db.values() if item.category == category]
    return items