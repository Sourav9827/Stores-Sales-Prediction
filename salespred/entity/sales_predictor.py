import os
import sys

from salespred.exception import SalesException
from salespred.util.util import load_object

import pandas as pd


class SalesData:

    def __init__(self,	
                 Item_Weight: float,	
                 Item_Fat_Content: str,
                 Item_Visibility: float,
                 Item_Type: str,
                 Item_MRP: float,
                 Outlet_Identifier: str,	
                 Outlet_Establishment_Year: int,	
                 Outlet_Size: str,
                 Outlet_Location_Type: str,
                 Outlet_Type: str,
                 Item_Outlet_Sales: float,
                 ):
        try:
            self.Item_Weight = Item_Weight
            self.Item_Fat_Content = Item_Fat_Content
            self.Item_Visibility = Item_Visibility
            self.Item_Type = Item_Type
            self.Item_MRP = Item_MRP
            self.Outlet_Identifier = Outlet_Identifier
            self.Outlet_Establishment_Year = Outlet_Establishment_Year
            self.Outlet_Size = Outlet_Size
            self.Outlet_Location_Type = Outlet_Location_Type
            self.Outlet_Type = Outlet_Type
            self.Item_Outlet_Sales = Item_Outlet_Sales
        except Exception as e:
            raise SalesException(e, sys) from e

    def get_salespred_input_data_frame(self):

        try:
            salespred_input_dict = self.get_salespred_data_as_dict()
            return pd.DataFrame(salespred_input_dict)
        except Exception as e:
            raise SalesException(e, sys) from e

    def get_salespred_data_as_dict(self):
        try:
            input_data = {
                "Item_Weight": [self.Item_Weight],
                "Item_Fat_Content": [self.Item_Fat_Content],
                "Item_Visibility": [self.Item_Visibility],
                "Item_Type": [self.Item_Type],
                "Item_MRP": [self.Item_MRP],
                "Outlet_Identifier": [self.Outlet_Identifier],
                "Outlet_Establishment_Year": [self.Outlet_Establishment_Year],
                "Outlet_Size": [self.Outlet_Size],
                "Outlet_Location_Type": [self.Outlet_Location_Type],
                "Outlet_Type": [self.Outlet_Type]
                }
            return input_data
        except Exception as e:
            raise SalesException(e, sys)


class SalesPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise SalesException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise SalesException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_house_value = model.predict(X)
            return median_house_value
        except Exception as e:
            raise SalesException(e, sys) from e