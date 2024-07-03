import jax.numpy as jnp
import pandas as pd


def generate_sample_data(symbol: str, num_records: int = 1000) -> pd.DataFrame:
    jnp.random.seed(42)

    timestamps = pd.date_range(start="2023-01-01", periods=num_records, freq="5T")

    data = {
        "timestamp": timestamps,
        "symbol": symbol,
        "volume": jnp.random.randint(100, 1000, num_records),
        "price": jnp.random.uniform(40, 60, num_records),
        "buy_broker": jnp.random.randint(1, 11, num_records),
        "sell_broker": jnp.random.randint(1, 11, num_records),
    }

    return pd.DataFrame(data)
