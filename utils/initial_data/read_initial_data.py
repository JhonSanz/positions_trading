import pandas as pd
from django.db.models import Model


class DataReader:
    def __init__(self, file_model: list[dict]):
        self.file_path = file_model

    def read_file(self, path: str):
        """
        Read the file and return a dataframe
        """
        df = pd.read_csv(path)
        return df

    def validate_columns(self, df: pd.DataFrame, model: Model):
        """
        Validate the columns of the dataframe
        """
        # model_columns = {
        #     item.name for item in model._meta.get_fields()
        #     if (
        #         not item.blank and not item.null
        #         and not item.auto_created
        #     )
        # }
        # if set(df.columns) != model_columns:
        #     raise Exception("The columns are not the same")
        return True

    def create_data(self, df: pd.DataFrame, model: Model):
        """
        Create the data in the database
        """
        for item in df.to_dict("records"):
            model.objects.create(**item)

    def run(self):
        """
        Get the data from the file and return a list of dictionaries
        """
        for item in self.file_path:
            df = self.read_file(item["file_path"])
            self.validate_columns(df, item["model"])
            self.create_data(df, item["model"])
