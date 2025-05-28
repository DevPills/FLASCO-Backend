# base.py
from sqlalchemy.orm import registry

table_registry = registry()
Base = table_registry.generate_base()
