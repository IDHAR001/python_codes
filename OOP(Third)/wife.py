class Wife:
    total_count = 0
    def __init__(self) -> None:
        Wife.total_count += 1

    @classmethod
    def print_count(cls):
        print(cls.total_count)



a = Wife()
b = Wife()
c = Wife()
Wife.print_count()
