# from py2neo import Graph, Node, Relationship



#coding:utf-8
from py2neo import Graph,Node,Relationship,NodeMatcher
 
##连接neo4j数据库，输入地址、用户名、密码
# graph = Graph('http://localhost:7474',auth="neo4j")
# graph = Graph("bolt://localhost:7687")
graph = Graph("http://localhost:7474", auth=("neo4j",""))
# sg = Graph("bolt://localhost:7687")
# Graph("http://localhost:7474")
##创建结点

a = Node("hero", name="Clint")  # Node(label, name)
b = Node("hero", name="Natasha")
ab = Relationship(a, "friend", b)
graph.run(ab)  # 创建节点和关系
