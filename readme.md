## Read initial data
Check the utilities/initial_data/data_creator.py script to understand the schema to create your data.

1. Create a .xls or .csv file with all your data
2. Run the following command
```python
python manage.py populate_database
```
3. It will populate your database with the data in the file. If you want to create a fixture file, you can use the second run method. Notice that your data file must have the same structure as the database definition.
4. Enjoy

## Generate endpoints automatically
1. Create all your models of your app
2. Run the following command
```bash
python manage.py add_endpoint -a YOUR_APP_NAME -p YOUR_TARGET_PATH
```
3. Modify the generated serializers to your needs
4. Modify the generated views to your needs
5. Modify the generated urls to your needs
6. Enjoy

## Generate cURL commands as endpoints documentation
1. Create all your views and serializers
2. Register all your routes in the urls.py file
3. Run the following command
```bash
python manage.py create_curl -a YOUR_APP_NAME
```
4. It will create a directory name docs on your project root directory
5. Import it all in your postman
6. Enjoy

## Paginator
1. You can use "page" and "page_size" as query params to paginate your results

## Restore database
1. Create a backup of the database. If you are using docker this is the command
```bash
docker exec -t <container name> pg_dumpall -c -U YOUR_USER > backup_database.sql
```
2. Restore the database. If you are using docker this is the command
```bash
cat backup_database.sql | docker exec -i <container name> psql -U YOUR_USER
```
3. If you are in a linux environment you can use this command
```bash
psql -U YOUR_USER -f backup_database.sql
```
4. Finally, for windows users, you can use this command
```bash
cd "C:\Program Files\PostgreSQL\YOUR_VERSION\bin"
./psql.exe -U YOUR_USER -f "C:\backup_database.sql"
```
5. Enjoy


### data

[data](https://docs.google.com/spreadsheets/d/1KNCQ2AoHyL1KbtTVRhvKVczNhVg-S98J06Z3ABNyORI)


### TODO:


- cuando haga un deal descontar o agregar dinero a la cuenta
- cuando se haga un deal hay que crear otra posición con el profit que se obtuvo