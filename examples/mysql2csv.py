#!/usr/bin/env python
import MySQLdb
import sys

db = MySQLdb.connect("old.mailserver.com","dbusername","dbpassword","dbfroxlor" )
cursor = db.cursor ()
cursor.execute ("select email, password, homedir, maildir from mail_users")

data = cursor.fetchall ()

for row in data :
        #print "%s%s" % (row[2],row[3])
        #print "%s;%s;%s%s" % (row[0],row[1],row[2],row[3])
        print "%s;%s" % (row[0],row[1])

cursor.close ()
db.close ()
sys.exit()
