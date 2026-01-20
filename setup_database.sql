-- Create Database
CREATE DATABASE IF NOT EXISTS attendance_system;
USE attendance_system;

-- Create student table
CREATE TABLE IF NOT EXISTS student (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    section VARCHAR(50),
    status VARCHAR(20) DEFAULT 'unregistered'
);

-- Create attendance table
CREATE TABLE IF NOT EXISTS attendance (
    id VARCHAR(50),
    name VARCHAR(100),
    section VARCHAR(50),
    time VARCHAR(20),
    date VARCHAR(20),
    FOREIGN KEY (id) REFERENCES student(id) ON DELETE CASCADE
);

-- Create admin_signup table
CREATE TABLE IF NOT EXISTS admin_signup (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create admin_login table
CREATE TABLE IF NOT EXISTS admin_login (
    admin_id INT,
    username VARCHAR(100),
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES admin_signup(admin_id) ON DELETE CASCADE
);

-- Create user 'mahar' if it doesn't exist
CREATE USER IF NOT EXISTS 'mahar'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON attendance_system.* TO 'mahar'@'localhost';
FLUSH PRIVILEGES;
