from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab1 import setup_database, create_session, divisions, matchs  # Подключаем модели из ORM
from datetime import datetime

# Инициализация базы данных
engine = setup_database("sqlite:///european_database.sqlite")
session = create_session(engine)

# CREATE (Создание)
def add_division(division, name, country):
    new_division = divisions(division=division, Name=name, Country=country)
    session.add(new_division)
    session.commit()
    print(f"Division '{name}' added with ID: {new_division.division}")
    return new_division.division

def add_match(Div, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, season):
    # Преобразуем строку в объект datetime.date
    date_obj = datetime.strptime(Date, '%Y-%m-%d').date()
    new_match = matchs(Div=Div, Date=date_obj, HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG, FTAG=FTAG, FTR=FTR, season=season)
    session.add(new_match)
    session.commit()
    print(f"Match '{HomeTeam} vs {AwayTeam}' added with Div: {new_match.Div}")
    return new_match.Div

# READ (Чтение)
def get_division_by_id(division_id):
    division = session.query(divisions).filter_by(division=division_id).first()
    if division:
        print(f"Division: {division.Name}, Country: {division.Country}")
        return division
    else:
        print(f"Division with ID {division_id} not found.")
        return None

def get_all_divisions():
    divisions_list = session.query(divisions).all()
    if divisions_list:
        for division in divisions_list:
            print(f"Division ID: {division.division}, Name: {division.Name}, Country: {division.Country}")
    else:
        print("No divisions found.")
    return divisions_list

def get_matches_by_division(division_id):
    matches = session.query(matchs).filter_by(Div=division_id).all()
    print(f"Matches in Division '{division_id}':")
    for match in matches:
        print(f"- {match.HomeTeam} vs {match.AwayTeam} on {match.Date}")
    return matches

# UPDATE (Обновление)
def update_division_name(division_id, new_name):
    division = session.query(divisions).filter_by(division=division_id).first()
    if division:
        division.Name = new_name
        session.commit()
        print(f"Division ID {division_id} updated to '{new_name}'")
        return division
    else:
        print(f"Division with ID {division_id} not found.")
        return None

def update_match_date(match_div, new_date):
    # Преобразуем строку в объект datetime.date
    date_obj = datetime.strptime(new_date, '%Y-%m-%d').date()
    match = session.query(matchs).filter_by(Div=match_div).first()
    if match:
        match.Date = date_obj
        session.commit()
        print(f"Match with Div {match_div} updated to date '{new_date}'")
        return match
    else:
        print(f"Match with Div {match_div} not found.")
        return None

# DELETE (Удаление)
def delete_division(division_id):
    division = session.query(divisions).filter_by(division=division_id).first()
    if division:
        session.delete(division)
        session.commit()
        print(f"Division ID {division_id} deleted.")
    else:
        print(f"Division with ID {division_id} not found.")

def delete_match(match_div):
    match = session.query(matchs).filter_by(Div=match_div).first()
    if match:
        session.delete(match)
        session.commit()
        print(f"Match with Div {match_div} deleted.")
    else:
        print(f"Match with Div {match_div} not found.")

# Примеры использования
if __name__ == "__main__":
    # Создание
    division_id = add_division("B1", "Division 1A", "Belgium")
    match_div = add_match("B1", "2020-08-08", "Club Brugge", "Charleroi", 0.0, 1.0, "A", 2021)

    # Чтение
    get_division_by_id(division_id)
    get_all_divisions()
    get_matches_by_division("B1")

    # Обновление
    update_division_name(division_id, "Updated Division 1A")
    update_match_date(match_div, "2020-08-09")

    # Удаление
    delete_match(match_div)
    delete_division(division_id)