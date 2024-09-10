class Subsystem1:
    """
    Subsystem1はファサードを通じてアクセスされるシステムの一部です。
    このクラスはファサードの背後にある複雑なロジックをカプセル化します。
    """
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation2(self) -> str:
        return "Subsystem1: Go!"

class Subsystem2:
    """
    Subsystem2もまた、ファサードを通じて利用されるシステムの一部です。
    このクラスは別の役割や責任を持ちます。
    """
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation2(self) -> str:
        return "Subsystem2: Go!"

class Facade:
    """
    Facadeクラスは一つのインターフェースを通じて複数のサブシステムにアクセスする方法を提供します。
    クライアントはファサードを通じてシステムの複雑な部分に簡単にアクセスできます。
    """
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self):
        """
        Facadeのメソッドoperationは、サブシステムのメソッドを協調して呼び出し、
        一連の操作を行います。これによりクライアントは複数のサブシステムを一度に扱う複雑さから解放されます。
        """
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation2())
        results.append(self._subsystem2.operation2())
        return "\n".join(results)

# クライアントコード
def client_code(facade: Facade) -> None:
    """
    クライアントコードはFacadeを通じて複数のサブシステムとのやり取りを行います。
    これにより、クライアントはサブシステムの複雑な部分に直接触れることなく、必要な操作を実行できます。
    """
    print(facade.operation())

subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
client_code(facade)
