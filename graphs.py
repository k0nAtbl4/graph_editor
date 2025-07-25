class BinaryTree:
    def __init__(self, val, left, right, coordinate):
        self.val = val
        self.left = left
        self.right = right
        self.coordinate = coordinate

    def bfs(self):
        node = self
        if node == None:
            return []

        res = []
        queue = [node]
        print(queue)
        while queue:
            temp = queue.pop(0)
            res.append( (temp.val, (temp.coordinate[0], temp.coordinate[1])) )

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res
