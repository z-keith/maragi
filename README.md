[![Build Status](https://travis-ci.org/z-keith/maragi.svg?branch=tdd-rewrite)](https://travis-ci.org/z-keith/maragi)

# keep in mind:
-	user/goal/action validation [continue as more fields are added to each]
-	safe_url [continue as any more login_required pages are added]

# todo: test-driven edition!
## Server side
-	~~database setup (postgres, this time)~~
-	data model (user, goal, action)
-	server-side of login and authentication
-	data access endpoints (RESTful get, add, edit, remove - all with HTTPS and server-side validation)
## Client side
-	login/logout/load-user functions
-	parse user/goal/action responses
-	home, login, dashboard, settings, user creation routes
## Front end
-	lay out pages on paper
-	build dashboard
-	build settings page
-   build account creation
-	build home page
---
#Dependency setup
1. sudo pip3 install virtualenv
2. virtualenv ../venv
3. (create a .env file with)
	- source ../venv/bin/activate
	- export FLASK_APP="run.py"
	- export SECRET="(secret goes here)"
	- export APP_SETTINGS="development"
	- export DATABASE_URL="postgresql:///maragi_test_db"
4. source .env
---
#Postgres setup:
1. sudo su
2. passwd postgres
3. su postgres
4. psql
5. \password postgres
6. createdb maragi_test_db
7. CREATE USER zkeith;
8. GRANT ALL PRIVILEGES ON DATABASE maragi_test_db TO zkeith;
9. \q
---
#Running Postgres:
1. sudo service postgresql start
---
#Running tests:
1. nose2 and/or
2. commit to Github and check Travis CI
