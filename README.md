# pair-sniffer

[![Python](https://github.com/alexandrebrilhante/pair-sniffer/actions/workflows/python-package.yml/badge.svg)](https://github.com/alexandrebrilhante/pair-sniffer/actions/workflows/python-package.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pair-sniffer)
![GitHub](https://img.shields.io/github/license/alexandrebrilhante/pair-sniffer)

This package implements a pairs trading detection algorithm using Fast Fourier Transform (FFT) to analyze trading patterns between two stocks. The algorithm is designed to identify potential pairs trading activity by a specific broker.

## Features
- Uses `numpy` for efficient numerical computations.
- Implements Fast Fourier Transform (FFT) for frequency domain analysis.
- Calculates coherence to measure the correlation of trading patterns.
- Configurable threshold for pairs trade detection.

## Installation
```bash
pip install pair-sniffer
```

## Example
The input data should be in the form of `numpy` arrays with the following fields: `[timestamp, symbol, volume, price, buy_broker, sell_broker]`.

```python
from pair_sniffer import PairSniffer
from pair_sniffer.utils import generate_sample_data

ko = generate_sample_data("KO")
pep = generate_sample_data("PEP")

ps = PairSniffer(ko, pep, 2)

is_pairs_trade, mean_coherence, opposite_direction, price_divergence = ps.detect_pairs_trade()
```