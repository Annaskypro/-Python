from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:1891Annaskypro!" \
    "@localhost:5432/postgres"


def test_insert():
    db = create_engine(db_connection_string)
    with db.connect() as connection:
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row1 = len(rows)
        sql = text("insert into subject(subject_title) values (:new_name)")
        connection.execute(sql, {"new_name": "psychology"})
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row2 = len(rows)
        assert row2 - row1 == 1
        sql = text("DELETE FROM subject WHERE subject_title  = :id")
        connection.execute(sql, {"id": 'psychology'})
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row3 = len(rows)
        assert row1 == row3
        connection.commit()
    connection.close()


def test_update():
    db = create_engine(db_connection_string)
    with db.connect() as connection:
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row1 = len(rows)
        sql = text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id,:new_name) RETURNING subject_id")
        result = connection.execute(sql, {"id": 16, "new_name": "psychology"})
        new_id = result.scalar()  # Получаем ID
        connection.commit()
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row2 = len(rows)
        assert row2 - row1 == 1
        sql = text(
            "UPDATE subject SET subject_title = :new_title "
            "WHERE subject_id = :id and subject_title = :new_name")
        connection.execute(
            sql, {"new_title": "updated", "id": new_id,
                  "new_name": "psychology"})
        connection.commit()
        result = connection.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": new_id})
        row = result.mappings().first()
        assert row['subject_title'] == "updated"
        sql = text("DELETE FROM subject WHERE subject_title  = :new_name")
        connection.execute(sql, {"new_name": 'updated'})
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row3 = len(rows)
        assert row1 == row3
        connection.commit()
    connection.close()


def test_delete():
    db = create_engine(db_connection_string)
    with db.connect() as connection:
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row1 = len(rows)
        sql = text("insert into subject(subject_title) values (:new_name)")
        connection.execute(sql, {"new_name": "psychology"})
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row2 = len(rows)
        assert row2 - row1 == 1
        sql = text("DELETE FROM subject WHERE subject_title  = :id")
        connection.execute(sql, {"id": 'psychology'})
        rows = connection.execute(text("SELECT * FROM subject")).fetchall()
        row3 = len(rows)
        assert row1 == row3
        connection.commit()
    connection.close()
