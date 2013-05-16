#!/usr/bin/env python

db = {}

def newuser():
	prompt = "login desired:"
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = "name taken,try another"
		else:
			break
	pwd = raw_input("passwd:")
	db[name] = pwd

def olduser():
	name = raw_input("login name:")
	pwd = raw_input("password:")
	passwd = db.get(name)
	if pwd == passwd:
		print "welcome back,",name
	else:
		print "error"

def showmenu():
	prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter Choice: """

	done = False

	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError,KeyboardInterrupt):
				choice = 'q'
			print "you picked:{%s] " % choice

			if choice not in 'neq':
				print "invalid option,tre again"
			else:
				chosen = True

		if choice == 'q':done = True
		if choice == 'n':newuser()
		if choice == 'e':olduser()

if __name__ == '__main__':
	showmenu()

