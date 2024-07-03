import pandas as pd
from numpy import random


def generate_sample_data(symbol: str, num_records: int = 1000) -> pd.DataFrame:
    random.seed(42)

    timestamps = pd.date_range(start="2023-01-01", periods=num_records, freq="30s")

    data = {
        "timestamp": timestamps,
        "symbol": symbol,
        "volume": random.randint(100, 1000, num_records),
        "price": random.uniform(40, 60, num_records),
        "buy_broker": random.randint(1, 11, num_records),
        "sell_broker": random.randint(1, 11, num_records),
    }

    return pd.DataFrame(data)
