import copy

class Prototype:
    """
    Prototypeクラスはプロトタイプインスタンスの複製を可能にします。
    このクラスはcloneメソッドを提供し、自身の複製を作成します。
    """
    def __init__(self, value):
        self._value = value

    def clone(self):
        """
        cloneメソッドは自身のディープコピーを作成して返します。
        この例ではcopy.deepcopyを使用していますが、必要に応じてより複雑な複製ロジックを実装できます。
        """
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    """
    ConcretePrototypeは具体的なプロトタイプクラスで、Prototypeを継承しています。
    追加の属性やメソッドを持つことができます。
    """
    def __init__(self, value, category):
        super().__init__(value)
        self.category = category

    def clone(self):
        """
        必要に応じて、cloneメソッドをオーバーライドしてカスタム複製ロジックを提供します。
        この実装では、単に基底クラスのcloneメソッドを呼び出しています。
        """
        return super().clone()

# クライアントコード
original = ConcretePrototype("initial data", "TypeA")
print(f"Original: {original._value}, {original.category}")

cloned = original.clone()
print(f"Cloned: {cloned._value}, {cloned.category}")
