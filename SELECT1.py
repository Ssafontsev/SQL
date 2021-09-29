import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
engine
connection = engine.connect()
sel = connection.execute("""
SELECT name, COUNT(artist_id) FROM artist
JOIN address a ON s.address_id = a.address_id;
""").fetchall()

pprint(sel)