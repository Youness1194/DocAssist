import os
import sys

from app.core.db import SessionLocal
from app.core.security import hash_password
from app.models import Role, User
from sqlalchemy import select

email = os.environ.get("ADMIN_EMAIL")
password = os.environ.get("ADMIN_PASSWORD")
if not email or not password:
    sys.exit("Set ADMIN_EMAIL and ADMIN_PASSWORD")

with SessionLocal() as db:
    user = db.scalar(select(User).where(User.email == email.lower()))
    if user:
        user.role = Role.ADMIN
    else:
        user = User(
            email=email.lower(), password_hash=hash_password(password), role=Role.ADMIN
        )
        db.add(user)
    db.commit()
    print("Admin ready")
