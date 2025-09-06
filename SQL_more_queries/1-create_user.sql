--  that creates the MySQL server user user_0d_1 --
CREATES USER IF NOT EXISTS  'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL ON *.* TO 'user_0d_1'@'localhost';