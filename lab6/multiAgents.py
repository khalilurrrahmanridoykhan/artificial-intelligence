class MultiAgentSearchAgent:
    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = lookup(evalFn, globals())  # The evaluation function for state evaluation
        self.depth = int(depth)  # Max search depth

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        action, score = self.alphaBeta(0, 0, gameState, float('-inf'), float('inf'))  # Set alpha to negative infinity and beta to positive infinity
        return action

    def alphaBeta(self, curr_depth, agent_index, gameState, alpha, beta):
        """
        Returns the best action and score using the Alpha-Beta pruning algorithm.
        For max player (Pacman, agent_index=0), it maximizes the score and for
        min player (ghosts, agent_index > 0), it minimizes the score.

        :param curr_depth: Current depth of the search tree
        :param agent_index: Index of the current agent (Pacman is 0, ghosts are >= 1)
        :param gameState: The current game state
        :param alpha: The best score for the maximizer found so far
        :param beta: The best score for the minimizer found so far
        :return: The best action and the score for that action
        """
        tmp = curr_depth
        indentation = "  " * curr_depth
        print(f"{indentation}Inside alphaBeta------ curr_depth: {curr_depth} agent_index: {agent_index}")

        # Roll over agent index and increase depth if all agents have played their turn
        if agent_index >= gameState.getNumAgents():
            agent_index = 0
            curr_depth += 1
        
        # Return the evaluation function value if the max depth is reached
        if curr_depth == self.depth:
            return None, self.evaluationFunction(gameState)

        best_action = None

        if agent_index == 0:  # Pacman's turn (Maximizing player)
            best_score = float('-inf')  # Pacman tries to maximize
            for action in gameState.getLegalActions(agent_index):  # Iterate over all legal actions
                next_game_state = gameState.generateSuccessor(agent_index, action)
                _, score = self.alphaBeta(curr_depth, agent_index + 1, next_game_state, alpha, beta)

                # If the score is higher, update best_score and best_action
                if score > best_score:
                    best_score = score
                    best_action = action
                
                # Update alpha
                alpha = max(alpha, best_score)
                
                # Prune if beta <= alpha
                if beta <= alpha:
                    print(f"{indentation}Pruned at curr_depth: {curr_depth} agent_index: {agent_index} action: {action}")
                    break

            return best_action, best_score

        else:  # Ghost's turn (Minimizing player)
            best_score = float('inf')  # Ghosts try to minimize
            for action in gameState.getLegalActions(agent_index):  # Iterate over all legal actions
                next_game_state = gameState.generateSuccessor(agent_index, action)
                _, score = self.alphaBeta(curr_depth, agent_index + 1, next_game_state, alpha, beta)

                # If the score is lower, update best_score and best_action
                if score < best_score:
                    best_score = score
                    best_action = action
                
                # Update beta
                beta = min(beta, best_score)

                # Prune if beta <= alpha
                if beta <= alpha:
                    print(f"{indentation}Pruned at curr_depth: {curr_depth} agent_index: {agent_index} action: {action}")
                    break

            return best_action, best_score
