class EnemyError(Exception):
    def __init__(self,msg,line) -> None:
        super().__init__("报错了")
        self.msg = msg
        self.line = line

class Enemy:
    def __init__(self,atk):
        self.atk = atk
        if 0 <= self.atk <= 100:
            self.atk = atk
        else:
            raise EnemyError("out of atk's range","line = 14")
try:
    e01 = Enemy(1001)
except EnemyError as e:
    print(e.msg)
    print(e.line)
    