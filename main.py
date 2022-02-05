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

        pygame.draw.rect(screen, rect_color, (bound[0], bound[2], bound[1], bound[3]) )

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
    # [minX,maxX,minY,maxY]
    bounds = [float('inf'),-float('inf'), float('inf'),-float('inf')]

    for circle in circles_list:
        if circle['x'] - circle['radius'] < bounds[0]: bounds[0] = circle['x'] - circle['radius']
        if circle['x'] + circle['radius'] > bounds[1]: bounds[1] = circle['x'] + circle['radius']
        if circle['y'] - circle['radius'] < bounds[2]: bounds[2] = circle['y'] - circle['radius']
        if circle['y'] + circle['radius'] > bounds[3]: bounds[3] = circle['y'] + circle['radius']

    return bounds



def resolve_task(circles_list):
    geometric_center = get_center([ (circle["x"], circle["y"]) for circle in circles_list ])
    bounds = get_bounds(circles_list)
    draw_task(bounds, circles_list)




def run_test(test):
    if resolve_task(test['source']) == test['result']:
        return f"'{test['name']}' Completed"
    else:
        return f"'{test['name']}' Failed"


if __name__ == '__main__':
    for test in tests:
        print(run_test(test))




