#!/bin/bash
# Запуск: sudo ./setup_pg_hba.sh
# Добавляет в pg_hba.conf правило: разрешить пользователю cs101_owner подключаться
# к БД cs101_db с хоста 127.0.0.1 (иначе Django получит "no pg_hba.conf entry").
PG_HBA=$(sudo -u postgres psql -t -c "SHOW hba_file;" | tr -d ' ')
ENTRY="host    cs101_db    cs101_owner    127.0.0.1/32    scram-sha-256"
if grep -q "cs101_db.*cs101_owner.*127.0.0.1" "$PG_HBA" 2>/dev/null; then
  echo "Запись уже есть в $PG_HBA"
else
  echo "$ENTRY" >> "$PG_HBA"
  echo "Добавлено в $PG_HBA"
fi
sudo -u postgres psql -c "SELECT pg_reload_conf();"
echo "Конфиг PostgreSQL перезагружен."
