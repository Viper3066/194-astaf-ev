from flask import Flask, request, render_template, flash
from datetime import datetime
from test2 import (
    add_division, delete_division, add_match, delete_match,
    get_all_divisions, get_all_matches, get_matches_by_date
)

app = Flask(__name__)
app.secret_key = "KEY"  # Секретный ключ для использования flash-сообщений

# Главная страница
@app.route("/", methods=["GET", "POST"])
def index():
    search_results = []  # Результаты поиска
    if request.method == "POST":
        try:
            # Обработка добавления дивизиона
            if "add_division" in request.form:
                division = request.form.get("division")
                name = request.form.get("name")
                country = request.form.get("country")
                try:
                    add_division(division, name, country)
                    flash(f"Дивизион '{name}' успешно добавлен!", "success")
                except ValueError as e:
                    flash(f"Ошибка при добавлении дивизиона: {e}", "error")

            # Обработка удаления дивизиона
            elif "delete_division" in request.form:
                division = request.form.get("division")
                try:
                    delete_division(division)
                    flash(f"Дивизион '{division}' успешно удален!", "success")
                except Exception as e:
                    flash(f"Ошибка при удалении дивизиона: {e}", "error")

            # Обработка добавления матча
            elif "add_match" in request.form:
                Div = request.form.get("Div")
                Date = request.form.get("Date")
                HomeTeam = request.form.get("HomeTeam")
                AwayTeam = request.form.get("AwayTeam")
                FTHG = float(request.form.get("FTHG"))
                FTAG = float(request.form.get("FTAG"))
                FTR = request.form.get("FTR")
                season = int(request.form.get("season"))
                try:
                    add_match(Div, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, season)
                    flash(f"Матч '{HomeTeam} vs {AwayTeam}' успешно добавлен!", "success")
                except Exception as e:
                    flash(f"Ошибка при добавлении матча: {e}", "error")

            # Обработка удаления матча
            elif "delete_match" in request.form:
                Div = request.form.get("Div")
                Date = request.form.get("Date")
                HomeTeam = request.form.get("HomeTeam")
                AwayTeam = request.form.get("AwayTeam")
                try:
                    delete_match(Div, Date, HomeTeam, AwayTeam)
                    flash(f"Матч '{HomeTeam} vs {AwayTeam}' успешно удален!", "success")
                except Exception as e:
                    flash(f"Ошибка при удалении матча: {e}", "error")

            # Обработка поиска матчей по дате
            elif "search_match_by_date" in request.form:
                search_date = request.form.get("search_date")
                try:
                    search_results = get_matches_by_date(search_date)
                    if not search_results:
                        flash(f"Матчи на дату {search_date} не найдены.", "info")
                except Exception as e:
                    flash(f"Ошибка при поиске матчей: {e}", "error")

        except Exception as e:
            flash(f"Произошла непредвиденная ошибка: {e}", "error")

    # Получение всех дивизионов и матчей
    try:
        divisions = get_all_divisions()
        matches = get_all_matches(limit=50)
    except Exception as e:
        flash(f"Ошибка при загрузке данных: {e}", "error")
        divisions = []
        matches = []

    return render_template("index.html", divisions=divisions, matches=matches, search_results=search_results)

if __name__ == "__main__":
    app.run(debug=True)