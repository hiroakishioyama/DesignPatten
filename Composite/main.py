from abc import ABC, abstractmethod

class Component(ABC):
    """
    Componentクラスは、すべてのコンポーネント（葉とコンテナ）が実装すべき共通のインターフェースです。
    このインターフェースを通じて、クライアントは複合オブジェクトと個々のオブジェクトを均一に扱うことができます。
    """
    @abstractmethod
    def operation(self):
        """
        operationはすべての具体的なコンポーネントで実装されるべきメソッドです。
        これにより各コンポーネントの振る舞いを定義します。
        """
        pass

class Leaf(Component):
    """
    Leafクラスは、コンポジット構造の基本要素を表します。
    これは他のオブジェクトを保持できない、コンポジットの「葉」です。
    """
    def operation(self):
        return "Leaf"

class Composite(Component):
    """
    Compositeクラスは複数の子コンポーネントを保持できるコンテナです。
    これはComponentのインターフェースを実装し、子コンポーネントをリストとして管理します。
    """
    def __init__(self):
        self._children = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def operation(self):
        """
        operationメソッドは子コンポーネントのoperationを呼び出し、その結果をまとめて返します。
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

# クライアントコード
root = Composite()
root.add(Leaf())
root.add(Leaf())

branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

root.add(branch1)

print(root.operation())
