from collections import deque
from typing import List, Tuple, Dict, Iterable, Optional

DAY, NIGHT = 0, 1

def findSafestPath(start: int, end: int, intersections: List[Tuple[int, int, int]]) -> List[int]:
    def state_augmented_bfs(start_states, is_goal, get_neighbors):
        queue = deque(start_states)
        visited = set(start_states)
        parent = {s: None for s in start_states}

        while queue:
            state = queue.popleft()
            if is_goal(state):
                return parent, state

            for nxt in get_neighbors(state):
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = state
                    queue.append(nxt)

        return parent, None

    # Build adjacency: adj[u] = [(v, annotation), ...]
    adj= {}
    for a, b, ann in intersections:
        adj.setdefault(a, []).append((b, ann))
        adj.setdefault(b, []).append((a, ann))

    def allowed(annotation: int, t: int) -> bool:
        if annotation == 0:
            return True
        if annotation == 1:      # day-only
            return t == DAY
        if annotation == -1:     # night-only
            return t == NIGHT
        return False

    def is_goal(state: Tuple[int, int]) -> bool:
        u, _t = state
        return u == end

    def get_neighbors(state: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
        u, t = state
        nt = 1 - t

        # wait (sleep)
        yield (u, nt)

        # move if allowed in current time t
        for v, ann in adj.get(u, []):
            if allowed(ann, t):
                yield (v, nt)

    # IMPORTANT: start is implicitly DAY to match Example 1
    parent, goal_state = state_augmented_bfs([(start, DAY)], is_goal, get_neighbors)
    if goal_state is None:
        return []

    # reconstruct state path
    states = []
    cur = goal_state
    while cur is not None:
        states.append(cur)
        cur = parent[cur]
    states.reverse()

    # convert to required output with duplication on waits
    path: List[int] = []
    for i in range(len(states) - 1):
        u, _ = states[i]
        v, _ = states[i + 1]
        path.append(u)
        if u == v:          # wait happened
            path.append(u)  # duplicate

    path.append(states[-1][0])
    return path


print(findSafestPath(0,2,[(0, 1, -1), (1, 2, 0)]))