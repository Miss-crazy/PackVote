from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from PackVote.config import DATABASE_URL

def make_engine() -> Engine:
    if not DATABASE_URL:
        raise RuntimeError("Set DATABASE_URL")
    return create_engine(DATABASE_URL , pool_pre_ping=True , pool_recycle = 3600)
