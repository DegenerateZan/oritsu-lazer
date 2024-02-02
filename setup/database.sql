CREATE TABLE tokens (
    'id' INT AUTO_INCREMENT PRIMARY KEY,
    'token' VARCHAR(500) NOT NULL,
    'user_id' INT NOT NULL,
    'created_at' TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE users (
  'id' int NOT NULL AUTO_INCREMENT,
  'name' varchar(15) NOT NULL,
  'email' varchar(45) NOT NULL,
  'country' varchar(3) DEFAULT NULL,
  'hash_pw' varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;