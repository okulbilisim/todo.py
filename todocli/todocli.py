# -*- coding: utf-8 -*-

__version__ = "0.0.1@alpha"


import sys
import sqlite3
import argparse

def main():
  check_create_todo_table()
  parser = argparse.ArgumentParser(description='Todo.py')
  parser.add_argument('-n','--new', help='new todo item', required=False)
  parser.add_argument('-d','--delete', help='delete a todo item with id', required=False)
  
  args = vars(parser.parse_args())
  if args['new'] != None:
    print "adding new todo"
  elif args['delete'] != None:
    delete_item()
  else:
    list_items()
  print "\n\n\ndebug line : "
  print("Executing todocli version %s." % __version__)
  print("List of argument strings: %s" % sys.argv[1:])


def new_item(todostr):
  conn = connect_todo_db()
  print "adding new todo item"
  conn.execute("INSERT INTO TODOPY (TITLE) \
      VALUES ('"+todostr+"')");
  conn.commit()
  conn.close()

def delete_item(todo_id):
  conn = connect_todo_db()
  print "deleting a todo item"
  conn.close()

def list_items():
  print "your todo list"
  conn = connect_todo_db()
  cursor = conn.execute("SELECT ID,TITLE FROM TODOPY")
  for row in cursor:
   print "ID = ", row[0]
   print "TITLE = ", row[1]
  cursor.close()
  conn.close()

def check_create_todo_table():
  conn = connect_todo_db()
  conn.execute('''CREATE TABLE IF NOT EXISTS TODOPY
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TITLE           TEXT    NOT NULL);''')
  conn.close()

def connect_todo_db():
  return sqlite3.connect('todo.db')
