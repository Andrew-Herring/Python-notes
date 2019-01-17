import sqlite3
import sys

# sys.argv is a list of the passed in args from the command line
print(sys.argv)

super_db = '/Users/andrewherring/nss/Backend/python/notes/superheroes.db'

def get_supers():
  # shorthand for creating a connection
  with sqlite3.connect(super_db) as conn:
    cursor = conn.cursor()

# cursor runs a SQL query against the database
# pass execute SQl commands
# row is taco, what we are calling the information coming back

  # for row in cursor.execute('SELECT * FROM Superheroes'):
    # print(row)


  # Another way to do the same thing

  cursor.execute('SELECT * FROM Superheroes')
  supers = cursor.fetchall() 
  print(supers)


def get_super(super):
  with sqlite3.connect(super_db) as conn:
    cursor = conn.cursor()

    # s.* gets all of the superheores but not all of the information from the other tables
    cursor.execute(f"""SELECT s.*, side.Name 
                    FROM SUPERHEROES s
                    JOIN Sidekicks side
                    ON s.SuperheroId = side.SuperheroId
                    Where s.Name = '{super}'
                    """)

  super = cursor.fetchone()
  print(super)
  return super



def addSuper(super):
  with sqlite3.connect(super_db) as conn:
    cursor = conn.cursor()

    try:
       cursor.execute(
          '''
          INSERT INTO Superheroes
          Values(?,?,?,?,?)
          ''', (None, super["name"], super["gender"], super["secret"], None)
        ) 
    except sqlite3.OperationalError as err:
        print("oops", err)     



if __name__ == "__main__":
  get_supers()
  get_super(sys.argv[1])
  addSuper({
    "name": "Captain Derp",
    "gender": "sure",
    "secret": "Larry Smith"
  })
  get_supers()