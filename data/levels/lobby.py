from pytmx.util_pygame import load_pygame
from data.settings import screen, TILE_SIZE, X, Y
from data.characters import Inspector
import pygame


pygame.init()


class Lobby():
    """
    Load lobby tmx
    """
    def __init__(self) -> None:
        self.level_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.load_tmx_map()

    def load_player(self, x, y):
        collisions = self.collision_sprites
        self.player = Inspector((x, y), self.level_sprites, collisions)

    def load_tmx_map(self):
        lobby_map = load_pygame('data/tmx/lobby.tmx')
        for layer in lobby_map.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surface in layer.tiles():
                    pos = (x * TILE_SIZE, y * TILE_SIZE)
                    add_to = [self.level_sprites]
                    if ('Walls' or 'Computers') == getattr(layer, 'name'):
                        add_to.append(self.collision_sprites)
                    Tile(pos, surface, add_to)
        for obj in lobby_map.get_layer_by_name('Player'):
            if obj.name == 'Start':
                self.load_player(obj.x, obj.y)

    def show(self, dt):
        screen.fill('green')
        # self.level_sprites.draw(screen)
        self.level_sprites.custom_draw(self.player)
        self.level_sprites.update(dt)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        infl_w = self.rect.width * 0.2
        infl_h = self.rect.height * 0.5
        self.hitbox = self.rect.copy().inflate(infl_w, infl_h)


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - X / 2
        self.offset.y = player.rect.centery - Y / 2
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)


if __name__ != '__main__':
    pass
