from singleton_data.util.utilities import Utility


class DataSource(object):
    class __datasource():
        def __init__(self):
            print(":::::::::::::::::::::::DATA::::::::::::::::::\n"
                  "::::::init DataSource::::::\n::::::::::::::::::::::::::::::::::::::::::::::")

        def get_application_by_name(self, query_name):
            row_object = 0
            lines = Utility.read_source("applications")
            header = Utility.get_header_source("applications")
            for index_line in range(0, len(lines)):
                row = lines[index_line].split(",")
                if query_name in row[0]:
                    row_object = dict(zip(header, row))
                    return row_object
            if row_object == 0:
                print(f"[¯\_(ツ)_/¯] 404 - resource applications not found (with query \"{query_name}\")")
                return 404

        def get_reviews_by_app_name(self, query_name):
            data = []
            lines = Utility.read_source("reviews")
            header = Utility.get_header_source("reviews")
            for line in lines:
                row = line.split(",")
                if query_name in row[0]:
                    row_object = dict(zip(header, row))
                    data.append(row_object)
            if len(data) <= 0:
                print(f"[¯\_(ツ)_/¯] 404 resource reviews not found (with query \"{query_name}\")")
                return 404
            return data

    instance = None

    def __new__(cls):
        if not DataSource.instance:
            DataSource.instance = DataSource.__datasource()
        return DataSource.instance
