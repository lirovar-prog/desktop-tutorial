import sys
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60
CAR_HEIGHT = 110
ANGLE_OFFSET = 180

def load_car(path):
    img = pygame.image.load(path).convert_alpha()
    corner = img.get_at((0, 0))
    if corner.a == 255:
        bg = pygame.mask.from_threshold(img, corner, (12, 12, 12, 255))
        bg.invert()
        img = bg.to_surface(setsurface=img, unsetcolor=(0, 0, 0, 0))
    k = CAR_HEIGHT / img.get_height()
    size = (round(img.get_width() * k), CAR_HEIGHT)
    return pygame.transform.smoothscale(img, size)

def load_bigcar(path):
    try:
        img = pygame.image.load(path).convert_alpha()
        corner = img.get_at((0, 0))
        if corner.a == 255:
            bg = pygame.mask.from_threshold(img, corner, (12, 12, 12, 255))
            bg.invert()
            img = bg.to_surface(setsurface=img, unsetcolor=(0, 0, 0, 0))
    except (pygame.error, FileNotFoundError):
        img = pygame.Surface((70, round(CAR_HEIGHT * 1.1)), pygame.SRCALPHA)
        img.fill((224, 100, 117))
    target_height = round(CAR_HEIGHT * 1.1)
    k = target_height / img.get_height()
    size = (round(img.get_width() * k), target_height)
    return pygame.transform.smoothscale(img, size)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original = load_car(r"C:\Users\User\Pictures\сам соханил\машинки.png")
        self.image = self.original
        self.rect = self.image.get_rect(center=(x, y))
        self.speed=6
        self.boost_speed=9
        self.angle = ANGLE_OFFSET

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            current_speed = self.boost_speed
        else:
            current_speed = self.speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= current_speed
            self.angle = 90 + ANGLE_OFFSET
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += current_speed
            self.angle = -90 + ANGLE_OFFSET
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= current_speed
            self.angle = 0 + ANGLE_OFFSET
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += current_speed
            self.angle = 180 + ANGLE_OFFSET

        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

        center = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect(center=center)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PYGAME GAME")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.all_sprites = pygame.sprite.Group(self.player)

        for _ in range(7):
            enemy = Enemy(self.enemies)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.is_running = False
            self.all_sprites.update()
            if pygame.sprite.spritecollide(self.player, self.enemies, False, pygame.sprite.collide_mask):
                self.is_running = False
            self.screen.fill((40, 44, 52))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemies_group):
        super().__init__()
        self.enemies_group = enemies_group
        self.original = load_bigcar(r"C:\Users\User\Pictures\сам соханил\фура.png")
        self.image = pygame.transform.rotate(self.original, 90)
        self.rect = self.image.get_rect()
        self.reset_position()

        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(3, 5)
    def reset_position(self):
        for _ in range(50):
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-250, -100)
            self.speed = random.randint(2, 6)
            collisions = [sprite for sprite in self.enemies_group if sprite != self and self.rect.colliderect(sprite.rect)]      
            if not collisions:
                break
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset_position()

if __name__ == "__main__":
    Game().run()