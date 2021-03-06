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
    
    start_node = (problem.getStartState(), "start", 0)
    # node contains (location, route to get there, cost to get there)
    
    dfs_stack = util.Stack()
    # stack of nodes to be used for Depth First Search
    been_state_set = set()
    # set of previously checked states
    been_state_set.add(start_node[0])

    for successor in problem.getSuccessors(start_node[0]):
        dfs_stack.push((successor[0], [successor[1]], successor[2]))

    current_node = dfs_stack.pop()

    while not problem.isGoalState(current_node[0]):
        # loop while not in goal state
        current_state = current_node[0]
        current_route = current_node[1]
        current_cost = current_node[2]

        if not (current_state in been_state_set):
            # check if current state was already checked
            # if not check successors
            been_state_set.add(current_state)
            current_successors = problem.getSuccessors(current_state)
            for successor_node in current_successors:
                if not (successor_node[0] in been_state_set):
                    # calculate route and cost
                    successor_route = current_route + [successor_node[1]]
                    successor_cost = current_cost + successor_node[2]
                    dfs_stack.push((successor_node[0], successor_route, successor_cost))
                    # add successor node to stack
        
        current_node = dfs_stack.pop()
        # pop next node to check
                            
    route_to_return = current_node[1]

    return route_to_return

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    start_node = (problem.getStartState(), "start", 0)
    
    bfs_queue = util.Queue()
    # queue of nodes to be used for Breadth First Search
    been_state_set = set()
    been_state_set.add(start_node[0])

    for successor in problem.getSuccessors(start_node[0]):
        bfs_queue.push((successor[0], [successor[1]], successor[2]))

    current_node = bfs_queue.pop()

    while not problem.isGoalState(current_node[0]):
        current_state = current_node[0]
        current_route = current_node[1]
        current_cost = current_node[2]

        if not (current_state in been_state_set):
            been_state_set.add(current_state)
            current_successors = problem.getSuccessors(current_state)
            for successor_node in current_successors:
                if not (successor_node[0] in been_state_set):
                    successor_route = current_route + [successor_node[1]]
                    successor_cost = current_cost + successor_node[2]
                    bfs_queue.push((successor_node[0], successor_route, successor_cost))
        
        current_node = bfs_queue.pop()
                            
    route_to_return = current_node[1]

    return route_to_return
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    start_node = (problem.getStartState(), "start", 0)
    
    ucs_queue = util.PriorityQueue()
    # uniform cost search uses priority queue
    been_state_set = set()
    been_state_set.add(start_node[0])

    for successor in problem.getSuccessors(start_node[0]):
        ucs_queue.update((successor[0], [successor[1]], successor[2]), successor[2])
        # priority is set as the cost to reach the node

    current_node = ucs_queue.pop()

    while not problem.isGoalState(current_node[0]):
        current_state = current_node[0]
        current_route = current_node[1]
        current_cost = current_node[2]

        if not (current_state in been_state_set):
            been_state_set.add(current_state)
            current_successors = problem.getSuccessors(current_state)
            for successor_node in current_successors:
                if not (successor_node[0] in been_state_set):

                    successor_route = current_route + [successor_node[1]]

                    successor_cost = current_cost + successor_node[2]
                    ucs_queue.update((successor_node[0], successor_route, successor_cost), successor_cost)
                    # priority is set as the cost to reach the node
        
        current_node = ucs_queue.pop()
        # new node popped based on lowest priority value
                            
    route_to_return = current_node[1]

    return route_to_return

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    start_node = (problem.getStartState(), "start", 0)
    
    astar_queue = util.PriorityQueue()
    # priority queue for astar
    been_state_set = set()
    been_state_set.add(start_node[0])

    for successor in problem.getSuccessors(start_node[0]):
        astar_priority = successor[2]+heuristic(successor[0], problem)
        astar_queue.update((successor[0], [successor[1]], successor[2]), astar_priority)
        # priority set as cost to reach node PLUS heuristic value

    current_node = astar_queue.pop()

    while not problem.isGoalState(current_node[0]):
        current_state = current_node[0]
        current_route = current_node[1]
        current_cost = current_node[2]

        if not (current_state in been_state_set):
            been_state_set.add(current_state)
            current_successors = problem.getSuccessors(current_state)
            for successor_node in current_successors:
                if not (successor_node[0] in been_state_set):

                    successor_route = current_route + [successor_node[1]]

                    successor_cost = current_cost + successor_node[2]

                    astar_priority = successor_cost + heuristic(successor_node[0], problem)
                    astar_queue.update((successor_node[0], successor_route, successor_cost), astar_priority)
                    # priority set as cost to reach node PLUS heuristic value
        current_node = astar_queue.pop()
    route_to_return = current_node[1]

    return route_to_return


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
