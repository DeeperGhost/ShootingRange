from datetime import datetime

from app.extensions import db
from app.models.sextable import SexTable
from app.models.basetable import BaseTable
from app.models.exercise import Exercise
from app.models.ranktable import RankTable
from app.models.events_data import EventsData

import csv


# Заполнить справочник SexTable
def create_sextable():
    # Удалить все данные из таблицы SexTable
    db.session.query(SexTable).delete()
    db.session.commit()
    # Создать две записи с М и Ж полом в таблице
    new_sex = SexTable(name="М", name_full="Мужской")
    db.session.add(new_sex)
    new_sex = SexTable(name="Ж", name_full="Женский")
    db.session.add(new_sex)
    db.session.commit()


# выбирает данные для выпадающего списка полов при добавления пользователя
def sexlist(name="М"):
    # db.session.query(EVENTS).order_by(EVENTS.id.desc()).filter_by(id=id_event).first()
    return db.session.query(SexTable).all()
    # return db.session.query(SexTable).filter_by(name=name).first()


# выбирает данные для выпадающего списка упражнений при добавления пользователя
def shortCaptionList():
    return db.session.query(BaseTable.short_caption).distinct(BaseTable.short_caption).all()

# список оружия
def gunList():
    return db.session.query(BaseTable.gun_short, BaseTable.gun_name).distinct(BaseTable.gun_short).all()


def exercise_list():
    return db.session.query(BaseTable.short_caption, BaseTable.series, BaseTable.total_shoot)\
        .distinct(BaseTable.short_caption, BaseTable.series, BaseTable.total_shoot).all()


def rankList():
    # return db.session.query(BaseTable).distinct(BaseTable.rank).group_by(BaseTable.rank).all()
    return db.session.query(BaseTable.rank, BaseTable.id_sex).distinct(BaseTable.rank, BaseTable.id_sex).all()


def switchsexID(sex):
    if sex == "М":
        return 1
    elif sex == "Ж":
        return 2


# Заполнить справочник BaseTable
def create_basetable():
    # Удалить все данные из таблицы SexTable

    db.session.commit()
    with open('app/res/databasetable.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            # print(row.keys())
            # print(row['id_static'])
            new_base_node = BaseTable(static_id=row['id'], short_caption=row['short_caption'],
                                      gun_short=row['gun_short'], gun_name=row['gun_name'],
                                      distance_1=row['distance_1'], total_shoot=row['total_shoot'],
                                      series=row['series'], caption=row['caption'], measure=row['measure'],
                                      rank=row['rank'], id_sex=switchsexID(row['sex']), value=row['value'])
            db.session.add(new_base_node)
    db.session.commit()


# Заполнить справочник exercise
def create_exercise_table():
    db.session.query(Exercise).delete()
    db.session.commit()
    with open('app/res/exercisetable.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            # print(row.keys())
            # print(row['id_static'])
            new_base_node = Exercise(ExerciseID=row['id'], name=row['name'],
                                     series=row['series'], total_shoot=row['total_shoot'])
            db.session.add(new_base_node)
    db.session.commit()


# Заполнить справочник ranktable
def create_rank_table():
    db.session.query(RankTable).delete()
    db.session.commit()
    with open('app/res/ranktable.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            # print(row.keys())
            # print(row['id_static'])
            new_base_node = RankTable(RankID=row['id'], name=row['name'], name_full=row['name_full'], age=row['age'])
            db.session.add(new_base_node)
    db.session.commit()






