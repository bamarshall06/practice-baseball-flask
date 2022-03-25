from app import db, app
from app.db_connect import connect

def get_teams():
    conn = connect()
    with conn.cursor() as cur:
        sql = f'SELECT team_id, team_name, team_mascot FROM team ORDER BY team_name'
        cur.execute(sql)
        return cur.fetchall()


def get_practices():
    conn = connect()
    with conn.cursor() as cur:
        sql = f'SELECT t.team_id, t.team_name, date(p.practice_date) as practice_date, p.practice_length, p.practice_id ' \
              f'FROM team t JOIN practice p ON t.team_id = p.team_id'
        cur.execute(sql)
        return cur.fetchall()