import sys
import pygame

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

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original = load_car(r"C:\Users\User\Pictures\сам соханил\машинки.png")
        self.image = self.original
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.angle = ANGLE_OFFSET

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.angle = 90 + ANGLE_OFFSET
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.angle = -90 + ANGLE_OFFSET
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.angle = 0 + ANGLE_OFFSET
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
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
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.all_sprites = pygame.sprite.Group(self.player)

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.is_running = False
            self.all_sprites.update()
            self.screen.fill((40, 44, 52))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()