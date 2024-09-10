from abc import ABC, abstractmethod

class Subject(ABC):
    """
    Subjectクラスは、オブザーバーを管理し、状態が変更された際に通知します。
    オブザーバーの登録、削除、通知のメソッドを定義します。
    """
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        オブザーバーを登録します。
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        オブザーバーを削除します。
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """
        すべての登録されたオブザーバーに対して状態変更を通知します。
        """
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    """
    ConcreteSubjectクラスは具体的なSubjectで、特定の状態を持ちます。
    状態が変更されると、attachされているオブザーバーに通知します。
    """
    def __init__(self, state=0):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer(ABC):
    """
    Observerインターフェースは、Subjectから通知を受け取るオブジェクトが実装すべきメソッドを定義します。
    """
    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserverA(Observer):
    """
    ConcreteObserverAはObserverの具体的な実装で、Subjectの状態変更に応じて行動を更新します。
    """
    def update(self, subject):
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    """
    ConcreteObserverBは別のObserverの具体的な実装で、異なる条件で行動を更新します。
    """
    def update(self, subject):
        if subject.state >= 3:
            print("ConcreteObserverB: Reacted to the event")

# クライアントコード
subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.state = 2
subject.state = 3
