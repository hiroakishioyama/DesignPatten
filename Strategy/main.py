from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    Strategyクラスは、すべての具体的なストラテジーが実装すべき操作を定義するインターフェースです。
    このインターフェースは、具体的なアルゴリズムの呼び出し方法を指定します。
    """
    @abstractmethod
    def do_algorithm(self, data):
        pass

class ConcreteStrategyA(Strategy):
    """
    ConcreteStrategyAはStrategyクラスの具体的な実装です。
    ここでは、特定のアルゴリズムを提供します。
    """
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    """
    ConcreteStrategyBは別のアルゴリズムを提供するStrategyクラスの実装です。
    このアルゴリズムでは、逆順でデータをソートします。
    """
    def do_algorithm(self, data):
        return sorted(data, reverse=True)

class Context:
    """
    Contextクラスは、ストラテジーに基づいてオペレーションを実行します。
    ストラテジーは実行時にセットされ、必要に応じて交換することができます。
    """
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        """
        実行時にストラテジーを設定または変更します。
        """
        self._strategy = strategy

    def do_some_business_logic(self):
        """
        サンプルデータを使用してストラテジーに定義されたアルゴリズムを実行します。
        """
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

# クライアントコード
context = Context(ConcreteStrategyA())
context.do_some_business_logic()

print("\nSwitch to another strategy:")
context.set_strategy(ConcreteStrategyB())
context.do_some_business_logic()
