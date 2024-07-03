from typing import Tuple

import numpy as np
import pandas as pd
from numpy.fft import fft


class PairSniffer:
    def __init__(
        self,
        data_x: pd.DataFrame,
        data_y: pd.DataFrame,
        broker: int,
        coherence_threshold: float = 0.7,
        opposite_direction_threshold: float = 0.6,
        price_divergence_threshold: float = 0.55,
    ):
        """
        Initialize the PairSniffer object.

        Parameters:
        - data_x (pd.DataFrame): The first dataset.
        - data_y (pd.DataFrame): The second dataset.
        - broker (int): The broker identifier.
        - coherence_threshold (float): The coherence threshold value (default: 0.7).
        - opposite_direction_threshold (float): The opposite direction threshold value (default: 0.6).
        - price_divergence_threshold (float): The price divergence threshold value (default: 0.55).
        """
        self.data_x = data_x
        self.data_y = data_y
        self.broker = broker
        self.coherence_threshold = coherence_threshold
        self.opposite_direction_threshold = opposite_direction_threshold
        self.price_divergence_threshold = price_divergence_threshold

    def detect_pairs_trade(self) -> Tuple[bool, float, float, float]:
        """
        Detects pairs trades based on the given criteria.

        Returns:
            is_pairs_trade (bool): Indicates whether a pairs trade is detected.
            mean_coherence (float): Mean coherence value.
            opposite_direction (float): Average percentage of trades with opposite direction.
            price_divergence (float): Average percentage of price changes with opposite direction.
        """
        x_trades = self.data_x[
            (self.data_x["buy_broker"] == self.broker)
            | (self.data_x["sell_broker"] == self.broker)
        ]

        y_trades = self.data_y[
            (self.data_y["buy_broker"] == self.broker)
            | (self.data_y["sell_broker"] == self.broker)
        ]

        x_net_position = np.where(
            x_trades["buy_broker"] == self.broker,
            x_trades["volume"],
            -x_trades["volume"],
        )

        y_net_position = np.where(
            y_trades["buy_broker"] == self.broker,
            y_trades["volume"],
            -y_trades["volume"],
        )

        x_price_changes = np.diff(x_trades["price"])
        y_price_changes = np.diff(y_trades["price"])

        min_length = min(
            len(x_net_position),
            len(y_net_position),
            len(x_price_changes),
            len(y_price_changes),
        )

        x_net_position = x_net_position[:min_length]
        y_net_position = y_net_position[:min_length]
        x_price_changes = x_price_changes[:min_length]
        y_price_changes = y_price_changes[:min_length]

        x_fft = fft(x_net_position)
        y_fft = fft(y_net_position)

        cross_correlation = np.abs(x_fft * np.conj(y_fft))

        x_power = np.abs(x_fft) ** 2
        y_power = np.abs(y_fft) ** 2

        coherence = cross_correlation / np.sqrt(x_power * y_power)
        mean_coherence = np.mean(coherence)

        opposite_direction = np.mean(np.sign(x_net_position) != np.sign(y_net_position))

        price_divergence = np.mean(np.sign(x_price_changes) != np.sign(y_price_changes))

        is_pairs_trade = (
            (mean_coherence > self.coherence_threshold)
            and (opposite_direction > self.opposite_direction_threshold)
            and (price_divergence > self.price_divergence_threshold)
        )

        return is_pairs_trade, mean_coherence, opposite_direction, price_divergence
