import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 10')
print('''Description: Allows Ad-selling companies to update their message 
      on Spotify so that they can provide new information about their product. In this example,
      change Kia Motors message.''')

def show_messages():
    query= 'SELECT * from Ads'
    cur.execute(query)
    rows = cur.fetchall()
    table = PrettyTable(['Ad_id', 'Company Name', 'Message', 'Views'])
    for row in rows:
        table.add_row(row)
    print(table)

show_messages()

def update_message():
    query = '''
    UPDATE Ads 
       SET message = 'Happy Birthday!'
     WHERE ad_id = 1;
    '''
    cur.execute(query)
    print('after: ')
    show_messages()
    

update_message()


