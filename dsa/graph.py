from collections import defaultdict, deque
from typing import Deque, Dict, List, Tuple


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    queue = deque([a])
    visited = set([a])
    level = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node == b:
                return level

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)

        level += 1

    return level


def flood_fill_bfs(r: int, c: int, new_color: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbors(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = coord
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []

        for delta_row, delta_column in deltas:
            neighbor_row = row + delta_row
            neighbor_column = col + delta_column
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_column < num_cols:
                neighbors.append((neighbor_row, neighbor_column))

        return neighbors

    old_color = image[r][c]
    image[r][c] = new_color
    queue = deque([(r, c)])
    visited = set([(r, c)])

    while queue:
        coord = queue.popleft()
        for row, col in get_neighbors(coord):
            if (row, col) in visited:
                continue

            if image[row][col] == old_color:
                image[row][col] = new_color
                queue.append((row, col))

            visited.add((row, col))

    return image


def flood_fill_dfs(r: int, c: int, new_color: int, image: List[List[int]]) -> List[List[int]]:
    old_color = image[r][c]
    image[r][c] = new_color

    for delta_row, delta_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row = r + delta_row
        neighbor_column = c + delta_column
        if 0 <= neighbor_row < len(image) and 0 <= neighbor_column < len(image[0]):
            if image[neighbor_row][neighbor_column] == old_color:
                flood_fill_dfs(neighbor_row, neighbor_column, new_color, image)

    return image


def sink_island(r: int, c: int, grid: List[List[int]]) -> None:
    grid[r][c] = 0

    for delta_row, delta_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row = r + delta_row
        neighbor_column = c + delta_column
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_column < len(grid[0]):
            if grid[neighbor_row][neighbor_column] == 1:
                sink_island(neighbor_row, neighbor_column, grid)


def count_number_of_islands(grid: List[List[int]]) -> int:
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                sink_island(r, c, grid)
                res += 1
    return res


def get_knight_shortest_path(x: int, y: int) -> int | None:
    if (0, 0) == (x, y):
        return 0

    def get_neighbors(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = coord
        deltas = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        return [(row + delta_row, col + delta_col) for delta_row, delta_col in deltas]

    steps = 1
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        for _ in range(len(queue)):
            coord = queue.popleft()

            for neighbor in get_neighbors(coord):
                if neighbor in visited:
                    continue

                if neighbor == (x, y):
                    return steps

                visited.add(neighbor)
                queue.append(neighbor)

        steps += 1


INF = 2147483647


def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    queue: Deque[Tuple[int, int]] = deque()
    num_rows, num_cols = len(dungeon_map), len(dungeon_map[0])

    for r in range(num_rows):
        for c in range(num_cols):
            if dungeon_map[r][c] == 0:
                queue.append((r, c))

    while queue:
        row, col = queue.popleft()
        for delta_row, delta_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if dungeon_map[neighbor_row][neighbor_col] == INF:
                    dungeon_map[neighbor_row][neighbor_col] = dungeon_map[row][col] + 1
                    queue.append((neighbor_row, neighbor_col))
    return dungeon_map


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    def get_neighbors(combo):
        for i in range(4):
            yield combo[0:i] + str((int(combo[i]) + 1) % 10) + combo[i + 1 :]
            yield combo[0:i] + str((int(combo[i]) - 1) % 10) + combo[i + 1 :]

    steps = 0
    start = "0000"
    visited = set(trapped_combos)
    visited.add(start)
    queue = deque([start])

    while queue:
        for _ in range(len(queue)):
            combo = queue.popleft()
            if combo == target_combo:
                return steps

            for neighbor in get_neighbors(combo):
                if neighbor in visited:
                    continue

                queue.append(neighbor)
                visited.add(neighbor)

        steps += 1
    return -1


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    if end not in word_list:
        return -1

    def build_patterns(words: List[str]) -> Dict[str, List[str]]:
        patterns = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                patterns[pattern].append(word)
        return patterns

    def get_neighbors(word: str, patterns: Dict[str, List[str]]) -> List[str]:
        neighbors = []
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1 :]
            neighbors.extend(patterns[pattern])
        return neighbors

    steps = 0
    queue = deque([begin])
    visited = set([begin])
    patterns = build_patterns(word_list)

    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == end:
                return steps

            for neighbor in get_neighbors(word, patterns):
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)

        steps += 1

    return -1


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    def get_in_degrees() -> Dict[int, int]:
        in_degrees = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1
        return in_degrees

    in_degrees = get_in_degrees()
    res = []
    queue: Deque[int] = deque()

    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        res.append(node)

        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    return res if len(graph) == len(res) else []


def task_scheduling(tasks, requirements):
    graph = {task: [] for task in tasks}  # type: ignore
    for task, dependant in requirements:
        graph[task].append(dependant)
    return topological_sort(graph)


def task_scheduling_with_time(tasks, times, requirements):
    def build_graph():
        graph = {tasks[i]: (times[i], []) for i in range(len(tasks))}  # type: ignore
        for task, dependant in requirements:
            graph[task][1].append(dependant)
        return graph

    def get_in_degrees(graph):
        in_degrees = {node: 0 for node in graph}
        for _, dependant in requirements:
            in_degrees[dependant] += 1
        return in_degrees

    graph = build_graph()
    in_degrees = get_in_degrees(graph)
    queue = deque()  # type: ignore
    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(node)

    result = 0
    temp = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            temp = max(temp, graph[node][0])
            for neighbor in graph[node][1]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        result += temp
        temp = 0
    return result


if __name__ == "__main__":
    # print(shortest_path([[1, 2], [0, 2, 3], [0, 1], [1]], 0, 3))
    # print(
    #     flood_fill_bfs(
    #         2,
    #         2,
    #         9,
    #         [
    #             [0, 1, 3, 4, 1],
    #             [3, 8, 8, 3, 3],
    #             [6, 7, 8, 8, 3],
    #             [12, 2, 8, 9, 1],
    #             [12, 3, 1, 3, 2],
    #         ],
    #     )
    # )

    # print(
    #     flood_fill_dfs(
    #         2,
    #         2,
    #         9,
    #         [
    #             [0, 1, 3, 4, 1],
    #             [3, 8, 8, 3, 3],
    #             [6, 7, 8, 8, 3],
    #             [12, 2, 8, 9, 1],
    #             [12, 3, 1, 3, 2],
    #         ],
    #     )
    # )

    # print(
    #     map_gate_distances(
    #         dungeon_map=[
    #             [INF, -1, 0, INF],
    #             [INF, INF, INF, -1],
    #             [INF, -1, INF, -1],
    #             [0, -1, INF, INF],
    #         ]
    #     )
    # )

    # print(
    #     word_ladder(
    #         "COLD", "WARM", ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
    #     )
    # )

    # print(
    #     topological_sort(
    #         {
    #             1: [],
    #             2: [1],
    #             4: [2],
    #             3: [1],
    #         }
    #     )
    # )

    # print(task_scheduling(["a", "b", "c", "d"], [["a", "b"], ["c", "b"], ["b", "d"]]))

    # print(
    #     task_scheduling_with_time(
    #         ["a", "b", "c", "d"], [1, 1, 2, 1], [["a", "b"], ["c", "b"], ["b", "d"]]
    #     )
    # )

    pass
