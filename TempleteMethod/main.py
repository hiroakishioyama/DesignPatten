from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        """テンプレートメソッドは、アルゴリズムの骨組みを定義します。
        サブクラスで一部のステップをカスタマイズ可能にして、フレキシビリティを提供します。"""
        self.base_operation1()  # 基本的な操作1
        self.required_operations1()  # 必須の操作1（サブクラスで定義が必要）
        self.base_operation2()  # 基本的な操作2
        self.hook1()  # フック1（オーバーライド可能、必須ではない）
        self.required_operations2()  # 必須の操作2（サブクラスで定義が必要）
        self.base_operation3()  # 基本的な操作3
        self.hook2()  # フック2（オーバーライド可能、必須ではない）

    def base_operation1(self):
        """基本的な操作1: 共通のロジックを提供します。"""
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self):
        """基本的な操作2: サブクラスでのオーバーライドを許容しますが、ここではデフォルトの実装を提供します。"""
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self):
        """基本的な操作3: もう一度、共通のロジックを実行します。"""
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self):
        """抽象メソッド: 必須の操作1, サブクラスで具体的な実装を提供する必要があります。"""
        pass

    @abstractmethod
    def required_operations2(self):
        """抽象メソッド: 必須の操作2, サブクラスで具体的な実装を提供する必要があります。"""
        pass

    def hook1(self):
        """フック1: サブクラスでオプションとしてオーバーライドすることができます。"""
        pass

    def hook2(self):
        """フック2: サブクラスでオプションとしてオーバーライドすることができます。"""
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        """具体的な必須の操作1の実装を提供します。"""
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self):
        """具体的な必須の操作2の実装を提供します。"""
        print("ConcreteClass1 says: Implemented Operation2")

    def hook1(self):
        """フック1をオーバーライドして、カスタムのロジックを追加します。"""
        print("ConcreteClass1 says: Overridden Hook1")

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        """具体的な必須の操作1の実装を提供します。"""
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self):
        """具体的な必須の操作2の実装を提供します。"""
        print("ConcreteClass2 says: Implemented Operation2")

# テンプレートメソッドの使用
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()

print("\n")

concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
