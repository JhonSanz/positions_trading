import pandas as pd
# from django.db.models import Model
# from django.apps import apps
import json

import enum


class DataCreator(enum.Enum):
    FIXTURE = 1
    POPULATE = 2


class DataReader:
    def __init__(self, data_file: str, data_definition: list[dict]):
        self.data_file = data_file
        self.data_definition = data_definition
        self.data = None
        self.sheet_names = []
        self.sheet_files = {}
        self.result = []

    def get_sheets_names(self):
        return [sheet["sheet_name"] for sheet in self.data_definition]

    def generate_data_from_sheet(self):
        return {sheet: pd.read_excel(self.data, sheet) for sheet in self.sheets_names}

    def iterate_over_data(self, mode: int):
        for item in self.data_definition:
            if item["related_fields"]:
                for related in item["related_fields"]:
                    related_table = list(filter(
                        lambda x: x["model"] == related["model"],
                        self.data_definition
                    ))
                    self.check_related_ids(related_table[0], item, related)
            if mode == DataCreator.FIXTURE:
                self.create_fixture(item)
            else:
                self.populate_database()

    def check_related_ids(self, table1: dict, table2: dict, related: dict) -> None:
        df_table1 = self.sheet_files[table1["sheet_name"]]
        df_table2 = self.sheet_files[table2["sheet_name"]]
        ids_table1 = set(df_table1["id"].dropna().unique().tolist())
        ids_related_table = set(df_table2[related["field"]].dropna().unique().tolist())

        if not ids_related_table.issubset(ids_table1):
            raise Exception(
                f"ids {ids_related_table.difference(ids_table1)} not found")

    def create_fixture(self, item: dict):
        sheet = self.sheet_files[item["sheet_name"]].astype(str)
        for record in sheet.to_dict("records"):
            id = record.pop("id")
            self.result.append(
                {"model": item["model"], "pk": id, "fields": record}
            )

    def populate_database(self):
        pass

    def run(self, mode: int):
        if not mode in [DataCreator.FIXTURE, DataCreator.POPULATE]:
            raise Exception(f"Mode {mode} not supported")
        self.data = pd.ExcelFile(self.data_file)
        self.sheets_names = self.get_sheets_names()
        self.sheet_files = self.generate_data_from_sheet()
        self.iterate_over_data(mode)

        with open("utils/initial_data/fixture.json", "w") as file:
            file.write(json.dumps(self.result, sort_keys=True, indent=4))
            file.close()

DataReader(
    data_file="utils/initial_data/data_inversiones.ods",
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
).run(mode=DataCreator.FIXTURE)
