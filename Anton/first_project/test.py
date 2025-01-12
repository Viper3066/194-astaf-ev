from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Divisions(Base):
    __tablename__ = 'divisions'
    division = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # Связь один ко многим с таблицей Matchs
    matches = relationship('Matchs', back_populates='division')

class Matchs(Base):
    __tablename__ = 'matchs'
    Div = Column(String, ForeignKey('divisions.division'), primary_key=True)
    Date = Column(Date, primary_key=True)
    HomeTeam = Column(String, primary_key=True)
    AwayTeam = Column(String, primary_key=True)
    FTHG = Column(Float, nullable=False)
    FTAG = Column(Float, nullable=False)
    FTR = Column(String, nullable=False)
    season = Column(Integer, nullable=False)

    # Связь с таблицей Divisions
    division = relationship('Divisions', back_populates='matches')

def setup_database(database_path="sqlite:///european_database.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

# Инициализация базы данных
engine = setup_database()
session = create_session(engine)



