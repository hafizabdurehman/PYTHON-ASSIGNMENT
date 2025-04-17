import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
ERASER_SIZE = 40

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser Canvas")

# Create grid
grid = [[BLUE for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    """Draws the grid on the screen."""
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    """Erases cells by setting them to white when the eraser moves over them."""
    for row in range(ROWS):
        for col in range(COLS):
            cell_x, cell_y = col * CELL_SIZE, row * CELL_SIZE
            if x < cell_x + CELL_SIZE and x + ERASER_SIZE > cell_x and y < cell_y + CELL_SIZE and y + ERASER_SIZE > cell_y:
                grid[row][col] = WHITE

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position and erase
    if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
        mouse_x, mouse_y = pygame.mouse.get_pos()
        erase(mouse_x, mouse_y)
    
    pygame.display.flip()

pygame.quit()