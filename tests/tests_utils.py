import unittest

from pair_sniffer.utils import generate_sample_data


class TestGenerateSampleData(unittest.TestCase):
    def test_generate_sample_data(self):
        df = generate_sample_data("AAPL")
        self.assertEqual(len(df), 1000)
        self.assertEqual(df["symbol"].unique(), ["AAPL"])
        self.assertTrue(df["volume"].between(100, 1000).all())
        self.assertTrue(df["price"].between(40, 60).all())
        self.assertTrue(df["buy_broker"].between(1, 10).all())
        self.assertTrue(df["sell_broker"].between(1, 10).all())

        df = generate_sample_data("AAPL", num_records=500)
        self.assertEqual(len(df), 500)
        self.assertEqual(df["symbol"].unique(), ["AAPL"])
        self.assertTrue(df["volume"].between(100, 1000).all())
        self.assertTrue(df["price"].between(40, 60).all())
        self.assertTrue(df["buy_broker"].between(1, 10).all())
        self.assertTrue(df["sell_broker"].between(1, 10).all())

        df = generate_sample_data("GOOG")
        self.assertEqual(len(df), 1000)
        self.assertEqual(df["symbol"].unique(), ["GOOG"])
        self.assertTrue(df["volume"].between(100, 1000).all())
        self.assertTrue(df["price"].between(40, 60).all())
        self.assertTrue(df["buy_broker"].between(1, 10).all())
        self.assertTrue(df["sell_broker"].between(1, 10).all())


if __name__ == "__main__":
    unittest.main()
