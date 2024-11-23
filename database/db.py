from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings
    

engine = create_engine(
    f"{settings.DATABASE_URL}/{settings.DATABASE_NAME}",
    connect_args={
        "check_same_thread": False
    },  # check_same_thread setting only applicable when you choose to use sqlite
)  # sqlite:///./data/<database-name.db>


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() :
    db: Session = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
 