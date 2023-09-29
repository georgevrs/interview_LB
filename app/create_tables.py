# app/create_tables.py
from .models import metadata, engine

metadata.create_all(engine)
