from collections.abc import Iterable, Iterator
from typing import List

class ConcreteAggregate(Iterable):
    """
    ConcreteAggregateは具体的な集合体で、イテレーターを生成します。
    このクラスはリストを内部状態として持ち、このリストの要素に順番にアクセスするためのイテレーターを提供します。
    """
    def __init__(self, collection: List[any]):
        self._collection = collection

    def __iter__(self) -> Iterator:
        """
        __iter__メソッドは集合体のイテレータを返します。
        """
        return ConcreteIterator(self._collection)

class ConcreteIterator(Iterator):
    """
    ConcreteIteratorはコレクションの要素にアクセスする具体的なイテレータです。
    現在の位置を追跡し、コレクションの次の要素へのアクセスを提供します。
    """
    def __init__(self, collection: List[any]):
        self._collection = collection
        self._index = 0

    def __next__(self):
        """
        __next__メソッドはコレクションの次の要素を返します。
        すべての要素が走査された後は、StopIteration例外を発生させます。
        """
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()

# クライアントコード
aggregate = ConcreteAggregate([1, 2, 3, 4, 5])
for item in aggregate:
    print(item)
