from abc import ABC, abstractmethod

class Component(ABC):
    """
    Componentインターフェースは、具体的なコンポーネントとデコレーターが実装するべきメソッドを定義します。
    これにより、デコレーターはコンポーネントのインターフェースに準拠し、互換性を保つことができます。
    """
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    """
    ConcreteComponentクラスは、Componentインターフェースの基本的な実装を提供します。
    これはデコレーターによって拡張される基本的な機能を持っています。
    """
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    """
    Decoratorクラスは、Componentインターフェースを実装し、
    これにコンポーネントへの参照を持ちます。デコレーターはコンポーネントの振る舞いを
    拡張または変更することができます。
    """
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    """
    ConcreteDecoratorAはDecoratorを継承し、特定の振る舞いを追加してコンポーネントの操作を拡張します。
    """
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """
    ConcreteDecoratorBは別の具体的なデコレーターで、異なる振る舞いを追加します。
    """
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# クライアントコード
component = ConcreteComponent()
decorator1 = ConcreteDecoratorA(component)
decorator2 = ConcreteDecoratorB(decorator1)

print(decorator2.operation())
