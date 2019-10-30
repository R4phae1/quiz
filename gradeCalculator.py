
class Student:
    def __init__(self, name, surename, ID, grades, course, ):
        self.fullName = name + ' ' + surename
        self.ID = ID
        self.course = course
        self.grades = grades


class course:
    def __init__(self, nameofcourse, assignments):
        self.nameofcourse = nameofcourse
        self.assignments = assignments

class assignment:
    def __init__(self, name, deadline, grade):
        self.name = name
        self.deadline = deadline
        self.grade = grade

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        current = self.head
        while current:
            print(current.data)
            current = current.getNextNode()