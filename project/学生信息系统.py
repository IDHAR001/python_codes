'''
学生管理系统
    项目计划：
        1.数据模型类 StudentModel
        2.创建逻辑控制类 StudentManagerController 
        3.完成数据： 学生列表 __stu_list
        4.行为： 获取学生列表 stu_list
        5.添加学生方法： add_student
        6.根据编号删除学生 remove_student
        7.根据编号修改学生 update_student
        8.在界面视图类中，根据编号删除学生
'''

class StudentModel:
    def __init__(self,name = "",age = 0,score = 0,id = 0):
        self.id = id
        self.name = name
        self.age = age 
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value

class StudentManagerController:
    # 类变量，表示初始编号，被所有对象共享
    __init_id = 0

    def __init__(self):
        self.__stu_list = []
    
    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu_info):
        self.__generate_id(stu_info)
        # self.__stu_list.append(stu_info)    两者都行
        self.stu_list.append(stu_info)
        return self.__stu_list

    def __generate_id(self, stu_info):
        StudentManagerController.__init_id += 1 
        stu_info.id = StudentManagerController.__init_id

    def remove_student(self,id):
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return True
        return False
        
    def update_student(self,stu_info):
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r].score,self.__stu_list[c].score = self.__stu_list[c].score,self.__stu_list[r].score

class StudentManagerView:
    '''
    学生管理器视图
    '''

    # 跨类调用，构建对象
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__remove_student()
        elif item == "4":
            self.__update_student()
        elif item == "5":
            self.__output_by_score(self.__manager.stu_list)

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)

    def __output_student(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __remove_student(self):
        id = int(input("请输入删除学生编号："))
        if self.__manager.remove_student(id):
            print("修改成功")
        else:
            print("修改失败")
    
    def __update_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入想要修改的学生id："))
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        # stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_by_score(self,list_output):
        self.__manager.order_by_score()
        self.__output_student(self.__manager.stu_list)
        
    # 入口
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
            item = input("退出吗？(y/n)")
            if item == "y":
                break
            elif item == "N":
                continue

view = StudentManagerView()
view.main()