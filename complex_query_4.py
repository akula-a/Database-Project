import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 6')
print('''Description: Allows Content Creator to rank their content against content of the same 
genre/category so that they know how well they are doing compared to their competition''')


def rank_content():
    query = '''
            SELECT au.content_id, au.name, cc.num_monthly_listeners, rank() over w
                FROM Audio_Content as au
                JOIN Makes as m ON au.content_id = m.content_id
                JOIN Content_Creator as cc ON m.creator_id = cc.creator_id
                JOIN Belongs_To as b ON au.content_id = b.content_id
                JOIN Category as c ON b.category_id = c.category_id
                WHERE c.category_id = 1 
            WINDOW w AS (ORDER BY cc.num_monthly_listeners DESC)
            '''
    cur.execute(query)
    print('after: ')
    rows = cur.fetchall()
    table = PrettyTable(['content_id', 'Name', 'Monthly Listeners', 'Rank'])
    for row in rows:
        table.add_row(row)
    print(table)

rank_content()
      