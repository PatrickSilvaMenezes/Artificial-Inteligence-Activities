from search import *

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


# ________________
class VacuumCleaner(Problem):

    
    def __init__(self, initial, goal):
        self.initial =initial 
        self.goal =   goal
        super().__init__(initial, goal)
    
    def find_agent_square(self, state):
        for agentpos in state:
            if agentpos == (1,1):
                return state.index((1,1))
            elif agentpos == (0,1):
                return state.index((0,1))
        
   

    def actions(self, state):
        possible_actions = ["UP", "DOWN", "LEFT", "RIGHT", "SUCK",]
        index_agent_square = self.find_agent_square(state)
        

        if index_agent_square % 3 == 0:
            possible_actions.remove("LEFT")
        if index_agent_square < 3:
            possible_actions.remove("UP")
        if index_agent_square % 3 == 2:
            possible_actions.remove("RIGHT")
        if index_agent_square > 5:
            possible_actions.remove("DOWN")
       
        return possible_actions
    
    def result(self, state, action):
        agent = self.find_agent_square(state)
        
        new_state = list(state)
        
        if(action == "UP" or action == "DOWN" or action == "RIGHT" or action == "LEFT"):
            delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
            frontier = agent + delta[action]
            if (new_state[frontier][0] == 0):
                new_state[frontier] = (0,1) 
            else:
                new_state[frontier] = (1,1)
            if(new_state[agent][0]==0):
                new_state[agent] = (0,0)
            else:
                new_state[agent] = (1,0)
        else:
            new_state[agent] = (0,1)
        

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal
    

initial =   ((1,0), (1,0), (1,0),
             (0,0), (0,1), (0,0),
             (0,0), (0,0), (0,0))

goal =      ((0,0), (0,0), (0,0),
             (0,0), (0,1), (0,0),
             (0,0), (0,0), (0,0))
problem = VacuumCleaner(initial, goal)
print(breadth_first_graph_search(problem).solution())