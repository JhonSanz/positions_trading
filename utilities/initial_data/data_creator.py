from utilities.read_initial_data import DataReader

reader = DataReader(
    data_file="utilities/initial_data/data_inversiones.ods",
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
