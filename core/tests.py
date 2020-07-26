from django.test import TestCase


from core.models import TriggerPhrase

from core.util.ArticleAnalyser import ArticleAnalyser


class TestTextAnalysis(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.ARTICLE_ANALYSER = ArticleAnalyser()

    def test_cleaning_text(self):
        text = "Roses (are) red, violets are blue!"
        self.assertEqual(self.ARTICLE_ANALYSER.clean_text(text), 'Roses are red violets are blue ')

    def test_normalizing_text(self):
        self.assertEqual(self.ARTICLE_ANALYSER.get_word_with_normal_form('Розы'), 'роза')
        self.assertEqual(self.ARTICLE_ANALYSER.get_word_with_normal_form('Делают'), 'делать')
