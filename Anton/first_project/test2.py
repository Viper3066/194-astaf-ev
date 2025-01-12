from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test import*
from datetime import datetime
import re

def validate_input(*args):
    """
    Проверяет входные данные на наличие потенциально опасных символов.
    """
    for arg in args:
        if not isinstance(arg, str):
            continue
        if re.search(r"[\'\";\\]", arg):
            raise ValueError("Недопустимые символы в входных данных.")

def add_division(division, name, country):
    try:
        validate_input(division, name, country)
        if not division or not name or not country:
            raise ValueError("Все поля должны быть заполнены.")
        new_division = Divisions(division=division, name=name, country=country)
        session.add(new_division)
        session.commit()
        return new_division.division
    except Exception as e:
        session.rollback()  # Откат транзакции в случае ошибки
        print(f"Ошибка при добавлении дивизиона: {e}")
        raise

def add_match(Div, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, season):
    try:
        validate_input(Div, Date, HomeTeam, AwayTeam, FTR, str(season))
        date_obj = datetime.strptime(Date, '%Y-%m-%d').date()
        new_match = Matchs(Div=Div, Date=date_obj, HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG, FTAG=FTAG, FTR=FTR, season=season)
        session.add(new_match)
        session.commit()
        print(f"Матч '{HomeTeam} vs {AwayTeam}' добавлен с Div: {new_match.Div}, Date: {new_match.Date}")
        return (new_match.Div, new_match.Date, new_match.HomeTeam, new_match.AwayTeam)
    except Exception as e:
        session.rollback()  # Откат транзакции в случае ошибки
        print(f"Ошибка при добавлении матча: {e}")
        raise

def get_division_by_division(division):
    try:
        division = session.get(Divisions, division)
        if division:
            print(f"Дивизион: {division.name}, Страна: {division.country}")
            return division
        else:
            print(f"Дивизион не найден.")
            return None
    except Exception as e:
        print(f"Ошибка при получении дивизиона: {e}")
        raise

def get_all_divisions():
    try:
        divisions_list = session.query(Divisions).all()
        if divisions_list:
            for division in divisions_list:
                if division is not None:
                    print(f"Дивизион: {division.division}, Название: {division.name}, Страна: {division.country}")
                else:
                    print("Пропуск дивизиона с None.")
        else:
            print("Дивизионов не найдено.")
        return divisions_list
    except Exception as e:
        print(f"Ошибка при получении всех дивизионов: {e}")
        raise

def get_matches_by_division(division):
    try:
        matches = session.query(Matchs).filter_by(Div=division).all()
        if matches:
            print(f"Матчи в дивизионе '{division}':")
            for match in matches:
                print(f"- {match.HomeTeam} vs {match.AwayTeam} on {match.Date}")
        else:
            print(f"Матчи в дивизионе '{division}' не найдены.")
        return matches
    except Exception as e:
        print(f"Ошибка при получении матчей по дивизиону: {e}")
        raise

def get_all_matches(limit=50):
    try:
        matches_list = session.query(Matchs).limit(limit).all()
        if matches_list:
            for match in matches_list:
                if match is not None:
                    print(f"Матч: Div={match.Div}, Date={match.Date}, HomeTeam={match.HomeTeam}, AwayTeam={match.AwayTeam}")
                else:
                    print("Пропуск матча с None.")
        else:
            print("Матчей не найдено.")
        return matches_list
    except Exception as e:
        print(f"Ошибка при получении всех матчей: {e}")
        raise

def update_division_name(division, new_name):
    try:
        validate_input(division, new_name)
        division = session.get(Divisions, division)
        if division:
            division.name = new_name
            session.commit()
            print(f"Дивизион с ID {division} обновлен на '{new_name}'")
            return division
        else:
            print(f"Дивизион с ID {division} не найден.")
            return None
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении названия дивизиона: {e}")
        raise

def update_match_date(Div, Date, HomeTeam, AwayTeam, new_date):
    try:
        validate_input(Div, Date, HomeTeam, AwayTeam, new_date)
        date_obj = datetime.strptime(new_date, '%Y-%m-%d').date()
        match = session.query(Matchs).filter_by(Div=Div, Date=Date, HomeTeam=HomeTeam, AwayTeam=AwayTeam).first()
        if match:
            match.Date = date_obj
            session.commit()
            print(f"Матч с Div {Div}, Date {Date}, HomeTeam {HomeTeam}, AwayTeam {AwayTeam} обновлен на дату '{new_date}'")
            return match
        else:
            print(f"Матч с Div {Div}, Date {Date}, HomeTeam {HomeTeam}, AwayTeam {AwayTeam} не найден.")
            return None
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении даты матча: {e}")
        raise

def delete_division(division):
    try:
        validate_input(division)
        division = session.get(Divisions, division)
        if division:
            session.delete(division)
            session.commit()
            print(f"Дивизион удален.")
        else:
            print(f"Дивизион не найден.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении дивизиона: {e}")
        raise

def delete_match(Div, Date, HomeTeam, AwayTeam):
    try:
        validate_input(Div, Date, HomeTeam, AwayTeam)
        match = session.query(Matchs).filter_by(Div=Div, Date=Date, HomeTeam=HomeTeam, AwayTeam=AwayTeam).first()
        if match:
            session.delete(match)
            session.commit()
            print(f"Матч с Div {Div}, Date {Date}, HomeTeam {HomeTeam}, AwayTeam {AwayTeam} удален.")
        else:
            print(f"Матч с Div {Div}, Date {Date}, HomeTeam {HomeTeam}, AwayTeam {AwayTeam} не найден.")
            return None
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении матча: {e}")
        raise

def get_matches_by_date(date):
    try:
        validate_input(date)
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        matches = session.query(Matchs).filter_by(Date=date_obj).all()
        if matches:
            print(f"Матчи на дату {date}:")
            for match in matches:
                print(f"- {match.HomeTeam} vs {match.AwayTeam} в дивизионе {match.Div}")
        else:
            print(f"Матчи на дату {date} не найдены.")
        return matches
    except Exception as e:
        print(f"Ошибка при получении матчей по дате: {e}")
        raise

# Тест
if __name__ == "__main__":
    try:
        # Создание
        division_id = add_division("L2", "Дивизион Ла Лига", "Италия")
        match_id = add_match("L2", "2020-08-08", "Club Brugge", "Charleroi", 0.0, 1.0, "A", 2021)

        # Чтение
        get_matches_by_division("L2")

        # Обновление
        update_division_name("L2", "Дивизион 1A")
        update_match_date("L2", "2020-08-08", "Club Brugge", "Charleroi", "2020-08-09")
        get_division_by_division("L2")
        get_matches_by_division("L2")

        # Удаление
        delete_match("L2", "2020-08-09", "Club Brugge", "Charleroi")
        delete_division("L2")

        # Получение всех матчей (первые 50)
        all_matches = get_all_matches()
        for match in all_matches:
            print(f"Матч: {match.HomeTeam} vs {match.AwayTeam} на {match.Date}")
    except Exception as e:
        print(f"Ошибка в основном блоке: {e}")