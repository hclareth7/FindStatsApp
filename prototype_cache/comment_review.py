class CommentReview:
    def __init__(self, app_name, translated_review, sentiment, sentiment_polarity, sentiment_subjectivity):
        self.app_name = app_name
        self.translated_review = translated_review
        self.sentiment = sentiment
        self.sentiment_polarity = sentiment_polarity
        self.sentiment_subjectivity = sentiment_subjectivity

    def __str__(self):
        return (f"\tAPP NAME: {str(self.app_name).upper()}\n"
                f"\tTranslated review: {self.translated_review}\n"
                f"\tSentiment: {self.sentiment}\n"
                f"\tSentiment polarity: {self.sentiment_polarity}\n"
                f"\tSentiment subjectivity: {self.sentiment_subjectivity}")
