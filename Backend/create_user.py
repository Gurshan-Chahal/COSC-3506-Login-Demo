from app.database import SessionLocal, engine
from app.models import User, Base
from app.security import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

email = "student@example.com"

existing_user = db.query(User).filter(User.email == email).first()

if existing_user:
    print("User already exists.")
else:
    new_user = User(
        email=email,
        password_hash=hash_password("Password123"),
        is_active=True
    )

    db.add(new_user)
    db.commit()

    print("Sample user created successfully!")

db.close()