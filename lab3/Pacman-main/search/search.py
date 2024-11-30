"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """Solves the tinyMaze for demonstration purposes."""
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    from util import Stack
    fringe = Stack()  # LIFO stack for DFS
    visited = set()

    # Push the initial state into the fringe with an empty path
    start_state = problem.getStartState()
    fringe.push((start_state, []))  # (current_state, path_to_state)

    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        # Check if the state is the goal
        if problem.isGoalState(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)

            # Expand and add successors
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []  # If no solution is found


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    fringe = Queue()  # FIFO queue for BFS
    visited = set()

    # Push the initial state into the fringe with an empty path
    start_state = problem.getStartState()
    fringe.push((start_state, []))  # (current_state, path_to_state)

    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        # Check if the state is the goal
        if problem.isGoalState(current_state):
            return path  # Return the path to the goal

        if current_state not in visited:
            visited.add(current_state)

            # Expand and add successors
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []  # If no solution is found


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    fringe = PriorityQueue()  # Priority queue for UCS
    visited = set()

    # Push the initial state with a cost of 0
    start_state = problem.getStartState()
    fringe.push((start_state, []), 0)  # (current_state, path_to_state), priority (cost)

    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        # Check if the state is the goal
        if problem.isGoalState(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)

            # Expand and add successors with updated costs
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    new_cost = problem.getCostOfActions(path + [action])
                    fringe.push((successor, path + [action]), new_cost)

    return []


def nullHeuristic(state, problem=None):
    """A trivial heuristic function."""
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    fringe = PriorityQueue()
    visited = set()

    # Push the initial state with a cost of 0 + heuristic
    start_state = problem.getStartState()
    fringe.push((start_state, []), 0 + heuristic(start_state, problem))

    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        # Check if the state is the goal
        if problem.isGoalState(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)

            # Expand and add successors with updated costs and heuristics
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    new_cost = problem.getCostOfActions(path + [action]) + heuristic(successor, problem)
                    fringe.push((successor, path + [action]), new_cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
