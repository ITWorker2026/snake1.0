
import pygame
import time
import random

# 初始化pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 游戏窗口尺寸
width = 600
height = 400

# 创建游戏窗口
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义蛇的块大小和速度
block_size = 10
snake_speed = 15

# 设置字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# 显示得分
def display_score(score):
    value = score_font.render("得分: " + str(score), True, black)
    game_window.blit(value, [0, 0])


# 绘制蛇
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], block_size, block_size])


# 显示消息
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])


# 游戏主循环
def game_loop():
    # 游戏是否结束
    game_over = False
    # 游戏是否关闭
    game_close = False

    # 蛇的初始位置
    x1 = width / 2
    y1 = height / 2

    # 蛇的位置变化
    x1_change = 0
    y1_change = 0

    # 蛇的身体列表
    snake_list = []
    length_of_snake = 1

    # 食物位置
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            # 游戏结束画面
            game_window.fill(blue)
            display_message("你输了! 按Q退出或C重玩", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # 处理键盘输入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # 检查碰撞边界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)
        
        # 绘制食物
        pygame.draw.rect(game_window, yellow, [foodx, foody, block_size, block_size])
        
        # 更新蛇的身体
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 检查蛇是否撞到自己
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 绘制蛇和得分
        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            # 生成新的食物
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            # 增加蛇的长度
            length_of_snake += 1

        # 控制蛇的速度
        time_clock = pygame.time.Clock()
        time_clock.tick(snake_speed)

    # 退出游戏
    pygame.quit()
    quit()


# 启动游戏
game_loop()