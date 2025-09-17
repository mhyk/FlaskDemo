-- PostgreSQL Schema for Flask Demo Application
-- Converted from MySQL to PostgreSQL

-- Create database (run separately as superuser)
-- CREATE DATABASE ccc151_cs;

-- Connect to the database before running the following commands
-- \c ccc151_cs;

-- Create users table
DROP TABLE IF EXISTS user_info CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE,
    email VARCHAR(50),
    user_password VARCHAR(50)
);

-- Create user_info table with foreign key constraint
CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150),
    address VARCHAR(200),
    birthday DATE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_user_info_user_id ON user_info(user_id);

-- Optional: Insert sample data (uncomment if needed)
-- INSERT INTO users (username, email, user_password) VALUES
-- ('admin', 'admin@example.com', MD5('admin123')),
-- ('user1', 'user1@example.com', MD5('password'));