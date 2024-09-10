from abc import ABC, abstractmethod

class Creator(ABC):
    """
    Creatorクラスはファクトリーメソッドを宣言します。
    Creatorのサブクラスはこのメソッドを実装して、具体的な製品を生成します。
    """
    @abstractmethod
    def factory_method(self):
        """
        ファクトリーメソッドは、製品オブジェクトを生成するためのインターフェースを定義します。
        実際のオブジェクトの生成はサブクラスによって行われます。
        """
        pass

    def some_operation(self):
        """
        some_operation() はファクトリーメソッドを使って何かしらの操作を行います。
        このメソッドはファクトリーメソッドによって返されるオブジェクトに依存します。
        """
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    """
    Productクラスは製品が持つべきインターフェースを定義します。
    すべての具体的な製品はこのインターフェースを実装する必要があります。
    """
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self):
        return "{Result of the ConcreteProduct2}"

# クライアントコード
def client_code(creator: Creator):
    print(creator.some_operation())

# 使用例
client_code(ConcreteCreator1())
client_code(ConcreteCreator2())
