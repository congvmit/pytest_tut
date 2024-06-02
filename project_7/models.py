from sqlalchemy import Column, Float, Integer, String

from db import Base


class Item(Base):
    __tablename__ = "items"
    # # https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table.params.extend_existing
    # # Pytest Problem: sqlalchemy.exc.InvalidRequestError: Table 'items' is already defined for this MetaData instance.
    # __table_args__ = {
    #     # "keep_existing": True,
    #     # "extend_existing": True
    # }
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
