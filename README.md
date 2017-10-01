[![Build Status](https://travis-ci.org/z-keith/maragi.svg?branch=tdd-rewrite)](https://travis-ci.org/z-keith/maragi)

# keep in mind:
-	user/goal/action validation [continue as more fields are added to each]
-	safe_url [continue as any more login_required pages are added]

# todo: test-driven edition!
## Server side
-	database setup (postgres, this time)
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
#Postgres setup:
sudo su
passwd postgres
su postgres
psql
\password postgres
createdb *****
CREATE USER zkeith;
GRANT ALL PRIVILEGES ON DATABASE ***** TO zkeith;
\q