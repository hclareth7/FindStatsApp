from singleton_data.data_source import DataSource
from prototype_cache.application import Application
from prototype_cache.comment_review import CommentReview
from prototype_cache.cache import Cache
from factory_output.printer_application import PrinterApplication
from factory_output.console_printer_factory import ConsolePrinterFactory
from factory_output.file_printer_factory import FilePrinterFactory

import datetime

if __name__ == '__main__':

    def print_option(target_data):
        printer_option = input("Select printer: [f/c] f: File printer, c: Console printer: ")
        if printer_option == "c":
            console_printer = ConsolePrinterFactory()
            printer = PrinterApplication(console_printer)
            printer.print(target_data)
        elif printer_option == "f":
            file_printer = FilePrinterFactory()
            printer = PrinterApplication(file_printer)
            printer.print(target_data)
        else:
            print("Please select a valid printer [f/c]")


    data = DataSource()
    cache = Cache()
    option = "y"
    while option == "y":
        application_name = input("type the App name: ")
        application = cache.get_item_by_name(application_name)
        if application is None:
            result = data.get_application_by_name(application_name)
            if result != 404:
                application = Application(name=result["app"],
                                          category=result["category"],
                                          rating=result["rating"],
                                          reviews=result["reviews"],
                                          size=result["size"],
                                          installs=result["installs"],
                                          last_updated=result["last_updated"],
                                          android_version=result["android_ver"])
                result_comments = data.get_reviews_by_app_name(application.name)
                if result_comments != 404:
                    comment_reviews = []
                    for comment in result_comments:
                        comment_review = CommentReview(app_name=comment["app"],
                                                       translated_review=comment["translated_review"],
                                                       sentiment=comment["sentiment"],
                                                       sentiment_polarity=comment["sentiment_polarity"],
                                                       sentiment_subjectivity=comment["sentiment_subjectivity"])
                        comment_reviews.append(comment_review)
                    application.comments_reviews = comment_reviews

                cache.add_item(application_name, application)

                print_option(application)
        else:
            application.last_search_date = datetime.datetime.now()
            print_option(application)
        option = input("type [yes or y or Y] to continue: ")
