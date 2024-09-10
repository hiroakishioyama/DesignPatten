from abc import ABC, abstractmethod

class Context:
    """
    Contextクラスは、現在の状態を保持し、外部からのリクエストを適切な状態オブジェクトに委譲します。
    状態が変わるたびに、Contextの状態オブジェクトを変更することで振る舞いが変化します。
    """
    def __init__(self, state):
        self._state = None
        self.transition_to(state)

    def transition_to(self, state):
        """
        Contextの状態を切り替えます。このメソッドを通じて新しい状態が設定されます。
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.set_context(self)

    def request1(self):
        """
        状態依存のリクエスト1。現在の状態オブジェクトに委譲されます。
        """
        self._state.handle1()

    def request2(self):
        """
        状態依存のリクエスト2。現在の状態オブジェクトに委譲されます。
        """
        self._state.handle2()

class State(ABC):
    """
    Stateインターフェースは、すべての具体的な状態が実装する必要があるメソッドを定義します。
    各状態はContextを通じてアクセスされ、状態の振る舞いを定義します。
    """
    @abstractmethod
    def set_context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass

class ConcreteStateA(State):
    """
    ConcreteStateAはStateインターフェースの一つの具体的な実装です。
    特定の状態での振る舞いを定義します。
    """
    def set_context(self, context):
        self._context = context

    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self._context.transition_to(ConcreteStateB())

    def handle2(self):
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    """
    ConcreteStateBもStateインターフェースの実装の一つです。
    この状態での異なる振る舞いを提供します。
    """
    def set_context(self, context):
        self._context = context

    def handle1(self):
        print("ConcreteStateB handles request1.")

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self._context.transition_to(ConcreteStateA())

# クライアントコード
context = Context(ConcreteStateA())
context.request1()
context.request2()
