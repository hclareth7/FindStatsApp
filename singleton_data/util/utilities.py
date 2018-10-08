class Utility:
    @classmethod
    def read_source(cls, source_name):
        file_dir = f"singleton_data/files/{Utility.get_source_by_name(source_name)}"
        with open(file_dir, "r") as log_file:
            return log_file.readlines()

    @classmethod
    def get_header_source(cls, source_name):
        return Utility._format_index_name(Utility.read_source(source_name)[0])

    @classmethod
    def _format_index_name(cls, index_line):
        new_index_line = []
        for index_name in index_line.split(","):
            new_index_name = str(index_name).lower().replace(" ", "_").replace("\n", "")
            new_index_line.append(new_index_name)
        return new_index_line

    @staticmethod
    def get_source_by_name(source_name):
        if source_name == "applications":
            return "googleplaystore.csv"
        elif source_name == "reviews":
            return "googleplaystore_user_reviews.csv"
