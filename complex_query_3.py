import psycopg2 as pg2
from prettytable import PrettyTable
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''User Story 4: As a content creator, I want to send messages to my most devoted fans
to keep them engaged in my activity.''')

def send_message(creator_id, message):
    print('Before query:')
    cur.execute('SELECT * FROM Messages')
    rows = cur.fetchall()
    table = PrettyTable(['message_id', 'sent_to', 'sent_from', 'message'])
    for row in rows:
        table.add_row(row)
    print(table)

    query = '''
    INSERT INTO Messages(sent_to, creator_id, message)
        (SELECT DISTINCT(f.user_id), %s, %s
           FROM Follows as f
           JOIN Messages as m ON m.creator_id = f.creator_id 
          WHERE f.rating >= 4 AND f.creator_id = %s) 
    '''

    print('After query:')
    cur.execute(query, [creator_id, message, creator_id])
    cur.execute('SELECT * FROM Messages')
    rows1 = cur.fetchall()
    table1 = PrettyTable(['message_id', 'sent_to', 'sent_from', 'message'])
    for row in rows1:
        table1.add_row(row)
    print(table1)

print('''Description: The creator with id 1 wants to send the message \"Listen to my new album Positions!\"
to her most devoted fans, or fans that have her rated at 4 or higher out of 5.''')
send_message(1, 'Listen to my new album Positions!')

