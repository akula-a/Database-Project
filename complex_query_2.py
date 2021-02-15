import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''User Story 3: As a listener, I want to find songs based off a genre I enjoy
so I can discover new music.''')

def find_songs(genre):
    query = '''
        SELECT a.name, a.artist_name
          FROM Audio_Content as a
          JOIN Belongs_To as b ON a.content_id = b.content_id
          JOIN Category as c ON b.category_id = c.category_id
         WHERE c.name = %s
         LIMIT 5
        '''
    cur.execute(query, [genre])
    rows = cur.fetchall()
    table = PrettyTable(['Song Name', 'Artist Name'])
    for row in rows:
        table.add_row(row)
    print(table)


print('Description: A user is looking for songs based off the Pop Genre.')
find_songs('Pop')