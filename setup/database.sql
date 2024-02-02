CREATE TABLE `tokens` (
  `token` varchar(255) NOT NULL,
  `refresh_token` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`token`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tokens_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  `country` varchar(2) NOT NULL,
  `safe_name` varchar(45) NOT NULL,
  `argon2_pw` varchar(128) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;