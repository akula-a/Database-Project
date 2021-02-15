import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 7')
print('''Description: Allows Listener to organize their content chronologically so that they 
can see their most recent content first''')

def show_content():
    query = 'SELECT * FROM Audio_Content'
    cur.execute(query)    
    rows = cur.fetchall()
    table = PrettyTable(['Content_id', 'Artist Name', 'Name', 'Date Published', 'Album'])
    for row in rows:
        table.add_row(row)
    print(table)

show_content()

def organize_content():
    query = '''
    SELECT name, album, date_published
      FROM Audio_Content 
     ORDER BY date_published DESC
    '''
    cur.execute(query)
    print('after: ')
    
    rows = cur.fetchall()
    table = PrettyTable(['Song Name', 'Album Name', 'Date Published'])
    for row in rows:
        table.add_row(row)
    print(table)

organize_content()


