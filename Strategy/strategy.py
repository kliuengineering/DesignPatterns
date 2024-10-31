from abc import ABC, abstractmethod
import copy
from typing import List


class Strategy(ABC):
    @abstractmethod
    def execute():
        pass


class ConcreteStrategyA(Strategy):
    def execute(self) -> None:
        print("Executing Strategy A...")


class ConcreteStrategyB(Strategy):
    def execute(self) -> None:
        print("Executing Strategy B...")


class Context:
    def __init__(self, strategy: Strategy | None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute(self) -> None:
        self._strategy.execute()


def main():
    strategy_a = ConcreteStrategyA()
    strategy_b = ConcreteStrategyB()
    context = Context(strategy_a)
    context.execute()
    context.set_strategy(strategy_b)
    context.execute()


if __name__ == "__main__":
    main()
