class DrawData:
    def __init__(self, val, is_left, is_right, coordinate):
        self.val = val
        self.is_left = is_left
        self.is_right = is_right
        self.coordinate = coordinate


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
            is_left = temp.left != None
            is_right = temp.right != None
            res.append(DrawData(temp.val, is_left, is_right, temp.coordinate))

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res
