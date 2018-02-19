from flask_sqlalchemy import SQLAlchemy

# initialize sql-alchemy
db = SQLAlchemy()

def init_testdb():
	init_users()
	init_goals()
	init_actions()

def init_users():
	from api.user import User
	arthur = User('mustbethursday', 'Arthur', 'Dent', 'bewareofleopard@yahoo.com', '$6$rounds=656000$5aoOS0OwZhuCSBgt$VjCBqVTG6N4Is17X2yEF1PcMooLquiaDftICME7my06biCVJojVept.4RVdYDoRBrojVHKxsDo6uMOeP0JZc9/')
	fenchurch = User('AnArtToFlying', 'Fenchurch', '', 'nomorenails@outlook.com', '$6$rounds=656000$5aoOS0OwZhuCSBgt$VjCBqVTG6N4Is17X2yEF1PcMooLquiaDftICME7my06biCVJojVept.4RVdYDoRBrojVHKxsDo6uMOeP0JZc9/')
	ford = User('Ix_prime', 'Ford', 'Prefect', 'unpleasantlydrunk@gmail.com', '$6$rounds=656000$TZ5JXKjROSOuEY97$M9bHq.N9h9cl3TPfoe29H5Y/LxfXmCDSm4KXUq8yNt9nlPmYaQ0DF.i/nbqGzHkOn0ROJrdWX4HNAkMMudXAU.')
	marvin = User('oh_no', 'Marvin', 'the Paranoid Android', 'GPP.0042@siriuscybernetics.com', '$6$rounds=656000$TZ5JXKjROSOuEY97$M9bHq.N9h9cl3TPfoe29H5Y/LxfXmCDSm4KXUq8yNt9nlPmYaQ0DF.i/nbqGzHkOn0ROJrdWX4HNAkMMudXAU.')

	db.session.add(arthur)
	db.session.add(fenchurch)
	db.session.add(ford)
	db.session.add(marvin)

	db.session.commit()

def init_goals():
	from api.goal import Goal
	g1 = Goal(1, 'Make 100 sandwiches', 100000)
	g2 = Goal(1, 'Save 100 dolphins', 100000)
	g3 = Goal(2, 'Fly 6 times', 6000)
	g4 = Goal(2, 'Don\'t disappear', 1000, inverted=True)
	g5 = Goal(3, 'Scan 1000 UFOs', 1000000)
	g6 = Goal(3, 'Write 50 articles', 50000)

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)

	db.session.commit()

def init_actions():
	from api.action import Action
	g1 = Action(1, 'Corned beef on rye', 1000)
	g2 = Action(1, 'Peanut butter and jelly', 1000)
	g3 = Action(2, 'Found fishbowl', 1000)
	g4 = Action(3, 'Had sex on wing of commercial airliner', 1000)
	g5 = Action(3, 'Had sex on wing of commercial airliner (w/ Walkmen)', 1000)
	g6 = Action(4, 'Took interstellar trip', 1000)
	g7 = Action(5, 'Red flying saucer', 1000)
	g8 = Action(5, 'Green flying saucer', 1000)

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)
	db.session.add(g7)
	db.session.add(g8)

	db.session.commit()