"""
Rate Provider interface and stub implementations.

Workshop task: implement a concrete RateProvider and wire it into CurrencyExchange.

Steps:
1. Write a failing test for your provider (Red)
2. Implement the provider so the test passes (Green)
3. Refactor as needed (Refactor)
"""

from abc import ABC, abstractmethod
from typing import Optional


class RateProvider(ABC):
    """Abstract base class for exchange rate providers.

    Any concrete provider must implement `get_rate`.
    """

    @abstractmethod
    def get_rate(self, from_currency: str, to_currency: str) -> float:
        """Return the exchange rate from *from_currency* to *to_currency*.

        Args:
            from_currency: ISO 4217 currency code of the source currency (e.g. "USD").
            to_currency:   ISO 4217 currency code of the target currency (e.g. "EUR").

        Returns:
            A positive float representing how many units of *to_currency*
            equal one unit of *from_currency*.

        Raises:
            ValueError: If either currency code is unsupported.
        """


class StaticRateProvider(RateProvider):
    """A simple rate provider backed by a fixed in-memory table.

    Workshop attendants: fill in `get_rate` using the `_rates` dict below,
    then write tests that drive the behaviour you want to support.

    Example rates dict structure:
        {
            ("USD", "EUR"): 0.92,
            ("EUR", "USD"): 1.09,
            ...
        }
    """

    def __init__(self, rates: Optional[dict[tuple[str, str], float]] = None):  # pyright: ignore[reportIndexIssue]
        """Initialise the provider with an optional rates table.

        Args:
            rates: Mapping of (from_currency, to_currency) tuples to rates.
                   Defaults to an empty table.
        """
        self._rates: dict[tuple[str, str], float] = rates or {}

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        """Return the rate for the given currency pair.

        Args:
            from_currency: ISO 4217 currency code of the source currency.
            to_currency:   ISO 4217 currency code of the target currency.

        Returns:
            1.0 when both currencies are the same; otherwise the rate from
            the internal table.

        Raises:
            ValueError: If the pair is not present in the rates table.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return 1.0

        pair = (from_currency, to_currency)
        if pair not in self._rates:
            raise ValueError(f"No rate available for {from_currency} -> {to_currency}")
        return self._rates[pair]
