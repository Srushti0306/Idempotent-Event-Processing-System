from app.db.database import Base, engine
from app.models.event import Event

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")