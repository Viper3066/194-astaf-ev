import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


from test2 import (
    add_division, add_match, get_all_divisions, get_matches_by_division,
    update_division_name, update_match_date, delete_division, delete_match,
    get_matches_by_date
)


session = None

def show_error(message):
    messagebox.showerror("Ошибка", message)

def show_success(message):
    messagebox.showinfo("Успех", message)


def load_divisions():
    divisions = get_all_divisions()
    for row in tree_divisions.get_children():
        tree_divisions.delete(row)
    for division in divisions:
        if division is not None:  # Проверка на None
            tree_divisions.insert("", "end", values=(division.division, division.name, division.country))

def add_division_gui():
    division = simpledialog.askstring("Добавить дивизион", "Введите ID дивизиона:")
    name = simpledialog.askstring("Добавить дивизион", "Введите название дивизиона:")
    country = simpledialog.askstring("Добавить дивизион", "Введите страну:")
    if division and name and country:
        try:
            add_division(division, name, country)
            show_success(f"Дивизион '{name}' добавлен.")
            load_divisions()
        except SQLAlchemyError as e:
            show_error(f"Ошибка при добавлении дивизиона: {e}")

def update_division_gui():
    selected_item = tree_divisions.selection()
    if not selected_item:
        show_error("Выберите дивизион для обновления.")
        return
    division_id = tree_divisions.item(selected_item)["values"][0]
    new_name = simpledialog.askstring("Обновить дивизион", "Введите новое название дивизиона:")
    if new_name:
        try:
            update_division_name(division_id, new_name)
            show_success(f"Дивизион обновлен на '{new_name}'.")
            load_divisions()
        except SQLAlchemyError as e:
            show_error(f"Ошибка при обновлении дивизиона: {e}")

def delete_division_gui():
    selected_item = tree_divisions.selection()
    if not selected_item:
        show_error("Выберите дивизион для удаления.")
        return
    division_id = tree_divisions.item(selected_item)["values"][0]
    try:
        delete_division(division_id)
        show_success(f"Дивизион удален.")
        load_divisions()
    except SQLAlchemyError as e:
        show_error(f"Ошибка при удалении дивизиона: {e}")

# Функции для работы с Matchs
def load_matches(division_id):
    matches = get_matches_by_division(division_id)
    for row in tree_matches.get_children():
        tree_matches.delete(row)
    for match in matches:
        tree_matches.insert("", "end", values=(match.Div, match.Date, match.HomeTeam, match.AwayTeam, match.FTHG, match.FTAG, match.FTR, match.season))

def add_match_gui():
    division = simpledialog.askstring("Добавить матч", "Введите ID дивизиона:")
    date = simpledialog.askstring("Добавить матч", "Введите дату матча (YYYY-MM-DD):")
    home_team = simpledialog.askstring("Добавить матч", "Введите домашнюю команду:")
    away_team = simpledialog.askstring("Добавить матч", "Введите гостевую команду:")
    fthg = simpledialog.askfloat("Добавить матч", "Введите голы домашней команды:")
    ftag = simpledialog.askfloat("Добавить матч", "Введите голы гостевой команды:")
    ftr = simpledialog.askstring("Добавить матч", "Введите результат (H, A, D):")
    season = simpledialog.askinteger("Добавить матч", "Введите сезон:")
    if division and date and home_team and away_team and fthg is not None and ftag is not None and ftr and season:
        try:
            add_match(division, date, home_team, away_team, fthg, ftag, ftr, season)
            show_success(f"Матч '{home_team} vs {away_team}' добавлен.")
            load_matches(division)
        except SQLAlchemyError as e:
            show_error(f"Ошибка при добавлении матча: {e}")

def update_match_gui():
    selected_item = tree_matches.selection()
    if not selected_item:
        show_error("Выберите матч для обновления.")
        return
    match_data = tree_matches.item(selected_item)["values"]
    new_date = simpledialog.askstring("Обновить матч", "Введите новую дату матча (YYYY-MM-DD):")
    if new_date:
        try:
            update_match_date(match_data[0], match_data[1], match_data[2], match_data[3], new_date)
            show_success(f"Матч обновлен на дату '{new_date}'.")
            load_matches(match_data[0])
        except SQLAlchemyError as e:
            show_error(f"Ошибка при обновлении матча: {e}")

def delete_match_gui():
    selected_item = tree_matches.selection()
    if not selected_item:
        show_error("Выберите матч для удаления.")
        return
    match_data = tree_matches.item(selected_item)["values"]
    try:
        delete_match(match_data[0], match_data[1], match_data[2], match_data[3])
        show_success(f"Матч удален.")
        load_matches(match_data[0])
    except SQLAlchemyError as e:
        show_error(f"Ошибка при удалении матча: {e}")

# Функция для поиска матчей по дате
def search_matches_by_date_gui():
    date = simpledialog.askstring("Поиск матчей по дате", "Введите дату (YYYY-MM-DD):")
    if date:
        try:
            matches = get_matches_by_date(date)
            for row in tree_matches.get_children():
                tree_matches.delete(row)
            if matches:
                for match in matches:
                    tree_matches.insert("", "end", values=(match.Div, match.Date, match.HomeTeam, match.AwayTeam, match.FTHG, match.FTAG, match.FTR, match.season))
            else:
                show_success(f"Матчи на дату {date} не найдены.")
        except SQLAlchemyError as e:
            show_error(f"Ошибка при поиске матчей: {e}")

# Создание главного окна
root = tk.Tk()
root.title("ORM и CRUD с Tkinter")

# Вкладки
tab_control = ttk.Notebook(root)

# Вкладка Divisions
tab_divisions = ttk.Frame(tab_control)
tab_control.add(tab_divisions, text="Дивизионы")

# Вкладка Matchs
tab_matches = ttk.Frame(tab_control)
tab_control.add(tab_matches, text="Матчи")

# Настройка вкладки Divisions
tree_divisions = ttk.Treeview(tab_divisions, columns=("ID", "Название", "Страна"), show="headings")
tree_divisions.heading("ID", text="ID")
tree_divisions.heading("Название", text="Название")
tree_divisions.heading("Страна", text="Страна")
tree_divisions.pack(fill="both", expand=True)

btn_add_division = ttk.Button(tab_divisions, text="Добавить дивизион", command=add_division_gui)
btn_add_division.pack(pady=5)

btn_update_division = ttk.Button(tab_divisions, text="Обновить дивизион", command=update_division_gui)
btn_update_division.pack(pady=5)

btn_delete_division = ttk.Button(tab_divisions, text="Удалить дивизион", command=delete_division_gui)
btn_delete_division.pack(pady=5)

# Настройка вкладки Matchs
tree_matches = ttk.Treeview(tab_matches, columns=(
    "Div", "Дата", "Домашняя команда", "Гостевая команда", "Голы дома", "Голы гости", "Результат", "Сезон"
), show="headings")
for col in tree_matches["columns"]:
    tree_matches.heading(col, text=col)
tree_matches.pack(fill="both", expand=True)

btn_add_match = ttk.Button(tab_matches, text="Добавить матч", command=add_match_gui)
btn_add_match.pack(pady=5)

btn_update_match = ttk.Button(tab_matches, text="Обновить матч", command=update_match_gui)
btn_update_match.pack(pady=5)

btn_delete_match = ttk.Button(tab_matches, text="Удалить матч", command=delete_match_gui)
btn_delete_match.pack(pady=5)

btn_search_match = ttk.Button(tab_matches, text="Поиск матчей по дате", command=search_matches_by_date_gui)
btn_search_match.pack(pady=5)

# Загрузка данных
load_divisions()

# Запуск приложения
tab_control.pack(expand=1, fill="both")
root.mainloop()