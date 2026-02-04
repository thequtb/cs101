-- Скрипт создания БД и пользователя PostgreSQL для Django.
-- Запуск один раз от суперпользователя: psql -U postgres -f create_db.sql
-- (на Linux часто: sudo -u postgres psql -f create_db.sql)

CREATE USER cs101_owner WITH PASSWORD 'bismillah';
CREATE DATABASE cs101_db OWNER cs101_owner;
GRANT ALL PRIVILEGES ON DATABASE cs101_db TO cs101_owner;
\c cs101_db
GRANT ALL ON SCHEMA public TO cs101_owner;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO cs101_owner;
