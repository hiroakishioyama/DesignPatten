from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """
    AbstractFactoryクラスは、具体的なファクトリーが実装するべき抽象メソッドを定義します。
    これにより、異なるファミリーの製品を作成するためのインターフェースが提供されます。
    """
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    """
    ConcreteFactory1はAbstractFactoryの一種で、特定の製品ファミリーを生成します。
    """
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    """
    ConcreteFactory2もAbstractFactoryの一種で、別の製品ファミリーを生成します。
    """
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

class AbstractProductA(ABC):
    """
    AbstractProductAは製品Aのインターフェースを定義します。
    すべての具体的な製品Aはこのインターフェースを実装する必要があります。
    """
    @abstractmethod
    def useful_function_a(self):
        pass

class AbstractProductB(ABC):
    """
    AbstractProductBは製品Bのインターフェースを定義します。
    すべての具体的な製品Bはこのインターフェースを実装する必要があります。
    """
    @abstractmethod
    def useful_function_b(self):
        pass

class ProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."

class ProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

class ProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."

class ProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

def client_code(factory: AbstractFactory):
    """
    client_code関数はAbstractFactoryインターフェースを通じて製品を生成します。
    この関数はファクトリーの型に依存せず、異なるファクトリーによって生成される製品の
    操作を行います。
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")

# 具体的なファクトリーを使用してクライアントコードをテスト
factory1 = ConcreteFactory1()
client_code(factory1)

print("\n")

factory2 = ConcreteFactory2()
client_code(factory2)
