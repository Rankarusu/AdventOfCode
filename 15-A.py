import heapq

with open("15-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    grid = [list(x) for x in lines]


def get_path():
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows = len(grid)
    cols = len(grid[0])

    #start top left, end bottom right and queue up starting location
    start = (0, 0)
    end = (rows - 1, cols - 1)
    to_visit = [(0, start)]
    visited = {start: 0}
    heapq.heapify(to_visit) # transform to_visit to a heapqueue. this makes sure the queue is always ordered. Our priority queue
    
    while to_visit:
        current_prio, current_location = heapq.heappop(to_visit)

        if current_location == end:
            break #exit when we hit the end

        row, col = current_location[0], current_location[1]

        for xoffset, yoffset in dirs: # check adjacent nodes
            new_row = row + xoffset
            new_col = col + yoffset
            
            if 0 <= new_row < rows and 0 <= new_col < cols: # make sure we dont go out of bounds.
                weight = int(grid[new_row][new_col]) #weight is the integer in the grid
                new_distance = visited[current_location] + weight # the updated distance to the current node
                new_location = (new_row, new_col)
                
                if (new_location in visited and new_distance < visited[new_location]) or new_location not in visited:
                    visited[new_location] = new_distance # add visited node or update it if shorter way has been found

                    heapq.heappush(to_visit, (new_distance, new_location)) #check the new node as well

    return visited[end]

result = get_path()
print(result)