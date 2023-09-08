## Restore database
1. Create a backup of the database. If you are using docker this is the command
```bash
docker exec -t <container name> pg_dumpall -c -U postgres > backup_database.sql
```
2. Restore the database. If you are using docker this is the command
```bash
cat backup_database.sql | docker exec -i <container name> psql -U postgres
```
3. If you are in a linux environment you can use this command
```bash
psql -U postgres -f backup_database.sql
```
4. Finally, for windows users, you can use this command
```bash
cd "C:\Program Files\PostgreSQL\YOUR_VERSION\bin"
./psql.exe -U postgres -f "C:\backup_database.sql"
```
