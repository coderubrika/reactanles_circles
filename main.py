import json, pygame

with open('test.json') as f:
    tests = json.loads(f.read())["tests"]


def draw_task(bound, circles_list):
    (width, height) = (500, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    running = True

    background_colour = (255, 255, 255)

    rect_color = (255, 0, 0)
    circle_color = (0, 255, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_colour)

        pygame.draw.rect(screen, rect_color, (bound[0], bound[1], bound[2], bound[3]) )

        for circle in circles_list:
            pygame.draw.circle(screen, circle_color, (circle['x'], circle['y']), circle['radius'])

        pygame.display.update()

def get_center(coords):
    geometric_center = (
        sum([coord[0] for coord in coords]) / len(coords),
        sum([coord[1] for coord in coords]) / len(coords)
    )

    return geometric_center


def get_bounds(circles_list):
    # [minX,minY,maxX,maxY]
    bounds = [float('inf'),float('inf'), -float('inf'),-float('inf')]

    for circle in circles_list:
        if circle['x'] - circle['radius'] < bounds[0]: bounds[0] = circle['x'] - circle['radius']
        if circle['y'] - circle['radius'] < bounds[1]: bounds[1] = circle['y'] - circle['radius']
        if circle['x'] + circle['radius'] > bounds[2]: bounds[2] = circle['x'] + circle['radius']
        if circle['y'] + circle['radius'] > bounds[3]: bounds[3] = circle['y'] + circle['radius']

    return bounds


def intersection_area(rect1, rect2):
    left = max(rect1[0], rect2[0])
    top = min(rect1[3], rect2[3])
    right = min(rect1[2], rect2[2])
    bottom = max(rect1[1], rect2[1])

    width = right - left
    height = top - bottom

    if width < 0 or height < 0:
        return 0

    return width * height


def get_squares_from_circles(circles_list):
    squares = []

    for circle in circles_list:
        rect = [None,None,None,None]
        rect[0] = circle['x'] - circle['radius']
        rect[1] = circle['y'] - circle['radius']
        rect[2] = circle['x'] + circle['radius']
        rect[3] = circle['y'] + circle['radius']

        squares.append(rect)

    return squares


def get_bounds_sqr(squares):
    # [minX,minY,maxX,maxY]
    bounds = [float('inf'), float('inf'), -float('inf'), -float('inf')]

    for square in squares:
        if square[0] < bounds[0]: bounds[0] = square[0]
        if square[1] < bounds[1]: bounds[1] = square[1]
        if square[2] > bounds[2]: bounds[2] = square[2]
        if square[3] > bounds[3]: bounds[3] = square[3]

    return bounds


def resolve_task(circles_list):
    geometric_center = get_center([ (circle["x"], circle["y"]) for circle in circles_list ])
    bounds = get_bounds(circles_list)

    draw_task(bounds, circles_list)

    squares = get_squares_from_circles(circles_list)

    #генетический алгоритм должен определить как заполнить группы
    # пример groups = [[0],[1,2]] [[0, 1],[2]] [[0, 2],[1]]
    # нужен метод который сможет найти общую площадь

    groups = [[],[]]


def run_test(test):
    if resolve_task(test['source']) == test['result']:
        return f"'{test['name']}' Completed"
    else:
        return f"'{test['name']}' Failed"


if __name__ == '__main__':
    for test in tests:
        print(run_test(test))




