## Read initial data
1. Create a .xls or .csv file with all your data
2. Run the following command
```python
from utils.read_initial_data import DataReader

DataReader(
    data_file="utils/initial_data/data_inversiones.ods",
    app="position",
    data_definition=[
        {
            "sheet_name": "money",
            "model": "Money",
            "related_fields": [],
        },
        {
            "sheet_name": "broker",
            "model": "Broker",
            "related_fields": [],
        },
        {
            "sheet_name": "account",
            "model": "Account",
            "related_fields": [
                {"model": "Broker", "field": "broker"}
            ]
        },
        {
            "sheet_name": "assets",
            "model": "Asset",
            "related_fields": [
                {"model": "Account", "field": "account"}
            ]
        },
        {
            "sheet_name": "positions",
            "model": "Position",
            "related_fields": [
                {"model": "Position", "field": "reference"},
                {"model": "Asset", "field": "asset"}
            ]
        }
    ]
)
reader.run(mode=DataCreator.POPULATE)
reader.run(mode=DataCreator.FIXTURE)
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