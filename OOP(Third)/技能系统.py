# 依赖倒置
# 父不依赖于子，抽象不依赖于具体
# 通过依赖注入的方式，注入文件，读取配置文件，用eval()来创建对象   
class SkillImpactEffect:
    def effect(self):
        raise NotImplementedError("没继承")
    
class ImpactEffect:
    pass