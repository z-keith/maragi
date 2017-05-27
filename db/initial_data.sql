-- sqlite3 maragi.db < initial-data.sql

-- Users
INSERT INTO user (id, name) VALUES (1, 'Arthur');
INSERT INTO user (id, name) VALUES (2, 'Fenchurch');
INSERT INTO user (id, name) VALUES (3, 'Ford');
INSERT INTO user (id, name) VALUES (4, 'Marvin');

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
