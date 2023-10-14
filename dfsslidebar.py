import copy
def get_blanktile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return [i,j]
            
def traverse(state):
    l=[]
    l.clear()
    x,y=get_blanktile(state)
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

def print_format(state_space):
    for state in state_space:
        print(state[0],end="      ")
    print()
    for state in state_space:
        print(state[1],end='')
        if state!=goal:
            print(' ---> ',end='')
    print()
    for state in state_space:
        print(state[2],end='      ')


def dfs(state,open,closed,parent_list,d,k):
    if d==k:
        return 
    if state not in closed:   
        closed.append(state)    
        children=traverse(state)
        k=k+1
        for child in children:
            parent_list.append([child,state])
            open.insert(0,child)
            dfs(open[0],open,closed,parent_list,d,k)
    return

if __name__=='__main__':
    start=[[2,8,3],[1,6,4],[7,0,5]]
    goal=[[1,2,3],[8,0,4],[7,6,5]]
    
    state=copy.deepcopy(start)
    open=[]
    closed=[]
    parent_list=[]
    d=6
    k=1
    dfs(state,open,closed,parent_list,d,k)
    path=[goal]
    path_state=closed[-1]
    while(path_state!=start):
        path.append(path_state)
        for ele in parent_list:
            if ele[0]==path_state:
                path_state=ele[1]
                break
    path.append(start)
    answer=path[::-1]
    print_format(answer)