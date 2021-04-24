from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class InvoiceModel(Base):
    """Invoice data model. This corresponds to the invoice model in covetrus"""
    __tablename__ = "invoice_table"
    # __table_args__ = {"schema": "invoice"}
    # TODO: need to run this by Terry

    id = Column(Integer, primary_key=True, nullable=False)
    invoice_id = Column(Integer, nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    client_id = Column(String(100), nullable=False)
    client_pms_id = Column(String(100), nullable=False)
    entered_by_id = Column(String(100), nullable=False)
    invoice_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, nullable=False)
    adjustment_amount = Column(Float, nullable=False)
    total_tax_amount = Column(Float, nullable=False)
    pms_status = Column(String(100), nullable=False)
    is_complete = Column(Boolean, nullable=False)
    is_paid = Column(Boolean, nullable=False)
    site_id = Column(String(100), nullable=False)
    api_created_date = Column(DateTime, nullable=False)
    api_last_change_date = Column(DateTime, nullable=False)
    api_removed_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Invoice model {}>'.format(self.id)


class InvoiceLineItemModel(Base):
    """Invoice line item data model. This corresponds to a "transaction" in Covetrus. This should also map directly
    to a claim line item """
    __tablename__ = "invoice_line_item_table"
    # __table_args__ = {"schema": "invoice_line_item"}
    # TODO: need to run this by Terry

    id = Column(Integer, primary_key=True, nullable=False)
    line_item_id = Column(Integer, nullable=False)
    line_item_type = Column(String(100), nullable=False)
    client_id = Column(String(100), nullable=False)
    client_pms_id = Column(String(100), nullable=False)
    patient_id = Column(String(100), nullable=False)
    patient_pims_id = Column(String(100), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    # sequence needs to go here

    entered_by_id = Column(String(100), nullable=False)
    invoice_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, nullable=False)
    adjustment_amount = Column(Float, nullable=False)
    total_tax_amount = Column(Float, nullable=False)
    pms_status = Column(String(100), nullable=False)
    is_complete = Column(Boolean, nullable=False)
    is_paid = Column(Boolean, nullable=False)
    site_id = Column(String(100), nullable=False)
    api_created_date = Column(DateTime, nullable=False)
    api_last_change_date = Column(DateTime, nullable=False)
    api_removed_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Invoice line item model {}>'.format(self.id)

# claims
# claim line item
# patient
# client
# clinic
# corporate brand
# insurance brand
# insurance company
# underwriter
