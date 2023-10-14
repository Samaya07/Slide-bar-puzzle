import copy
class Problem:
    def __init__(self,initial,goal):
        self.initial_state=initial
        self.goal=goal
    def goal_test(self,node):
        if node==self.goal:
            return True
    def get_blanktile(self,state):
        for i in range(3):
            for j in range(3):
                if state[i][j]==0:
                    return [i,j]
    def actions(self,state):
        l=[]
        l.clear()
        x,y=self.get_blanktile(state)
        if x==0:
            if y==0:
                state1=copy.deepcopy(state)
                state2=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2[x][y],state2[x+1][y]=state2[x+1][y],state2[x][y]
                l.extend([state1,state2])
            elif y==1:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x][y-1]=state2[x][y-1],state2[x][y]
                state3=copy.deepcopy(state)
                state3[x][y],state3[x+1][y]=state3[x+1][y],state3[x][y]
                l.extend([state1,state2,state3])
            elif y==2:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y-1]=state1[x][y-1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x+1][y]=state2[x+1][y],state2[x][y]
                l.extend([state1,state2])
        elif x==2:
            if y==0:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x-1][y]=state2[x-1][y],state2[x][y]
                l.extend([state1,state2])
            elif y==1:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x][y-1]=state2[x][y-1],state2[x][y]
                state3=copy.deepcopy(state)
                state3[x][y],state3[x-1][y]=state3[x-1][y],state3[x][y]
                l.extend([state1,state2,state3])
            elif y==2:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y-1]=state1[x][y-1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x-1][y]=state2[x-1][y],state2[x][y]
                l.extend([state1,state2])
        elif x==1:
            if y==0:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x-1][y]=state2[x-1][y],state2[x][y]
                state3=copy.deepcopy(state)
                state3[x][y],state3[x+1][y]=state3[x+1][y],state3[x][y]
                l.extend([state1,state2,state3])
            elif y==1:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y+1]=state1[x][y+1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x][y-1]=state2[x][y-1],state2[x][y]
                state3=copy.deepcopy(state)
                state3[x][y],state3[x-1][y]=state3[x-1][y],state3[x][y]
                state4=copy.deepcopy(state)
                state4[x][y],state4[x+1][y]=state4[x+1][y],state4[x][y]
                l.extend([state1,state2,state3,state4])
            elif y==2:
                state1=copy.deepcopy(state)
                state1[x][y],state1[x][y-1]=state1[x][y-1],state1[x][y]
                state2=copy.deepcopy(state)
                state2[x][y],state2[x-1][y]=state2[x-1][y],state2[x][y]
                state3=copy.deepcopy(state)
                state3[x][y],state3[x+1][y]=state3[x+1][y],state3[x][y]
                l.extend([state1,state2,state3])
        return l

    def get_loc(self,number):
        for i in range(3):
            for j in range(3):
                if goal[i][j]==number:
                    return [i,j]
            
    def get_cost1(self,state):
        cost=0
        for i in range(3):
            for j in range(3):
                if state[i][j]!=0:
                    x,y=self.get_loc(state[i][j])
                    cost=cost+abs(x-i)+abs(y-j)
    
        return cost
    
    def get_cost2(self,state):
        misplaced_tiles=0
        for i in range(3):
            for j in range(3):
                if state[i][j]!=0:
                    if state[i][j]!=goal[i][j]:
                        misplaced_tiles=misplaced_tiles+1
        return misplaced_tiles
class Child_node:
    def __init__(self,problem,child):
        self.state=child
        self.g=problem.get_cost1(child)
        self.h=problem.get_cost2(child)
        self.f=self.g+self.h
    
class Node:
    def __init__(self, state, g, h):
        self.state = state  # Current state
        self.g = g  # Path cost from the initial state to this state
        self.h = h  # Heuristic estimate of cost from this state to a goal

def recursive_best_first_search(problem):
    # Initialize RBFS with initial node and an infinite f-cost limit
    initial_node = Node(state=problem.initial_state, g=0, h=problem.get_cost2(problem.initial_state))
    path=[]
    result, path = rbfs(problem, initial_node, float('inf'),path)
    return result,path

def rbfs(problem, node, f_limit,path):
    if problem.goal_test(node.state):
        return node, path  # Solution found
    path.append(node)
    successors = []
    for action in problem.actions(node.state):
        child_node = Child_node(problem,action)
        successors.append(child_node)

    if not successors:
        return None, float('inf')  # Failure, return infinity

    while True:
        successors.sort(key=lambda x: x.f)  # Sort by f-value

        best = successors[0]
        if best.f > f_limit:
            return None, best.f  # Failure, return the best's f-value

        alternative = successors[1].f if len(successors) > 1 else float('inf')

        result, best.f = rbfs(problem, best, min(f_limit, alternative),path)
        if result is not None:
            return result, best.f        

def print_format(state_space):
    for node in state_space:
        print(node.state[0],end="      ")
    print()
    for node in state_space:
        print(node.state[1],end='')
        if node.state!=goal:
            print(' ---> ',end='')
    print()
    for node in state_space:
        print(node.state[2],end='      ')
    
def print_format_s(state_space):
    for state in state_space:
        print(state[0],end="          ")
    print()
    for state in state_space:
        print(state[1],end='')
        if state!=goal:
            print('   --->   ',end='')
    print()
    for state in state_space:
        print(state[2],end='          ')

if __name__=='__main__':
    start=[[2,8,3],[1,6,4],[7,0,5]]
    goal=[[1,2,3],[8,0,4],[7,6,5]]
    print("Start state  \t   Goal state  ")
    startgoal=[start,goal]
    print_format_s(startgoal)
    print("\n")
    print("The path from the start to the goal for the given slide bar states using RBFS :")
    print()
    problem=Problem(start,goal)
    result,path=recursive_best_first_search(problem)
    path.append(result)
    print_format(path)