import heapq

class PuzzleState:
  def __init__(self, board, goal, cost=0, parent=None):
      self.board = board
      self.goal = goal
      self.cost = cost
      self.parent = parent

  def __lt__(self, other):
      return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

  def __eq__(self, other):
      return self.board == other.board

  def __hash__(self):
      return hash(tuple(map(tuple, self.board)))

  def __str__(self):
      return '\n'.join([' '.join(map(str, row)) for row in self.board])

  def get_blank_position(self):
      for i, row in enumerate(self.board):
          for j, tile in enumerate(row):
              if tile == 0:
                  return i, j

  def get_neighbors(self):
      i, j = self.get_blank_position()
      neighbors = []

      for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          ni, nj = i + move[0], j + move[1]
          if 0 <= ni < 3 and 0 <= nj < 3:
              new_board = [row.copy() for row in self.board]
              new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
              neighbors.append(PuzzleState(new_board, self.goal, self.cost + 1, self))

      return neighbors

  def is_goal(self):
      return self.board == self.goal

  def heuristic(self):
      # Manhattan distance heuristic
      h = 0
      for i in range(3):
          for j in range(3):
              if self.board[i][j] != 0:
                  goal_i, goal_j = divmod(self.board[i][j] - 1, 3)
                  h += abs(i - goal_i) + abs(j - goal_j)
      return h


def astar(initial_state):
    open_set = [initial_state]
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            path = []
            while current_state:
                path.insert(0, current_state)
                current_state = current_state.parent
            return path

        closed_set.add(current_state)

        neighbors = current_state.get_neighbors()
        for neighbor in neighbors:
            if neighbor not in closed_set:
                if neighbor not in open_set or neighbor.cost < current_state.cost:
                    heapq.heappush(open_set, neighbor)

    return None


def get_user_input():
    print("Enter the initial state of the puzzle (use 0 for the blank space):")
    initial_board = [list(map(int, input().split())) for _ in range(3)]

    print("Enter the goal state of the puzzle:")
    goal_board = [list(map(int, input().split())) for _ in range(3)]

    return PuzzleState(initial_board, goal_board)


if __name__ == "__main__":
    initial_state = get_user_input()
    print(initial_state)
    solution = astar(initial_state)

    if solution:
        for i, state in enumerate(solution):
            print(f"Step {i}:\n{state}\n")
    else:
        print("No solution found.")
