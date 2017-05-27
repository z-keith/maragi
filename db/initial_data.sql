-- sqlite3 maragi.db < initial-data.sql

-- Users
INSERT INTO user (id, username, firstname, lastname, email, hashed_password) VALUES (1, 'mustbethursday', 'Arthur', 'Dent', 'bewareofleopard@yahoo.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0');
INSERT INTO user (id, username, firstname, lastname, email, hashed_password) VALUES (2, 'AnArtToFlying', 'Fenchurch', '', 'nomorenails@outlook.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0');
INSERT INTO user (id, username, firstname, lastname, email, hashed_password) VALUES (3, 'Ix', 'Ford', 'Prefect', 'unpleasantlydrunk@gmail.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0');
INSERT INTO user (id, username, firstname, lastname, email, hashed_password) VALUES (4, 'oh_no', 'Marvin', 'the Paranoid Android', 'GPP.0042@siriuscybernetics.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0');

-- Goals
INSERT INTO goal (id, user_id, title) VALUES (1, 1, 'Make sandwiches');
INSERT INTO goal (id, user_id, title) VALUES (2, 1, 'Save dolphins');
INSERT INTO goal (id, user_id, title) VALUES (3, 2, 'Fly');
INSERT INTO goal (id, user_id, title) VALUES (4, 2, 'Don''t disappear');
INSERT INTO goal (id, user_id, title) VALUES (5, 3, 'Scan UFOs');
INSERT INTO goal (id, user_id, title) VALUES (6, 3, 'Write articles');

-- Actions
INSERT INTO action (id, goal_id, description) VALUES (1, 1, 'Corned beef on rye');
INSERT INTO action (id, goal_id, description) VALUES (2, 1, 'Peanut butter and jelly');
INSERT INTO action (id, goal_id, description) VALUES (3, 2, 'Found fishbowl');
INSERT INTO action (id, goal_id, description) VALUES (4, 3, 'Had sex on wing of commercial airliner');
INSERT INTO action (id, goal_id, description) VALUES (5, 3, 'Had sex on wing of commercial airliner (w/ Walkmen)');
INSERT INTO action (id, goal_id, description) VALUES (6, 4, 'Took interstellar trip');
INSERT INTO action (id, goal_id, description) VALUES (7, 5, 'Red flying saucer');
INSERT INTO action (id, goal_id, description) VALUES (8, 5, 'Green flying saucer');
