from pydantic import BaseModel


class ReceiptModel(BaseModel):
    date: str
    amount: float
    store_name: str
    description: str
    category: str
    province: str
    subtotal_before_tax: float | None = None
    gst_amount: float | None = None
    pst_qst_amount: float | None = None
    tip_amount: float | None = None
    # budget: str
