
INSERT INTO users (id, name, email, balance, date_created)
VALUES
(1, 'Alex', 'alex@example.com', 1500.50, '2026-10-20'),
(2, 'Maria', 'maria@example.com', 2300.00, '2026-10-20'),
(3, 'Ivan', 'ivan@example.com', 750.25, '2026-10-20');

INSERT INTO products (id, name, price, sale, date_created)
VALUES
(1, 'Laptop', 850.00, 10, '2026-10-20'),
(2, 'Mouse', 25.50, 5, '2026-10-20'),
(3, 'Keyboard', 60.00, 15, '2026-10-20');

SELECT * FROM users;
SELECT * FROM products;
