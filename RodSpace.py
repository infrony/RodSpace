from __future__ import division
import pygame
import random
from os import path

directorioImagenes = path.join(path.dirname(__file__), 'assets')
directorioSonidos = path.join(path.dirname(__file__), 'sounds')

ANCHO = 480
ALTO = 500
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_ALTO = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rod Space")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def main_menu():
    global pantalla

    menu_song = pygame.mixer.music.load(path.join(directorioSonidos, "HappyLevel.wav"))
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(path.join(directorioImagenes, "blue.png")).convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO), pantalla)

    draw_text(pantalla, "RodSpace Game", 40, ANCHO/2, 50)
    
    pantalla.blit(fondo, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
            
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_c:
                creditos()
        else:
            draw_text(pantalla, "Presione |Enter| para iniciar", 30, ANCHO/2, ALTO/2)
            draw_text(pantalla, "Presione |C| para ver los creditos", 30, ANCHO/2, (ALTO/2)+40)
            draw_text(pantalla, "o |Q| para terminar", 30, ANCHO/2, (ALTO/2)+80)
            pygame.display.update()

    ready = pygame.mixer.Sound(path.join(directorioSonidos,'getready.ogg'))
    ready.play()
    pantalla.fill(BLACK)
    draw_text(pantalla, "Nivel 1", 40, ANCHO/2, (ALTO/2)-100)
    pygame.display.update()

def nivel(level):
    global pantalla

    pygame.display.update()
    ready = pygame.mixer.Sound(path.join(directorioSonidos,'getready.ogg'))
    ready.play()
    pantalla.fill(BLACK)
    draw_text(pantalla, "Nivel " + str(level), 40, ANCHO/2, (ALTO/2)-100)
    pygame.display.update()

def pause():
    global pantalla

    menu_song = pygame.mixer.music.load(path.join(directorioSonidos, "HappyLevel.wav"))
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(path.join(directorioImagenes, "blue.png")).convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO), pantalla)

    draw_text(pantalla, "JUEGO EN PAUSA", 40, ANCHO/2, 50)
    
    pantalla.blit(fondo, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(pantalla, "Presione |ESC| para continuar", 30, ANCHO/2, ALTO/2)
            draw_text(pantalla, "o |Q| para terminar", 30, ANCHO/2, (ALTO/2)+40)
            pygame.display.update()

    pygame.display.update()

def gameOver():
    global pantalla

    menu_song = pygame.mixer.music.load(path.join(directorioSonidos, "HappyLevel.wav"))
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(path.join(directorioImagenes, "blue.png")).convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO), pantalla)

    draw_text(pantalla, "JUEGO TERMINADO", 50, ANCHO/2, 50)
    
    pantalla.blit(fondo, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_r:
                main_menu()
        else:
            draw_text(pantalla, "Presione |ESC ó Q| para Salir", 30, ANCHO/2, ALTO/2)
            draw_text(pantalla, "Presione |R| para Reiniciar el Juego", 30, ANCHO/2, (ALTO/2)+40)
            pygame.display.update()

    pygame.display.update()

def creditos():
    global pantalla

    menu_song = pygame.mixer.music.load(path.join(directorioSonidos, "HappyLevel.wav"))
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(path.join(directorioImagenes, "blue.png")).convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO), pantalla)

    draw_text(pantalla, "Creditos", 50, ANCHO/2, 50)
    
    pantalla.blit(fondo, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                main_menu()
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(pantalla, "Estudiante -> Rodney Guillen", 30, ANCHO/2, ALTO/2)
            draw_text(pantalla, "Cedula -> 8-818-534", 30, ANCHO/2, (ALTO/2)+40)
            draw_text(pantalla, "Carrera", 30, ANCHO/2, (ALTO/2)+80)
            draw_text(pantalla, "Lic. Desarrollo de Software", 30, ANCHO/2, (ALTO/2)+110)
            draw_text(pantalla, "Grupo -> 1LS231", 30, ANCHO/2, (ALTO/2)+150)
            draw_text(pantalla, "Presion |ESC| para Volver al Menú Principal", 30, ANCHO/2, (ALTO/2)+190)
            pygame.display.update()

def winner():
    global pantalla

    menu_song = pygame.mixer.music.load(path.join(directorioSonidos, "HappyLevel.wav"))
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(path.join(directorioImagenes, "blue.png")).convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO), pantalla)

    draw_text(pantalla, "Juego Completado!", 50, ANCHO/2, 50)
    
    pantalla.blit(fondo, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_r:
                main_menu()
        else:
            draw_text(pantalla, "Presione |ESC ó Q| para Salir", 30, ANCHO/2, ALTO/2)
            draw_text(pantalla, "Presione |R| para Reiniciar el Juego", 30, ANCHO/2, (ALTO/2)+40)
            draw_text(pantalla, "Completado en " + str(segundo) + " segundos", 30, ANCHO/2, (ALTO/2)+190)
            pygame.display.update()

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
    pct = max(pct, 0)
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_ALTO)
    fill_rect = pygame.Rect(x, y, fill, BAR_ALTO)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def newmob():
    mob_element = Mob()
    all_sprites.add(mob_element)
    mobs.add(mob_element)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = 20
        self.rect.bottom = ALTO / 2
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def update(self):
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = 20
            self.rect.bottom = ALTO / 2

        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5
        elif keystate[pygame.K_UP]:
            self.rect.bottom -= 5
        elif keystate[pygame.K_DOWN]:
            self.rect.bottom += 5

        if keystate[pygame.K_SPACE]:
            self.shoot()

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        self.rect.x += self.speedx

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top + 22)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.centerx, self.rect.top)
                bullet2 = Bullet(self.rect.centerx, self.rect.top + 40)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            if self.power >= 3:
                bullet1 = Bullet(self.rect.centerx, self.rect.top)
                bullet2 = Bullet(self.rect.centerx, self.rect.top + 40)
                missile1 = Missile(self.rect.centerx, self.rect.top + 22)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (ANCHO / 2, ALTO + 200)

# enemigos
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(ANCHO - 150, ANCHO - self.rect.width)
        self.rect.y = random.randrange(0, ALTO - self.rect.width)
        self.speedy = random.randrange(-3, 3)
        self.speedx = random.randrange(1, 4)
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_update > 50:
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy

        if (self.rect.top > ALTO + 10) or (self.rect.left < -25) or (self.rect.right > ANCHO + 20):
            self.rect.x = random.randrange(ANCHO - 150, ANCHO - 40)
            self.rect.y = random.randrange(0, ALTO - self.rect.width)
            self.speedy = random.randrange(1, 8)

## Powerups
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.x -= self.speedy
        if self.rect.top > ALTO:
            self.kill()

## Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.x -= self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.x -= self.speedy
        if self.rect.bottom < 0:
            self.kill()

## Carga de imagenes del juego
background = pygame.image.load(path.join(directorioImagenes, 'fondo.jpg')).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(directorioImagenes, 'playerShip2_green_landscape.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(directorioImagenes, 'laserGreen12.png')).convert()
missile_img = pygame.image.load(path.join(directorioImagenes, 'laserGreen10.png')).convert_alpha()

meteor_images = []
meteor_list = [
    'meteorGrey_big1.png',
    'meteorGrey_big2.png',
    'meteorGrey_med1.png',
    'meteorGrey_med2.png',
    'meteorGrey_small1.png',
    'meteorGrey_small2.png',
    'meteorGrey_tiny2.png',
    'meteorGrey_tiny1.png'
]

for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(directorioImagenes, image)).convert())

## explosion meteoro
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(directorioImagenes, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(directorioImagenes, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(directorioImagenes, 'pill_yellow.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(directorioImagenes, 'star_gold.png')).convert()

### sonidos
shooting_sound = pygame.mixer.Sound(path.join(directorioSonidos, 'sfx_laser1.ogg'))
missile_sound = pygame.mixer.Sound(path.join(directorioSonidos, 'rocket.ogg'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(directorioSonidos, sound)))
pygame.mixer.music.set_volume(0.2)

player_die_sound = pygame.mixer.Sound(path.join(directorioSonidos, 'rumble1.ogg'))

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

## spawn a group of mob
mobs = pygame.sprite.Group()
for i in range(8):
    newmob()

## grupo de bullets
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

score = 0
level = 1
segundo = 0
## Ciclo del  juego
running = True
menu_display = True
mostrar_nivel = False
while running:
    segundo = int(pygame.time.get_ticks() / 1000)
    if mostrar_nivel:
        level += 1
        clock.tick(0)
        nivel(level)
        pygame.time.wait(3000)
        print(segundo)
        mostrar_nivel = False
    
    if score == 2000 and level == 1:
        mostrar_nivel = True
    elif score == 4000 and level == 2:
        mostrar_nivel = True
    elif score == 6000 and level == 3:
        winner()
        
    if menu_display:
        main_menu()
        pygame.time.wait(3000)

        pygame.mixer.music.stop()

        pygame.mixer.music.load(path.join(directorioSonidos, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)

        menu_display = False

    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()
                
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for hit in hits:
        score += 50
        
        random.choice(expl_sounds).play()

        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()
            #player.lives += 1

    if player.lives == 0 and not death_explosion.alive():
        gameOver()

    pantalla.fill(BLACK)
    pantalla.blit(background, background_rect)

    all_sprites.draw(pantalla)
    draw_text(pantalla, str(score) + " Puntos", 18, ANCHO / 2, 10)
    draw_shield_bar(pantalla, ANCHO - 105, 5, player.shield)

    draw_lives(pantalla, 5, 5, player.lives, player_mini_img)

    pygame.display.flip()

pygame.quit()
