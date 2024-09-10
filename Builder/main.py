from abc import ABC, abstractmethod

class Builder(ABC):
    """
    Builderクラスは、製品の構築過程の各ステップを定義する抽象基底クラスです。
    具体的なビルダークラスはこのクラスを継承し、具体的なビルドプロセスを実装します。
    """
    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass

class ConcreteBuilder1(Builder):
    """
    ConcreteBuilder1はBuilderの具体的な実装です。
    このクラスは製品の特定の構成を組み立てます。
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")

    def get_product(self):
        product = self._product
        self.reset()
        return product

class Product:
    """
    Productクラスは、ビルダーによって構築される最終的なオブジェクトを表します。
    複数の部品を含めることができ、ビルダーによって段階的に組み立てられます。
    """
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}")

class Director:
    """
    Directorクラスは、ビルダーを使って製品を組み立てるプロセスを制御します。
    このクラスは、特定の構築プロセスを定義し、そのプロセスに従ってビルダーが部品を組み立てるよう指示します。
    """
    def __init__(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self._builder.produce_part_a()

    def build_full_featured_product(self):
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()

# クライアントコード
builder = ConcreteBuilder1()
director = Director(builder)

print("Standard basic product:")
director.build_minimal_viable_product()
builder.get_product().list_parts()

print("\n")

print("Standard full featured product:")
director.build_full_featured_product()
builder.get_product().list_parts()
