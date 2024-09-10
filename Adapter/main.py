class Target:
    """
    Targetクラスはクライアントが使用するドメイン固有のインターフェースを定義します。
    アダプタークラスはこのインターフェースに従って実装されるべきです。
    """
    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    """
    Adapteeクラスは既存のインターフェースを持ち、アダプテーションが必要です。
    このクラスにはクライアントにとって使いづらいインターフェースがあります。
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    """
    AdapterクラスはAdapteeクラスのインターフェースをTargetインターフェースに変換します。
    これにより、AdapteeクラスのインスタンスがTargetインターフェースを実装しているかのように振る舞います。
    """
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

# クライアントコード
def client_code(target: Target):
    """
    クライアントコードはTargetクラスを通じて作業を実行します。
    この関数はAdapterとTargetオブジェクトのどちらも受け入れます。
    """
    print(target.request())

# 既存のクラス（Adaptee）のインスタンスを作成
adaptee = Adaptee()
print("Adaptee: ", adaptee.specific_request())

# アダプターを使用してAdapteeとクライアントコード間の互換性を確保
adapter = Adapter()
client_code(adapter)
