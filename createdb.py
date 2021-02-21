#!/usr/bin/python
  
import sqlite3

conn = sqlite3.connect('beenodeslive.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE IPTOCITY
         (D INTEGER PRIMARY KEY,
          IP             TEXT     NOT NULL,
          LAT            REAL     NOT NULL,
          LNG            REAL     NOT NULL,
          CITY           TEXT     NOT NULL);''')
conn.execute('''CREATE INDEX iptocity_ip on IPTOCITY(IP)''')
print("Table IPTOCITY created successfully");

conn.execute('''CREATE TABLE OVERLAYTOIP
         (OVERLAY  TEXT  PRIMARY KEY,
          IP           TEXT    NOT NULL);''')
print("Table OVERLAYTOIP created successfully");

conn.execute('''CREATE TABLE BEENODES
         (ID INTEGER PRIMARY KEY,
          DATE            TEXT     NOT NULL,
          CITY            TEXT     NOT NULL,
          IP              TEXT    NOT NULL);''')
conn.execute('''CREATE INDEX beenodes_date on BEENODES(DATE)''')
print("Table BEENODES created successfully");
conn.close()

