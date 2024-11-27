from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class divisions(Base):
    __tablename__ = 'divisions'
    division = Column(String, primary_key=True)
    Name = Column(String)
    Country = Column(String)

class matchs(Base):
    __tablename__ = 'matchs'
    Div = Column(String, primary_key=True)  # Используем Div как первичный ключ
    Date = Column(Date)
    HomeTeam = Column(String)
    AwayTeam = Column(String)
    FTHG = Column(Float)
    FTAG = Column(Float)
    FTR = Column(String)
    season = Column(Integer)

def setup_database(database_path="sqlite:///european_database.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)  # Создаем таблицы, если они не существуют
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

# Основной код
engine = setup_database()
session = create_session(engine)

new_division = divisions(division="NewDivision", Name="New divisions", Country="Country")
session.add(new_division)
session.commit()
print(f"Added division with ID: {new_division.division}")

# Получить все матчи, связанные с этим дивизионом
division = session.query(divisions).filter_by(Name="New divisions").first()
if division:
    print(f"Matches in {division.Name}: {[match.HomeTeam for match in session.query(matchs).filter_by(Div=division.division)]}")

# Удалить матч
match = session.query(matchs).filter_by(HomeTeam="Some Team").first()
if match:
    session.delete(match)
    session.commit()
    print("Match deleted.")