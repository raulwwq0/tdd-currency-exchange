"""
Currency Exchange class

This module will contain the currency exchange logic.
Start by writing tests first!
"""


class CurrencyExchange:
    """Handle currency conversion operations."""

    def __init__(self):
        """Initialize the currency exchange."""
        self.exchange_rates = {}

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency to another."""
        if from_currency == to_currency:
            return amount

        key = (from_currency, to_currency)
        if key not in self.exchange_rates:
            raise ValueError(
                f"Exchange rate not found for {from_currency} to {to_currency}"
            )
        rate = self.exchange_rates[key]
        return amount * rate

    def set_exchange_rate(self, from_currency, to_currency, rate):
        """Set the exchange rate from one currency to another."""
        key = (from_currency, to_currency)
        self.exchange_rates[key] = rate

    def get_exchange_rate(self, from_currency, to_currency):
        """Get the exchange rate from one currency to another."""
        key = (from_currency, to_currency)
        return self.exchange_rates[key]
