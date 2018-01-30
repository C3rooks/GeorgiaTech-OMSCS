from SemanticNet import SemanticNet
class ProblemSolver:
    def __init__(self, size, problem):
        self.size = size
        self.problem = problem
        self.net = SemanticNet()

    def BeginSolver(self):
        self.BuildFigureObjects()


    #This method is going to get A and B objects
    def BuildFigureObjects(self):
        figures = self.problem.figures
        figureA = figures['A']
        countAObjects = 0
        for obj in figureA.objects:
            countAObjects += 1

        figureB = figures['B']
        countBObjects = 0
        for obj in figureB.objects:
            countBObjects += 1

        #used to check if shapes have deleted or not.
        self.net.HasShapeDeleted(countAObjects, countBObjects)



    #Build network for A to B
    #Build network for C to ? using transformations of A to B.
    #Handle weights. 
