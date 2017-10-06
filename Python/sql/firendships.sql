SELECT users.first_name, users.last_name, users2.first_name
FROM users
LEFT JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as user2 ON users.id=friendships.friend_id
