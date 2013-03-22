"""
model.py
"""

import sqlite3
import datetime, time

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE email = ? AND password = ?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None

def new_task(db, title, user_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
	created_at = datetime.datetime.now()
	result = c.execute(query, (title, created_at, user_id))
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT Tasks.user_id, Users.id, Users.email, Users.password, Users.name FROM Tasks INNER JOIN Users ON Tasks.user_id = Users.id WHERE user_id = ?"""
	c.execute(query, (user_id,))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None

def complete_task(db, task_id):
	c = db.cursor()
	query = """UPDATE Tasks SET completed_at = ? WHERE id = ?"""
	completed_at = datetime.datetime.now()
	result = c.execute(query, (completed_at, task_id,))
	db.commit
	return result.lastrowid

def get_tasks(db, user_id):
	c = db.cursor()
	if user_id:
		query = """SELECT * FROM Tasks WHERE user_id = ?"""
		c.execute(query, (user_id,))
	else:
		query = """SELECT * FROM Tasks"""
		c.execute(query)
	tasks = []
	rows = c.fetchall()
	for row in rows:
		task = dict(zip(["id", "title", "created_at", "completed_at", "user_id"], row))
		tasks.append(task)
	return tasks

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id = ?"""
	c.execute(query, (task_id,))
	result = c.fetchone()
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))

	return None