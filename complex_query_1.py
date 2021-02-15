import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''User Story 2: As a listener, I want to find the artist with the highest average rating
so I know who the most popular artist is and I can listen to their music.''')

def find_popular_artist():
    query = '''
        SELECT c.name
          FROM Content_Creator as c
          JOIN Follows as f ON f.creator_id = c.creator_id
         GROUP BY f.creator_id, c.name
        HAVING avg(f.rating) = (SELECT avg(f1.rating)
                                  FROM Follows as f1
                                 GROUP BY f1.creator_id
                                 ORDER BY avg(f1.rating) DESC
                                 LIMIT 1)
        
    '''
    cur.execute(query)
    print('Best Rated Artist(s) = ' + str(cur.fetchall()))

find_popular_artist()