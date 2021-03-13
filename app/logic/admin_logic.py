from datetime import datetime

from app.extensions import db
from app.models.sextable import SexTable
from app.models.basetable import BaseTable


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


def sexlist(name="М"):
    # db.session.query(EVENTS).order_by(EVENTS.id.desc()).filter_by(id=id_event).first()
    return db.session.query(SexTable).all()
    # return db.session.query(SexTable).filter_by(name=name).first()


# Заполнить справочник BaseTable
def create_basetable():
    # Удалить все данные из таблицы SexTable
    db.session.query(BaseTable).delete()
    db.session.commit()
    new_base_node = BaseTable(name="ПП-20", gun_name="пистолет пневматический",
                              caption="пистолет пневматический, 10 м, 20 выстрелов стоя с упора (штатив)",
                              measure="Очки", rank="III", id_sex=2, number_shoot=4, value=169)
    db.session.add(new_base_node)
    # db.session.commit()
    new_base_node = BaseTable(name="ПП-20", gun_name="пистолет пневматический",
                              caption="пистолет пневматический, 10 м, 20 выстрелов стоя с упора (штатив)",
                              measure="Очки", rank="III", id_sex=1, number_shoot=2, value=173)
    db.session.add(new_base_node)
    db.session.commit()
