import pygame
import os

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Peternakan Sapi")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (150, 200, 100)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Load gambar (placeholder grafis kartun)
cow_image = pygame.Surface((80, 80))
cow_image.fill((255, 255, 255))
pygame.draw.circle(cow_image, (0, 0, 0), (40, 40), 30)  # kepala

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(GREEN)

# Font
font = pygame.font.SysFont(None, 36)

# Data Game
money = 100
cows = 1
milk = 0
food = 5
barn_level = 1
day = 1
time_counter = 0

# Fungsi menggambar teks
def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Fungsi logika produksi susu
def produce_milk():
    global milk, food
    if food >= cows:
        milk += cows * 2
        food -= cows

# Fungsi jual susu
def sell_milk():
    global milk, money
    money += milk * 5
    milk = 0

# Fungsi beli makanan
def buy_food():
    global money, food
    if money >= 10:
        money -= 10
        food += 5

# Fungsi beli sapi
def buy_cow():
    global money, cows
    if money >= 50:
        money -= 50
        cows += 1

# Fungsi upgrade kandang
def upgrade_barn():
    global money, barn_level
    if money >= 100:
        money -= 100
        barn_level += 1

# Game Loop
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
    draw_text(f"Makanan: {food}", 10, 90)
    draw_text(f"Sapi: {cows}", 10, 130)
    draw_text(f"Kandang Lv: {barn_level}", 10, 170)
    draw_text(f"Hari: {day}", 10, 210)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                produce_milk()
            elif event.key == pygame.K_s:
                sell_milk()
            elif event.key == pygame.K_f:
                buy_food()
            elif event.key == pygame.K_c:
                buy_cow()
            elif event.key == pygame.K_u:
                upgrade_barn()

    # Sistem waktu (naik hari tiap 10 detik)
    time_counter += 1
    if time_counter >= FPS * 10:
        day += 1
        time_counter = 0

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
