import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''User Story 1: As a listener, I want to be able to rate my followed artists
so Spotify can recommend more content from artists that I rate higher.''')

def rate_artist(user_id, creator_id, rating):
    print('Before query:')
    cur.execute('SELECT * FROM Follows')
    rows = cur.fetchall()
    table = PrettyTable(['user_id', 'creator_id', 'rating'])
    for row in rows:
        table.add_row(row)
    print(table)
    
    check_exists = cur.execute('SELECT (EXISTS(SELECT user_id, creator_id FROM Follows))')

    if (check_exists):
        query = '''
        UPDATE Follows
           SET rating = 4
         WHERE user_id = 3 and creator_id = 6
        '''
    else:
        query = '''
        INSERT INTO Follows(user_id, creator_id, rating)
            VALUES(3, 6, 4)
        '''

    print('After query:')
    cur.execute(query)
    cur.execute('SELECT * FROM Follows')
    rows1 = cur.fetchall()
    table1 = PrettyTable(['user_id', 'creator_id', 'rating'])
    for row in rows1:
        table1.add_row(row)
    print(table1)
    

print('''Description: If a user follows an artist, changes rating (1-5) for artist. 
    If not, makes user follow the artist and adds in a rating. In this case, user_id 3
    is adding a rating of 4 to creator_id 6.''')
rate_artist(3,6,4)

    

