import pygame

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Peternakan Sapi")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Gambar latar dan sapi (sementara kotak putih)
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((150, 200, 100))  # Hijau rumput

cow_image = pygame.Surface((80, 80))
cow_image.fill((255, 255, 255))  # Sapi putih kotak

# Data game
money = 100
cows = 1
milk = 0
day = 1

font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    # Gambar sapi
    for i in range(cows):
        x = 100 + (i % 5) * 100
        y = 200 + (i // 5) * 100
        screen.blit(cow_image, (x, y))

    # HUD
    draw_text(f"Uang: ${money}", 10, 10)
    draw_text(f"Susu: {milk}", 10, 50)
    draw_text(f"Sapi: {cows}", 10, 90)
    draw_text(f"Hari: {day}", 10, 130)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
