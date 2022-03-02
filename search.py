# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    start_state = problem.getStartState()
    curr_state = start_state
    curr_succ = problem.getSuccessors(start_state)

    print(f"CURRENT:\t{start_state}")
    print(f"SUCC0:\t{curr_succ[0][0]}")
    
    poss_stack = util.Stack()
    been_set = set()
    been_set.add(start_state)
    
    route = []
    curr_route = []
    curr_cost = 0
        
    for succ in curr_succ:
        succ_route = []
        succ_route.append(succ[1])
        succ_cost = succ[2]
        print(f"SUCCROUTE:\t{succ_route}")
        poss_stack.push((succ, succ_route, succ_cost))
        print(f"NEXT SUCCS:\t{succ}\n")

    while not problem.isGoalState(curr_state[0]):
        (curr_state, curr_route, curr_cost) = poss_stack.pop()
        print(f"CURRENT STATE:\t{curr_state}")
        print(f"ROUTE:\t{curr_route}")
        print(f"BEEN:\t{been_set}")
                
        if problem.isGoalState(curr_state[0]) or (curr_state[0] in been_set):
            continue
        else:
            been_set.add(curr_state[0])
            curr_succ = problem.getSuccessors(curr_state[0])
            for succ in curr_succ:
                if not succ[0] in been_set:
                    print(f"NEXT SUCCS:\t{succ}")
                    succ_route = curr_route + [succ[1]]
                    succ_cost = curr_cost + succ[2]
                    print(f"NEXT SUCCS STUFF:\t{curr_route}\t{succ[1]}")
                    print(f"NEXT SUCCS ROUTE:\t{succ_route}")
                    poss_stack.push((succ, succ_route, succ_cost))
                    
        print("\n")
                            
    # while not poss_stack.isEmpty():
    #     a_succ = poss_stack.pop()
    #     print(a_succ)
    route2return = []
    
    for direc in curr_route:
        if direc == 'North':
            route2return.append(n)
        elif direc == 'South':
            route2return.append(s)
        elif direc == 'East':
            route2return.append(e)
        else:
            route2return.append(w)

    #util.raiseNotDefined()
    print(route2return)
    print(f"COST---{curr_cost}")
    
    return route2return
    
    #util.raiseNotDefined()
    
    # from game import Directions
    # n = Directions.NORTH
    # s = Directions.SOUTH
    # e = Directions.EAST
    # w = Directions.WEST
    
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    # start_state = problem.getStartState()
    # curr_state = start_state
    # curr_succ = problem.getSuccessors(start_state)

    # print(f"CURRENT:\t{start_state}")
    # print(f"SUCC0:\t{curr_succ[0][0]}")
    
    # poss_stack = util.Stack()
    # been_set = set()
    # been_set.add(start_state)
    
    # route = []
    # curr_route = []
        
    # for succ in curr_succ:
    #     succ_route = []
    #     succ_route.append(succ[1])
    #     print(f"SUCCROUTE:\t{succ_route}")
    #     poss_stack.push((succ, succ_route))
    #     print(f"NEXT SUCCS:\t{succ}\n")

    # while problem.isGoalState(curr_state[0]):
    #     (curr_state, curr_route) = poss_stack.pop()
    #     print(f"CURRENT STATE:\t{curr_state}")
    #     print(f"ROUTE:\t{curr_route}")
    #     print(f"BEEN:\t{been_set}")
                
    #     if problem.isGoalState(curr_state[0]) or (curr_state[0] in been_set):
    #         continue
    #     else:
    #         been_set.add(curr_state[0])
    #         curr_succ = problem.getSuccessors(curr_state[0])
    #         for succ in curr_succ:
    #             if not succ[0] in been_set:
    #                 print(f"NEXT SUCCS:\t{succ}")
    #                 succ_route = curr_route + [succ[1]]
    #                 print(f"NEXT SUCCS STUFF:\t{curr_route}\t{succ[1]}")
    #                 print(f"NEXT SUCCS ROUTE:\t{succ_route}")
    #                 poss_stack.push((succ, succ_route))
                    
    #     print("\n")
                            
    # # while not poss_stack.isEmpty():
    # #     a_succ = poss_stack.pop()
    # #     print(a_succ)
    # route2return = []
    
    # for direc in curr_route:
    #     if direc == 'North':
    #         route2return.append(n)
    #     elif direc == 'South':
    #         route2return.append(s)
    #     elif direc == 'East':
    #         route2return.append(e)
    #     else:
    #         route2return.append(w)

    # #util.raiseNotDefined()
    # print(route2return)
    
    # return route2return

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    start_state = problem.getStartState()
    curr_state = start_state
    curr_succ = problem.getSuccessors(start_state)

    print(f"CURRENT:\t{start_state}")
    print(f"SUCC0:\t{curr_succ[0][0]}")
    
    poss_queue = util.Queue()
    been_set = set()
    been_set.add(start_state)
    
    route = []
    curr_route = []
        
    for succ in curr_succ:
        succ_route = []
        succ_route.append(succ[1])
        print(f"SUCCROUTE:\t{succ_route}")
        poss_queue.push((succ, succ_route))
        print(f"NEXT SUCCS:\t{succ}\n")

    while not problem.isGoalState(curr_state[0]):
        (curr_state, curr_route) = poss_queue.pop()
        print(f"CURRENT STATE:\t{curr_state}")
        print(f"ROUTE:\t{curr_route}")
        print(f"BEEN:\t{been_set}")
                
        if problem.isGoalState(curr_state[0]) or (curr_state[0] in been_set):
            continue
        else:
            been_set.add(curr_state[0])
            curr_succ = problem.getSuccessors(curr_state[0])
            for succ in curr_succ:
                if not succ[0] in been_set:
                    print(f"NEXT SUCCS:\t{succ}")
                    succ_route = curr_route + [succ[1]]
                    print(f"NEXT SUCCS STUFF:\t{curr_route}\t{succ[1]}")
                    print(f"NEXT SUCCS ROUTE:\t{succ_route}")
                    poss_queue.push((succ, succ_route))
                    
        print("\n")
                            
    # while not poss_queue.isEmpty():
    #     a_succ = poss_queue.pop()
    #     print(a_succ)
    route2return = []
    
    for direc in curr_route:
        if direc == 'North':
            route2return.append(n)
        elif direc == 'South':
            route2return.append(s)
        elif direc == 'East':
            route2return.append(e)
        else:
            route2return.append(w)

    #util.raiseNotDefined()
    print(route2return)
    
    return route2return
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
