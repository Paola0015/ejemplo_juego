import pygame
import sys

# Inicio
pygame.init()

# Configuro la pantalla
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Esquivando al Enemigo")

# Colores 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configuro el jugador
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 128, 255)
player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 2 * PLAYER_SIZE]
player_speed = 10

# Configuro el enemigos
ENEMY_SIZE = 50
ENEMY_COLOR = RED
enemy_list = [[100, 100], [300, 200], [500, 300]]

# Funciones
def draw_player(player_pos):
    pygame.draw.rect(DISPLAYSURF, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(DISPLAYSURF, ENEMY_COLOR, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

def check_for_collisions(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if (enemy_pos[1] >= player_pos[1] and
            enemy_pos[1] < (player_pos[1] + PLAYER_SIZE) and
            enemy_pos[0] >= player_pos[0] and
            enemy_pos[0] < (player_pos[0] + PLAYER_SIZE)):
            return True
    return False

def game_over_screen():
    font = pygame.font.SysFont("monospace", 35)
    game_over_text = font.render("¡GAME OVER!", True, BLACK)
    DISPLAYSURF.blit(game_over_text, (WINDOW_WIDTH // 4, WINDOW_HEIGHT // 2))

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter para dar comienzo a el juego
                    return
        DISPLAYSURF.fill(WHITE)
        font = pygame.font.SysFont("monospace", 50)
        title_text = font.render("MENÚ PRINCIPAL", True, BLACK)
        DISPLAYSURF.blit(title_text, (WINDOW_WIDTH // 4, WINDOW_HEIGHT // 4))
        font = pygame.font.SysFont("monospace", 30)
        instructions_text = font.render("Presiona ENTER para jugar", True, BLACK)
        DISPLAYSURF.blit(instructions_text, (WINDOW_WIDTH // 4, WINDOW_HEIGHT // 2))
        pygame.display.update()

def main_game():
    player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 2 * PLAYER_SIZE]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WINDOW_WIDTH - PLAYER_SIZE:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < WINDOW_HEIGHT - PLAYER_SIZE:
            player_pos[1] += player_speed

        DISPLAYSURF.fill(WHITE)
        draw_enemies(enemy_list)
        draw_player(player_pos)

        if check_for_collisions(enemy_list, player_pos):
            game_over_screen()
            pygame.display.update()
            pygame.time.wait(2000)
            return  # Regreso al menú principal

        pygame.display.update()
        clock.tick(30)

#  EL. Menú principal y LA. Ejecución del juego
menu()
main_game()
