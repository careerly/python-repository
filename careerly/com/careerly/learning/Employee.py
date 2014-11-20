# -*- coding: utf-8 -*-
# 创建对象，并使用对象
__author__ = 'shengyahuang'


# 定义对象
class Employee:
    """定义雇员类，用于存储雇员信息"""

    __count = 10  # 私有变量
    # 定义构造函数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 显示雇员相关信息
    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    # 修改属性
    def update(self, name):
        self.name = name

    # 删除属性
    def delete(self):
        del self.name

    # 访问私有变量
    def getCount(self):
        return self.__count


# 使用对象
def main():
    employee = Employee("careerly", 2000000)
    employee.displayEmployee()
    employee.update("shengya.huang")
    employee.displayEmployee()
    print "Count:", employee.getCount()

    print "Employee.__doc__:", Employee.__doc__
    print "Employee.__name__:", Employee.__name__
    print "Employee.__module__:", Employee.__module__
    print "Employee.__bases__:", Employee.__bases__
    print "Employee.__dict__:", Employee.__dict__

# 调用
main()
