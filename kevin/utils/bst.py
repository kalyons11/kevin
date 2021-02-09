"""
BST utils.
"""


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'val={self.val}, left=({self.left}), right=({self.right})'


class BST:

    def __init__(self, root):
        self.root = root

    @staticmethod
    def init_from_list(vals):
        """
        Init a BST from a list of values in the proper order.

        value in vals should be None if empty, otherwise a value of a given
        type of each Node value
        """
        # inspired by https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
        if len(vals) == 0:
            raise ValueError('must have at least one value')

        nodes = [None if val is None else TreeNode(val) for val in vals]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children: node.left = children.pop()
                if children: node.right = children.pop()

        return BST(root)

    def to_list(self):
        """
        Convert BST to list of values using depth-order traversal.

        Just run a BFS!
        """
        out = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current is None:
                out.append(None)
            else:
                out.append(current.val)

            if current is not None:
                queue.append(current.left)
                queue.append(current.right)

        # remove trailing patch of None's
        last_none_index = 1
        for i, val in enumerate(out):
            if val is None and out[i - 1] is not None:
                last_none_index = i

        return out[:last_none_index]

    def __repr__(self):
        return repr(self.root)

    def draw(self):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y-20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x-dx, y-60, dx/2)
                jumpto(x, y-20)
                draw(node.right, x+dx, y-60, dx/2)

        import turtle
        t = turtle.Turtle()
        t.speed(0); turtle.delay(0)
        h = height(self.root)
        jumpto(0, 30*h)
        draw(self.root, 0, 30*h, 40*h)
        t.hideturtle()
        turtle.mainloop()
