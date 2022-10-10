import bll
import model

class StudentManagerView:
    '''
    学生管理器视图
    '''

    # 跨类调用，构建对象
    def __init__(self):
        self.__manager = bll.StudentManagerController()

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
        stu = model.StudentModel(name,age,score)
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
        stu = model.StudentModel()
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