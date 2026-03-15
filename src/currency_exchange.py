"""
Currency Exchange class

This module will contain the currency exchange logic.
Start by writing tests first!
"""

from typing import Optional

from src.rate_provider import RateProvider


class CurrencyExchange:
    """Handle currency conversion operations."""

    def __init__(self, rate_provider: Optional[RateProvider] = None):
        """Initialize the currency exchange."""
        self._rate_provider = rate_provider
        self.exchange_rates = {}

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency to another.

        Delegates to the injected RateProvider when available; falls back to
        the internal exchange_rates dict otherwise.
        """
        if from_currency == to_currency:
            return amount

        if self._rate_provider is not None:
            rate = self._rate_provider.get_rate(from_currency, to_currency)
            return amount * rate

        key = (from_currency, to_currency)
        if key not in self.exchange_rates:
            raise ValueError(
                f"Exchange rate not found for {from_currency} to {to_currency}"
            )
        return amount * self.exchange_rates[key]

    def set_exchange_rate(self, from_currency, to_currency, rate):
        """Set the exchange rate from one currency to another."""
        key = (from_currency, to_currency)
        self.exchange_rates[key] = rate

    def get_exchange_rate(self, from_currency, to_currency):
        """Get the exchange rate from one currency to another."""
        key = (from_currency, to_currency)
        return self.exchange_rates[key]
