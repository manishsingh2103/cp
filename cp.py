class Node :
    def __init__(self,data,left=None,right=None):
        self.value=data
        self.left=left
        self.right=right

    def getnode(self,data):
        return Node(data)

    def insert(self,data):
        temp_node=self.getnode(data)

        if self.value <= data :
            if self.right :
                self.right.insert(data)
            else :
                self.right=temp_node
        else :
            if self.left:
                self.left.insert(data)
            else:
                self.left = temp_node

    def printTree(self, level=0):
        if self != None:

            if self.right :
                self.right.printTree( level + 1)
            print(' ' * 4 * level , self.value)
            if self.left :
                self.left.printTree( level + 1)

    def find_max_right(self) :
        print('self.value : '+str(self.value))
        if self.left :
            # print(self.value)
            return self.left.value
        elif self.right :
            # print(self.value)
            return self.right.find_max_right()
        else :
            # print(self.value)
            return self.value

    def delete_node(self,val):
        if val>self.value :
            if self.right :
                self.right=self.right.delete_node(val)
        elif val < self.value:
            if self.left :
                self.left=self.left.delete_node(val)
        else :
            if self.right == None and self.left == None :
                return None
            elif self.right == None:
                return self.left
            elif self.left == None :
                return self.left

            max_left=self.find_max_right()
            # print(max_left)
            self.value=max_left
            self.left=self.left.delete_node(max_left)
        return self



if __name__ == '__main__' :
    root=Node(15)
    root.insert(22)
    root.insert(11)
    root.insert(5)
    root.insert(13)
    root.insert(24)
    root.insert(20)
    root.insert(18)
    root.insert(17)
    root.insert(19)
    root.printTree()
    root.delete_node(17)
    print('*'*10)
    root.printTree()
    # a=root.find_max_right()
    # print(a)
