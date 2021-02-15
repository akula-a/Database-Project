import psycopg2 as pg2
con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('User Story 5')
print('''As a content creator, I want to know my total number of followers
so that I know how well my content is doing''')

def show_num_followers(creator_id):
    query = '''
        SELECT num_followers
          FROM Content_Creator
         WHERE creator_id = 1;
    '''
    cur.execute(query)
    print('Number of Followers' + str(cur.fetchall()))

print('Prints the number of followers for Ariana Grande whose creator_id is 1')
show_num_followers(1)

    

