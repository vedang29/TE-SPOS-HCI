import pygame, random, sys

pygame.init()

W, H = 500, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ball Catcher Game - Pastel Look")
clock = pygame.time.Clock()


BG = (255, 230, 250)      
BALL = (50, 200, 180)     
BASKET = (150, 100, 255)  
TEXT = (40, 40, 40)       


basket = pygame.Rect(W//2 - 40, H - 50, 80, 15)
ball = pygame.Rect(random.randint(0, W - 20), 0, 20, 20)
ball_speed = 4.5
basket_speed = 6
score = 0
game_over = False

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 48)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and game_over:
            if e.key == pygame.K_r:
                score = 0
                ball_speed = 4.5
                ball.y = 0
                ball.x = random.randint(0, W - 20)
                game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            basket.x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket.x += basket_speed
        basket.x = max(0, min(W - basket.width, basket.x))
        ball.y += ball_speed

        if ball.colliderect(basket):
            score += 1
            ball_speed += 0.15
            ball.y = 0
            ball.x = random.randint(0, W - 20)

        if ball.y > H:
            game_over = True

    
    screen.fill(BG)
    pygame.draw.rect(screen, BASKET, basket, border_radius=5)
    pygame.draw.ellipse(screen, BALL, ball)
    screen.blit(font.render(f"Score: {score}", True, TEXT), (10, 10))

    if game_over:
        over_text = big_font.render("Game Over!", True, BALL)
        retry_text = font.render("Press R to Restart", True, TEXT)
        screen.blit(over_text, (W//2 - over_text.get_width()//2, H//2 - 40))
        screen.blit(retry_text, (W//2 - retry_text.get_width()//2, H//2 + 10))

    pygame.display.flip()
    clock.tick(60)
