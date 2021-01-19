import random

class node:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        if self.parent == None:
            return "Root Node: %s" % str(id(self))
        elif self.value is not None:
            return "Leaf Node: %s from parent %s" % (str(self.value), str(id(self.parent)))
        else:
            return "Node: %s from parent %s" % (str(id(self)), str(id(self.parent)))

    def prints(self, level=0):
        print '\t' * level + str(self) + "  Term: %s" % self.isTerm()
        for child in self.children:
            child.prints(level+1)

    def isTerm(self):
        return len(self.children) is 0

    def populate(self, width, depth):
        if depth is not 1:
            for val in range(width):
                self.children.append(node(None, self))
                self.children[val].populate(width, depth-1)
        else:
            for val in range(width):
                x = input("Leaf node: ")
                self.children.append(node(x, self))

    def RandomPopulate(self, width, depth):
        if depth is not 1:
            for val in range(width):
                self.children.append(node(None, self))
                self.children[val].RandomPopulate(width, depth-1)
        else:
            for val in range(width):
                x = random.randint(1, 20) 
                self.children.append(node(x, self))


class Tree:
    def __init__(self):
        self.root = node()

    def prints(self):
        self.root.prints()
    
    def populate(self, width, depth):
        choice = input("Random: [0] UserInput: [1] ")
        if choice is 1:
            self.root.populate(width, depth)
        else:
            self.root.RandomPopulate(width, depth)

    
INF = 10000000000

def minimax(s, player, alpha, beta):
    if s.isTerm():
        print "Terminal, sending %s" % s.value
        return s.value
    else:
        if player is "MAX":
            #max = -INF
            for child in s.children:
                v = minimax(child, "MIN", alpha, beta)
                print "Val: %s  Alpha: %s  Beta: %s " % (v, alpha, beta)
                if v >= beta:
                    print "v >= beta, breaking loop, return beta"    
                    return beta
                if v > alpha:
                    print "v > alpha"
                    alpha = v
            return alpha
        
        else:
            #min = INF
            for child in s.children:
                v = minimax(child, "MAX", alpha, beta)
                print "Val: %s  Alpha: %s  Beta: %s " % (v, alpha, beta)
                if v <= alpha:
                    print "v <= alpha, breaking loop, return beta"
                    return alpha
                if v < beta:
                    print "v < beta"
                    beta = v
            return beta



if __name__ == '__main__':
    myTree = Tree()
    myTree.populate(10, 54)
    myTree.prints()

    val = minimax(myTree.root, "MAX", -INF, INF)
    print "\nBest that MAX can do: %s" % val

