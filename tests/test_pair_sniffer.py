import unittest

import pandas as pd

from pair_sniffer import PairSniffer


class TestPairSniffer(unittest.TestCase):
    def setUp(self):
        self.data_x = pd.DataFrame(
            {
                "timestamp": pd.date_range(
                    start="2023-01-01", periods=1000, freq="30s"
                ),
                "symbol": "X",
                "volume": [100] * 1000,
                "price": [50] * 1000,
                "buy_broker": [1] * 1000,
                "sell_broker": [2] * 1000,
            }
        )

        self.data_y = pd.DataFrame(
            {
                "timestamp": pd.date_range(
                    start="2023-01-01", periods=1000, freq="30s"
                ),
                "symbol": "Y",
                "volume": [100] * 1000,
                "price": [50] * 1000,
                "buy_broker": [1] * 1000,
                "sell_broker": [2] * 1000,
            }
        )

        self.broker = 1
        self.pair_sniffer = PairSniffer(self.data_x, self.data_y, self.broker)

    def test_detect_pairs_trade(self):
        is_pairs_trade, mean_coherence, opposite_direction, price_divergence = (
            self.pair_sniffer.detect_pairs_trade()
        )

        self.assertIsInstance(is_pairs_trade, bool)
        self.assertIsInstance(mean_coherence, float)
        self.assertIsInstance(opposite_direction, float)
        self.assertIsInstance(price_divergence, float)


if __name__ == "__main__":
    unittest.main()
