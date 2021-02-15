import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 9')
print('Description: Allows Ad-selling companies to create an ad message so that they can inform users of their product.')

def show_ads():
    query='SELECT * from Ads'
    cur.execute(query)
    rows = cur.fetchall()
    table = PrettyTable(['Ad_id', 'Company Name', 'Message', 'Views'])
    for row in rows:
        table.add_row(row)
    print(table)

show_ads()
          
    
def new_ad():
    query = '''
            INSERT INTO Ads(company_name, message, views)
            VALUES ('LA Fitness', 'Check out our new workout playlist', 0)

            '''
    cur.execute(query)
    print('after: ')
    show_ads()
    

new_ad()