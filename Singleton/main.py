class Singleton:
    """
    Singletonクラスはシングルトンパターンを実装します。
    このクラスのインスタンスはプログラム全体で一つしか存在しないことを保証します。
    """
    _instance = None  # シングルトンインスタンスを保持するクラス変数

    @classmethod
    def get_instance(cls):
        """
        このメソッドはクラスの唯一のインスタンスを返します。
        インスタンスがまだ存在しない場合は、ここで新たに作成します。
        """
        if cls._instance is None:
            cls._instance = cls()  # インスタンスがなければ生成
        return cls._instance

    def __init__(self):
        """
        コンストラクタは外部から直接呼び出されることは想定していません。
        _instanceがNoneでない場合は、新たにインスタンスを作成しようとしていることを示す例外を投げます。
        """
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # 初期化処理はここで行います
            self.state = 0

    def business_logic(self):
        """
        シングルトンクラスのビジネスロジックを実行します。
        このメソッドはシングルトンインスタンスによってのみ呼び出されることを想定しています。
        """
        self.state += 1
        return self.state

# シングルトンインスタンスを取得して利用する
singleton_instance = Singleton.get_instance()
print(singleton_instance.business_logic())  # 処理実行例

# もう一度同じインスタンスを取得する
same_singleton_instance = Singleton.get_instance()
print(same_singleton_instance.business_logic())  # 同じインスタンスであるため、stateがインクリメントされる
