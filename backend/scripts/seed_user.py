import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import SessionLocal
from models.user import User


from database.database import SessionLocal
from models.user import User

db = SessionLocal()
user = User(username="alice", hashed_password="secret", role="admin")
db.add(user)
db.commit()
db.close()
