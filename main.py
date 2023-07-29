# Крестики - Нолики на Pygame
import pygame

# Размер окна
width = 340
height = 340

# Цвета
black = ("black")
red = ("red")
light_blue = ("lightblue")
white = ("white")
# Создание игровой сетки
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крестики - Нолики")

# Создание иконки игры
icon = pygame.image.load("cross zero.png")

# Установка новой иконки
pygame.display.set_icon(icon)

# Размер квадрата
square_size = 100

# Позиция квадрата
square_x = 10
square_y = 10

# Позиция второго квадрата
second_square_x = 120
second_square_y = 10

# Позиция третьего квадрата
third_square_x = 230
third_square_y = 10

# Позиция четвёртого квадрата
fourth_square_x = 10
fourth_square_y = 120

# Позиция пятого квадрата
fifth_square_x = 120
fifth_square_y = 120

# Позиция шестого квадрата
sixth_square_x = 230
sixth_square_y = 120

# Позиция седьмого квадрата
seventh_square_x = 10
seventh_square_y = 230

# Позиция восьмого квадрата
eighth_square_x = 120
eighth_square_y = 230

# Позиция девятого квадрата
ninth_square_x = 230
ninth_square_y = 230

# Цвета для квадратов
square_color = red
second_square_color = light_blue
third_square_color = white

# Цвет экрана
screen.fill("dark blue")

# Рисуем квадрат
pygame.draw.rect(screen, third_square_color, (square_x, square_y, square_size, square_size))

# Рисуем второй квадрат
pygame.draw.rect(screen, third_square_color, (second_square_x, second_square_y, square_size, square_size))

# Рисуем третий квадрат
pygame.draw.rect(screen, third_square_color, (third_square_x, third_square_y, square_size, square_size))

# Рисуем четвёртый квадрат
pygame.draw.rect(screen, third_square_color, (fourth_square_x, fourth_square_y, square_size, square_size))

# Рисуем пятый квадрат
pygame.draw.rect(screen, third_square_color, (fifth_square_x, fifth_square_y, square_size, square_size))

# Рисуем шестой квадрат
pygame.draw.rect(screen, third_square_color, (sixth_square_x, sixth_square_y, square_size, square_size))

# Рисуем седьмой квадрат
pygame.draw.rect(screen, third_square_color, (seventh_square_x, seventh_square_y, square_size, square_size))

# Рисуем восьмой квадрат
pygame.draw.rect(screen, third_square_color, (eighth_square_x, eighth_square_y, square_size, square_size))

# Рисуем девятый квадрат
pygame.draw.rect(screen, third_square_color, (ninth_square_x, ninth_square_y, square_size, square_size))

# Текущий игрок
current_player = "X"

# Обновление экрана
pygame.display.flip()

def draw_cross(x, y):
    # Рисуем крестик в квадрате с координатами (x, y)
    pygame.draw.line(screen, black, (x + 40, y + 40), (x + square_size - 40, y + square_size - 40), 6)
    pygame.draw.line(screen, black, (x + square_size - 40, y + 40), (x + 40, y + square_size - 40), 6)

def draw_zero(x, y):
    # Рисуем нолик в квадрате с координатами (x, y)
    pygame.draw.circle(screen, black, (x + square_size // 2, y + square_size // 2), square_size // 2 - 35, 5)

# Цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            successful_step = False
            # Получение координат клика мыши
            mouse_pos = pygame.mouse.get_pos()
            # Первая строка
            if 10 < mouse_pos[0] < 110 and 10 < mouse_pos[1] < 110 and board[0][0] == "":
                board[0][0] = current_player
                successful_step = True
            if 120 < mouse_pos[0] < 220 and 10 < mouse_pos[1] < 110 and board[0][1] == "":
                board[0][1] = current_player
                successful_step = True
            if 230 < mouse_pos[0] < 330 and 10 < mouse_pos[1] < 110 and board[0][2] == "":
                board[0][2] = current_player
                successful_step = True
            # Вторая строка
            if 10 < mouse_pos[0] < 110 and 120 < mouse_pos[1] < 220 and board[1][0] == "":
                board[1][0] = current_player
                successful_step = True
            if 120 < mouse_pos[0] < 220 and 120 < mouse_pos[1] < 220 and board[1][1] == "":
                board[1][1] = current_player
                successful_step = True
            if 230 < mouse_pos[0] < 330 and 120 < mouse_pos[1] < 220 and board[1][2] == "":
                board[1][2] = current_player
                successful_step = True
            # Третья строка
            if 10 < mouse_pos[0] < 110 and 230 < mouse_pos[1] < 330 and board[2][0] == "":
                board[2][0] = current_player
                successful_step = True
            if 120 < mouse_pos[0] < 220 and 230 < mouse_pos[1] < 330 and board[2][1] == "":
                board[2][1] = current_player
                successful_step = True
            if 230 < mouse_pos[0] < 330 and 230 < mouse_pos[1] < 330 and board[2][2] == "":
                board[2][2] = current_player
                successful_step = True

            for row in range(3):
                for col in range(3):
                    if board[row][col] == "X":
                        # Рисуем квадрат
                        pygame.draw.rect(screen, square_color, (10 + 10 * col + 100 * col, 10 + 10 * row + 100 * row, square_size, square_size))

            if successful_step == True:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
                # Рисуем крестик в первом квадрате
                if successful_step:
                    draw_cross(square_x, square_y)
            # Обновляем состояние игровой сетки
            pygame.display.flip()
# Завершение игры
pygame.quit()