import pygame
import sys
import os
from datetime import datetime

# === ИНИЦИАЛИЗАЦИЯ PYGAME ===
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock + Music Player + Red Ball")

# === ЗАГРУЗКА ИЗОБРАЖЕНИЙ ===
body = pygame.image.load("/Users/miraszhumatayev/Downloads/mickeyclock.jpeg").convert_alpha()
right_hand = pygame.image.load("/Users/miraszhumatayev/Downloads/min_hand.png").convert_alpha()
left_hand = pygame.image.load("/Users/miraszhumatayev/Downloads/sec_hand.png").convert_alpha()

# === ЦЕНТР ЧАСОВ ===
center = WIDTH // 2, HEIGHT // 2

# === ПЛЕЕР ===
pygame.mixer.init()
music_folder = "/Users/miraszhumatayev/Downloads/music"  # Укажи свою папку
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
is_playing = False

def play_track(index):
    global is_playing
    if playlist:
        pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
        pygame.mixer.music.play()
        is_playing = True

# === КРАСНЫЙ ШАР ===
ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_color = (255, 0, 0)
ball_speed = 20

# === ФУНКЦИЯ ПОВОРОТА ===
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect)

# === ГЛАВНЫЙ ЦИКЛ ===
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))  # Белый фон

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === КЛАВИАТУРНЫЕ КОМАНДЫ ===
    keys = pygame.key.get_pressed()

    # Музыка
    if keys[pygame.K_p]:
        if not is_playing:
            play_track(current_track)
    if keys[pygame.K_s]:
        pygame.mixer.music.stop()
        is_playing = False
    if keys[pygame.K_n]:
        current_track = (current_track + 1) % len(playlist)
        play_track(current_track)
        pygame.time.wait(200)
    if keys[pygame.K_b]:
        current_track = (current_track - 1) % len(playlist)
        play_track(current_track)
        pygame.time.wait(200)

    # Движение шара
    if keys[pygame.K_LEFT] and ball_x - ball_radius - ball_speed >= 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + ball_speed <= WIDTH:
        ball_x += ball_speed
    if keys[pygame.K_UP] and ball_y - ball_radius - ball_speed >= 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + ball_speed <= HEIGHT:
        ball_y += ball_speed

    # === РИСУЕМ ЧАСЫ ===
    now = datetime.now()
    minute = now.minute
    second = now.second

    min_angle = -minute * 6
    sec_angle = -second * 6

    screen.blit(body, body.get_rect(center=center))
    blitRotateCenter(screen, right_hand, center, min_angle)
    blitRotateCenter(screen, left_hand, center, sec_angle)

    # === РИСУЕМ ШАР ===
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
