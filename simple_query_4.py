import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 8')
print('Description: Allows Ad-selling companies to see the number of views on their ad so that they can know how many people their ad is reaching.')

def show_ads():
    query = 'SELECT * FROM Ads'
    cur.execute(query)
    rows = cur.fetchall()
    table = PrettyTable(['Ad_id', 'Company Name', 'Message', 'Views'])
    for row in rows:
        table.add_row(row)
    print(table)

show_ads()

def see_views():
    query = '''
    SELECT company_name, message, views
      FROM Ads 
     WHERE company_name = 'Spotify'
     ORDER BY views DESC
    '''
    cur.execute(query)
    print('after: ')
    
    rows = cur.fetchall()
    table = PrettyTable(['Company Name', 'Message', 'Views'])
    for row in rows:
        table.add_row(row)
    print(table)

see_views()



