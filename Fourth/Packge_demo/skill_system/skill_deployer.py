class SkillDeployer:
    def __init__(self,name) -> None:
        self.name = name
    def SkillDeployer_print_name(self, name):
        print(name)
    
    age = 0

    @staticmethod
    def SkillDeployer_print_age_static():
        print(SkillDeployer.age)

    @classmethod
    def SkillDeployer_print_age(cls):
        print(SkillDeployer.age)