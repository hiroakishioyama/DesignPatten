from abc import ABC, abstractmethod

class Command(ABC):
    """
    Commandインターフェースは、実行されるすべてのコマンドが持つべきexecuteメソッドを定義します。
    これにより、コマンドのクライアントは実行するコマンドの具体的な種類を知る必要がなくなります。
    """
    @abstractmethod
    def execute(self):
        pass

class Light:
    """
    Lightクラスは、この例でのレシーバであり、実際のアクション（例えば点灯と消灯）を持つクラスです。
    """
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class TurnOnCommand(Command):
    """
    TurnOnCommandはCommandを実装し、特定のレシーバ（Light）のturn_onメソッドを呼び出します。
    """
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

class TurnOffCommand(Command):
    """
    TurnOffCommandはCommandを実装し、特定のレシーバ（Light）のturn_offメソッドを呼び出します。
    """
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

class RemoteControl:
    """
    RemoteControlは、コマンドオブジェクトを保持し、そのexecuteメソッドを呼び出すことでレシーバにアクションを実行させます。
    """
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        if self._command:
            self._command.execute()

# クライアントコード
light = Light()
turn_on_command = TurnOnCommand(light)
turn_off_command = TurnOffCommand(light)

remote = RemoteControl()
remote.set_command(turn_on_command)
remote.press_button()

remote.set_command(turn_off_command)
remote.press_button()
