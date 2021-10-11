import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Name of file to be parsed')
if len(fname) < 1:
    fname = 'default.txt'
file = open(fname)

for line in file:
    if line.startswith('From:'):
        email = line.split()[1]
        cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
        # If a record already exists, update it; otherwise initialize it
        if cur.fetchone():
            cur.execute(
                'UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
        else:
            cur.execute(
                'INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    conn.commit()

for row in cur.execute('SELECT email, count FROM Counts ORDER BY count LIMIT 10'):
    print(row[0], row[1])
