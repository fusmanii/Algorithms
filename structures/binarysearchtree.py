class BSTree:
    ''' An implementation of a Binary Search Tree.
    '''

    def __init__(self, value, index, parent=None, left=None, right=None):
        ''' (BSTree, object, float[, BSTree, BSTree]) -> NoneType
        Initializes this node with the given value and index. Optional
        left and right subtries can be supplied.
        '''

        self._value = value
        self.index = index
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        ''' (BSTree) -> str
        String representation of this tree.
        '''

        return self._str().strip('\n')

    def insert(self, value, index):
        ''' (BSTree, object, float) -> NoneType
        Inserts a new node into this tree with value value and
        index index.
        '''

        if index <= self.index:
            if self.left:
                self.left.insert(value, index)
            else:
                self.left = BSTree(value, index, self)
        else:
            if self.right:
                self.right.insert(value, index)
            else:
                self.right = BSTree(value, index, self)

    def remove(self, index):
        ''' (BSTree, float[, BSTree or NoneType]) -> tuple of (object, float)
        Removes and returns the node with index index.
        Does nothing if not node with index index is present.
        '''

        if self.index != index:
            if index <= self.index and self.left:
                self.left.remove(index)
            elif self.right:
                self.right.remove(index)
        else:

            # found the node. have three cases:
            # node has one or no children.
            if not (self.right and self.left):
                if self.parent.right == self:
                    self.parent.right = self.right if self.right else self.left
                    if self.parent.right:
                        self.parent.right.parent = self.parent
                else:
                    self.parent.left = self.right if self.right else self.left
                    if self.parent.left:
                        self.parent.left.parent = self.parent
            
            # node has two childern
            else:
                soccessor = self._soccessor()
                self.index = soccessor.index
                self._value = soccessor._value
                soccessor.remove(soccessor.index)

    def get(self, index):
        ''' (BSTree, float) -> Object
        Returns the value of the node in this binary search tree at index index.
        '''

        if self.index != index:
            if index <= self.index and self.left:
                return self.left.get(index)
            elif self.right:
                return self.right.get(index)
        else:
            return self._value

    def preorder(self):
        ''' (BSTree) -> list
        Returns a list containing the elements of this BSTree in preorder traversal.
        '''

        return self._preorder()

    def inorder(self):
        ''' (BSTree) -> list
        Returns a list containing the elements of this BSTree in inorder traversal.
        '''

        return self._inorder()

    def postorder(self):
        ''' (BSTree) -> list
        Returns a list containing the elements of this BSTree in postorder traversal.
        '''

        return self._postorder()

    def _preorder(self):

        res = []
        res.append(self._value)
        res += self.left._preorder() if self.left else []
        res += self.right._preorder() if self.right else []
        return res

    def _inorder(self):

        res = []
        res += self.left._inorder() if self.left else []
        res.append(self._value)
        res += self.right._inorder() if self.right else []
        return res

    def _postorder(self):

        res = []
        res += self.left._postorder() if self.left else []
        res += self.right._postorder() if self.right else []
        res.append(self._value)
        return res

    def _soccessor(self):

        return self.left._biggest()

    def _biggest(self):

        return self.right._biggest() if self.right else self
        


    def _str(self, ext=''):
        
        res = self.right._str(ext + '    ') if self.right else ''
        res += ext
        res += str((self._value, self.index)) + '\n\n'
        res += self.left._str(ext + '    ') if self.left else ''
        return res 

if __name__ == "__main__":
    bs = BSTree(6,6)
    bs.insert(7,7)
    bs.insert(8,8)
    bs.insert(1,1)
    bs.insert(0,0)
    bs.insert(3,3)
    bs.insert(2,2)
    bs.insert(5,5)
    bs.insert(4,4)

    print(bs)
    bs.remove(1)
    print(bs)
    print(bs.get(7))
    print(bs.postorder())