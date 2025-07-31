import unittest
import pandas as pd
from main import *

class TestNetflixAssignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv("data/netflix.csv")

    def test_data_dimensions(self):
        self.assertEqual(get_data_dimensions(self.df), self.df.shape)

    def test_null_counts(self):
        self.assertTrue(isinstance(get_null_counts(self.df), pd.Series))

    def test_no_duplicates(self):
        self.assertEqual(has_duplicates(self.df), self.df.duplicated().any())

    def test_summary_statistics(self):
        stats = get_summary_statistics(self.df)
        self.assertTrue("type" in stats.columns or "type" in stats.index)

    def test_director_filter(self):
        result = get_movies_by_director(self.df)
        self.assertTrue((result["director"] == "Masahiko Murata").all())

    def test_mean_runtime(self):
        mean_runtime = get_mean_runtime(self.df)
        self.assertIsInstance(mean_runtime, float)

    def test_top_country(self):
        country = get_top_country(self.df)
        self.assertIsInstance(country, str)

    def test_rating_chart_saved(self):
        plot_rating_bar_chart(self.df)
        import os
        self.assertTrue(os.path.exists("ratings_bar_chart.png"))

    def test_total_counts(self):
        counts = get_total_counts(self.df)
        self.assertIn("Movie", counts)
        self.assertIn("TV Show", counts)

if __name__ == "__main__":
    unittest.main()
