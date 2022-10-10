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