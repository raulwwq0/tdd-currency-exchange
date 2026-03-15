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

        TODO (workshop): implement this method.
              Hint - look up (from_currency, to_currency) in self._rates
              and raise ValueError when the pair is not found.
        """
        raise NotImplementedError("TODO: implement get_rate in StaticRateProvider")
