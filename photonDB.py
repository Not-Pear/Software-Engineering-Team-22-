"requires pip install psycopg2-binary"
import psycopg2

"Function to get connection to the photon database"
def getConnection():
	try:
		return psycopg2.connect(
			database="photon",
			user="student",
		)
	except:
		return False
		
"Parameters: none"
"Returns: A list of Tuples of all Players formatted (id, codename)"
def getAllPlayers():
	conn = getConnection()
	if not conn:
		return []
	curr = conn.cursor()
	curr.execute(f"SELECT * FROM players;")
	data = curr.fetchall()
	conn.close()
	return data

"Parameters: id of player you're looking for"
"Return: Tuple of a boolean indicating if the player was in the database and the players codename if found"	
def queryId(id):
	conn = getConnection()
	if not conn:
		return (False, 'Failure')
	curr = conn.cursor()
	curr.execute(f"SELECT * FROM players WHERE id = {id};")
	data = curr.fetchall()
	conn.close()
	if len(data) > 0:
		return (True, data[0][1])
	else:
		return (False, '')

"Parameters: id and codename of player you wish to insert into the database"
"Returns: if a connection to the SQL database was established"
def addPlayer(id, codename):
	conn = getConnection()
	if not conn:
		return False
	curr = conn.cursor()
	curr.execute(f"INSERT INTO players VALUES ({id}, '{codename}');")
	conn.commit()
	return True

"Parameters: id to be deleted"
"Returns: if a connection to the SQL database was established"
def deleteId(id):
	conn = getConnection()
	if not conn:
		return False
	curr = conn.cursor()
	curr.execute(f"DELETE FROM players WHERE id={id}")
	conn.commit()
	conn.close()
	return True

