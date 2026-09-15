import pygame

pygame.init()
import sys
import os

def resource_path(relative_path):
    """ Возвращает абсолютный путь к ресурсу (для dev и exe) """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

screen = pygame.display.set_mode((1440, 680), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("CHEBUREK GAME")
icon = pygame.image.load(resource_path('images/Flux_Dev_The_icon_for_the_2d_pixel_game_in_the_style_of_1930s__1.png'))
pygame.display.set_icon(icon)

bg = pygame.image.load(resource_path('images/Background2.png')).convert_alpha()
bg2 = pygame.image.load(resource_path('images/Background3.png')).convert_alpha()
bg_menu = pygame.image.load(resource_path('images/bg_menu.png')).convert_alpha()
scroll_speed = 1
bg_scroll = 0

WORLD_WIDTH = 3300  # Ширина игрового мира
SCREEN_WIDTH = 1440  # Ширина экрана
CAMERA_BORDER = 500  # Зона у краев экрана, где включается "притягивание"
import os

def clean_build_web(path='build/web'):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d == '__pycache__':
                full_path = os.path.join(root, d)
                print(f"Removing directory: {full_path}")
                os.rmdir(full_path)
        for f in files:
            if f.endswith('.map'):
                full_path = os.path.join(root, f)
                print(f"Removing file: {full_path}")
                os.remove(full_path)



import random
run_right = [
    pygame.image.load(resource_path('images/player/RUN/Run.png')),
    pygame.image.load(resource_path('images/player/RUN/Run (1).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (2).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (3).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (4).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (5).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (6).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (7).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (8).png')),
    pygame.image.load(resource_path('images/player/RUN/Run (9).png')),
]

run_left = [
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (1) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (2) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (3) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (4) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (5) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (6) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (7) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (8) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (9) (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT RUN/Run (10).png')),
]

walk_right = [
    pygame.image.load(resource_path('images/player/WALK/Walk.png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (1).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (2).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (3).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (4).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (5).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (6).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (7).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (8).png')),
    pygame.image.load(resource_path('images/player/WALK/Walk (9).png')),
]

walk_left = [
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (8) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (9) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (10).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (11).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (6) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (5) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (4) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (7) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (3) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (2) (1).png')),
    pygame.image.load(resource_path('images/Player_left/LEFT_WALK/Walk (1) (1).png')),
]

stay = [
    pygame.image.load(resource_path('images/player/Idle.png')),
]
left_stay = [
    pygame.image.load(resource_path('images/Player_left/idle_left.png'))
]

jump = [
    pygame.image.load(resource_path('images/player/JUMP/jump1.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 2.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 3.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 4.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 5.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 6.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 7.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 8.png')),
    pygame.image.load(resource_path('images/player/JUMP/jump 9.png')),
]

atack = [
    pygame.image.load(resource_path('images/player/ATACK/Attack1.png')),
    pygame.image.load(resource_path('images/player/ATACK/Attack2.png')),
    pygame.image.load(resource_path('images/player/ATACK/Attack3.png')),
    pygame.image.load(resource_path('images/player/ATACK/Attack4.png')),
]

atack_left = [
    pygame.image.load(resource_path('images/player_left/LEFT_ATACK/Attack1.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_ATACK/Attack2 (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT_ATACK/Attack3 (1).png')),
    pygame.image.load(resource_path('images/player_left/LEFT_ATACK/Attack4 (1).png')),
]

shot = [
    pygame.image.load(resource_path('images/player/SHOT/shot1.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot2.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot3.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot4.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot5.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot6.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot7.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot8.png')),
    pygame.image.load(resource_path('images/player/SHOT/shot9.png')),
]

shot_left = [
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot1.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot2.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot3.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot4.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot5.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot6.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot7.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot8.png')),
    pygame.image.load(resource_path('images/player_left/LEFT_SHOT/shot9.png')),
]

# --- NPC1 ---
npc1_idle_left = [
    pygame.image.load(resource_path('images/NPC1/IDLE/idle.png')),
]
npc1_idle_right = [
    pygame.image.load(resource_path('images/NPC1/IDLE/right_idle.png')),
]
npc1_walk_left = [
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (12).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (13).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (14).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (15).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (16).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (17).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (18).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (19).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (20).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_WALK/walk (21).png')),
]
npc1_shot_left = [
    pygame.image.load(resource_path('images/NPC1/LEFT_SHOT/shot (31).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_SHOT/shot (32).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_SHOT/shot (33).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_SHOT/shot (34).png')),
]
npc1_shot_right = [
    pygame.image.load(resource_path('images/NPC1/SHOT/shot (31).png')),
    pygame.image.load(resource_path('images/NPC1/SHOT/shot (32).png')),
    pygame.image.load(resource_path('images/NPC1/SHOT/shot (33).png')),
    pygame.image.load(resource_path('images/NPC1/SHOT/shot (34).png')),
]
npc1_dead_left = [
    pygame.image.load(resource_path('images/NPC1/LEFT_DEAD/Dead.png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_DEAD/Dead (1).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_DEAD/Dead (2).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_DEAD/Dead (3).png')),
    pygame.image.load(resource_path('images/NPC1/LEFT_DEAD/Dead (4).png')),
]

# --- NPC2 ---
npc2_run_right = [
    pygame.image.load(resource_path('images/NPC2/RUN/Run (11).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (12).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (13).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (14).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (15).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (16).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (17).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (18).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (19).png')),
    pygame.image.load(resource_path('images/NPC2/RUN/Run (20).png')),
]
npc2_run_left = [
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (11).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (12).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (13).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (14).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (15).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (16).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (17).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (18).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (19).png')),
    pygame.image.load(resource_path('images/NPC2/RUN_LEFT/Run (20).png')),
]
npc2_attack_right = [
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1.png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1 (1).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1 (2).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1 (3).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1 (4).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK/Attack_1 (5).png')),
]
npc2_attack_left = [
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1.png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1 (1).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1 (2).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1 (3).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1 (5).png')),
    pygame.image.load(resource_path('images/NPC2/ATTACK_LEFT/Attack_1 (5).png')),
]
npc2_dead_right = [
    pygame.image.load(resource_path('images/NPC2/DEAD/Dead (5).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD/Dead (6).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD/Dead (7).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD/Dead (8).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD/Dead (9).png')),
]
npc2_dead_left = [
    pygame.image.load(resource_path('images/NPC2/DEAD_LEFT/Dead (5).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD_LEFT/Dead (6).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD_LEFT/Dead (7).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD_LEFT/Dead (8).png')),
    pygame.image.load(resource_path('images/NPC2/DEAD_LEFT/Dead (9).png')),
]
npc2_idle = [
    pygame.image.load(resource_path('images/NPC2/IDLE/idle.png')),
]
npc2_idle_left = [
    pygame.image.load(resource_path('images/NPC2/IDLE/idle_left.png')),
]

# --- BOSS ---
boss_walk = [
    pygame.image.load(resource_path('images/BOSS/WALK/Walk1.png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk2.png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (26).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (27).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (28).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (29).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (30).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (31).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (32).png')),
    pygame.image.load(resource_path('images/BOSS/WALK/Walk (33).png')),
]
boss_walk_left = [
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk1.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk2.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk3.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk4.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk5.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk6.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk7.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk8.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk9.png')),
    pygame.image.load(resource_path('images/BOSS/WALK_LEFT/walk10.png')),
]
boss_dead = [
    pygame.image.load(resource_path('images/BOSS/DEAD/Dead (8).png')),
    pygame.image.load(resource_path('images/BOSS/DEAD/Dead (9).png')),
    pygame.image.load(resource_path('images/BOSS/DEAD/Dead (10).png')),
    pygame.image.load(resource_path('images/BOSS/DEAD/Dead (11).png')),
    pygame.image.load(resource_path('images/BOSS/DEAD/Dead (12).png')),
]
boss_dead_left = [
    pygame.image.load(resource_path('images/BOSS/DEAD_LEFT/dead1.png')),
    pygame.image.load(resource_path('images/BOSS/DEAD_LEFT/dead2.png')),
    pygame.image.load(resource_path('images/BOSS/DEAD_LEFT/dead3.png')),
    pygame.image.load(resource_path('images/BOSS/DEAD_LEFT/dead4.png')),
    pygame.image.load(resource_path('images/BOSS/DEAD_LEFT/dead5.png')),
]
boss_attack = [
    pygame.image.load(resource_path('images/BOSS/ATTACK/Attack (1).png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK/Attack (2).png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK/Attack (3).png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK/Attack (4).png')),
]
boss_attack_left = [
    pygame.image.load(resource_path('images/BOSS/ATTACK_LEFT/Attack (1)-fotor-20250506193928.png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK_LEFT/Attack (2)-fotor-20250506194114.png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK_LEFT/Attack (3)-fotor-20250506194125.png')),
    pygame.image.load(resource_path('images/BOSS/ATTACK_LEFT/Attack (4)-fotor-20250506194014.png')),
]



boss_idle = [

    pygame.image.load(resource_path('images/BOSS/IDLE/idle1.png')),
]

boss_idle_left = [
    pygame.image.load(resource_path('images/BOSS/IDLE/idle2.png')),
]
brick = pygame.image.load(resource_path('images/brick3.png')).convert_alpha()
mebel = pygame.image.load(resource_path('images/mebel1.png')).convert_alpha()

TELEPORT_COLOR = (50, 200, 50)
BRICK_IMAGE = pygame.image.load(resource_path('images/brick.png')).convert_alpha()

boom = [
    pygame.image.load(resource_path('images/BOSS/BOOM/b1.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b2.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b3.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b4.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b5.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b6.png')),

    pygame.image.load(resource_path('images/BOSS/BOOM/b8.png')),

    pygame.image.load(resource_path('images/BOSS/BOOM/b10.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b11.png')),

    pygame.image.load(resource_path('images/BOSS/BOOM/b13.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b14.png')),

    pygame.image.load(resource_path('images/BOSS/BOOM/b16.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b17.png')),

    pygame.image.load(resource_path('images/BOSS/BOOM/b19.png')),
    pygame.image.load(resource_path('images/BOSS/BOOM/b20.png')),
]

player_anim_count = 10
clock = pygame.time.Clock()
FPS = 60
bg_x = 0

player_speed = 1
player_x = 50
player_y = 390
is_attaking = False
CAMERA_OFFSET = 500  # Отступ камеры от края экрана
MAX_PLAYER_X = 3300    # Максимальная координата X игрока
MIN_PLAYER_X = 50      # Минимальная координата X игрока
SCREEN_HEIGHT = 450
front = "right"



is_jump = False
jump_count = 21

# Каждый кадр анимации смерти длится 15/60 = 0.25 сек

npc2_x = 1500
npc2_y = 390
npc2_run_anim_count = 0
npc2_attack_anim_count = 0
npc2_hp = 100

npc_health = 100
hp = 350
MAX_HP = 400

player_bullets = []  # Список пуль игрока
last_shot_time = 0  # Время последнего выстрела
shot_cooldown = 2000  # 3 секунды в миллисекундах
is_player_shooting = False
player_shot_anim_count = 0
bullet_spawn_frame = 4 # На каком кадре анимации появляется пуля
bullet_spawn_delay = bullet_spawn_frame * 3  # Ускоренная анимация (1.5x быстрее)

bullet_surface = pygame.Surface((10, 5))
bullet_surface.fill('Yellow')



elevator = pygame.image.load(resource_path('images/HOUSE/elevator2.png')).convert_alpha()
elevator_button = pygame.image.load(resource_path('images/HOUSE/lift_button.png')).convert_alpha()
wall = pygame.image.load(resource_path('images/wall3.png')).convert_alpha()
safer = pygame.image.load(resource_path('images/safer.png')).convert_alpha()
piano = pygame.image.load(resource_path('images/HOUSE/piano.png')).convert_alpha()
bookshell = pygame.image.load(resource_path('images/HOUSE/bookshell.png')).convert_alpha()
box = pygame.image.load(resource_path('images/HOUSE/box.png')).convert_alpha()
box2 = pygame.image.load(resource_path('images/HOUSE/box2.png')).convert_alpha()
box3 = pygame.image.load(resource_path('images/HOUSE/box3.png')).convert_alpha()
glass = pygame.image.load(resource_path('images/HOUSE/glass.png')).convert_alpha()
glassshell = pygame.image.load(resource_path('images/HOUSE/glassshell.png')).convert_alpha()
picture = pygame.image.load(resource_path('images/HOUSE/picture.png')).convert_alpha()
sofa = pygame.image.load(resource_path('images/HOUSE/sofa.png')).convert_alpha()
tv = pygame.image.load(resource_path('images/HOUSE/tv2.png')).convert_alpha()
speaker = pygame.image.load(resource_path('images/HOUSE/speaker.png')).convert_alpha()
game_automat = pygame.image.load(resource_path('images/HOUSE/game_automat (2).png')).convert_alpha()
side_window = pygame.image.load(resource_path('images/HOUSE/window3 (1).png')).convert_alpha()
side_door = pygame.image.load(resource_path('images/HOUSE/side_door4.png')).convert_alpha()
chair = pygame.image.load(resource_path('images/HOUSE/chair.png')).convert_alpha()
chair2 = pygame.image.load(resource_path('images/HOUSE/chair2.png')).convert_alpha()
chair2_left = pygame.image.load(resource_path('images/HOUSE/chair2_left.png')).convert_alpha()
table = pygame.image.load(resource_path('images/HOUSE/table3.png')).convert_alpha()
bed = pygame.image.load(resource_path('images/HOUSE/bed.png')).convert_alpha()

granade = pygame.image.load(resource_path('images/BOSS/granade3.png')).convert_alpha()

down = pygame.image.load(resource_path('images/down4.png')).convert_alpha()

healer_img = pygame.image.load(resource_path('images/healer.png')).convert_alpha()

setting = pygame.image.load(resource_path('images/setting.png')).convert_alpha()


npc_list_in_game = []

npc_timer = pygame.USEREVENT + 1
pygame.time.set_timer(npc_timer, 8000)

is_npc2_attacking = False
damage_cooldown = 0


trip = 0


warn = pygame.image.load(resource_path('images/warn2.gif')).convert_alpha()

rus = pygame.image.load(resource_path('images/rus.jpg')).convert_alpha()
eng = pygame.image.load(resource_path('images/eng.png')).convert_alpha()

npc_timer = pygame.USEREVENT + 1
pygame.time.set_timer(npc_timer, 10000)

label = pygame.font.SysFont('Arial', 25)
restart_label = label.render('Начать сначала', False, (6, 128, 16))
level1_label = label.render('Уровень 1', False, (254, 254, 254))
level2_label = label.render('Уровень 2', False, (254, 254, 254))

lang_label_rus = label.render('Русский язык', False, (254, 254, 254))
lang_label_eng = label.render('English', False, (254, 254, 254))

restart_label_rect = restart_label.get_rect(topleft=(590, 222))
restart_label_rect2 = restart_label.get_rect(topleft=(590, 450))
level_label_rect1 = level1_label.get_rect(topleft=(610, 222))
level_label_rect2 = level2_label.get_rect(topleft=(610, 322))


lang_label_rect_rus = lang_label_rus.get_rect(topleft=(1280, 92))
lang_label_rect_eng = lang_label_eng.get_rect(topleft=(1280, 92))



level = 1

player_height = 80
player_width = 30  # примерная ширина

player_speed_y = 0  # вертикальная скорость

# Параметры кирпичей
brick_height = 20
brick_floor_y = 460

brick_floor_y2 = 320# Y-координата верхнего края кирпичей
brick_floor_y3 = 180

door_status = "close"
door_status2 = "close"
door_status3 = "close"
door_status7 = "close"
door_status4 = "close"
door_status5 = "close"
door_status6 = "close"

floor = 1

is_shot = False
pygame.mixer.init()
music_channel = pygame.mixer.Channel(0)
bg_sound = pygame.mixer.Sound(resource_path('sound/bg_sound_gta.mp3'))
bg_sound.set_volume(0.15)
music_channel.play(bg_sound)

bullet = pygame.Surface((10, 5))
bullet.fill('Yellow')

lang = "rus"
eng_rect = pygame.Rect(1280, 52,
                                   eng.get_width(),
                                   eng.get_height())
rus_rect = pygame.Rect(1280, 52,
                                   rus.get_width(),
                                   rus.get_height())

setting_rect = pygame.Rect(50, 52,
                                   setting.get_width(),
                                   setting.get_height())


#NPC на первом уровне
bullet_active = False
bullet_x = 0
bullet_y = 0

npc1_shoot_timer = 0
is_npc1_shooting = False
npc1_shot_anim_count = 0
npc1_y = 390
npc1_x = 600
npc1_x_move = 1
npc_death_anim_count = 0
npc_death_timer = 0
npc_death_delay = 90  # 3 секунды при 60 FPS
npc_death_frame_duration = 3


#NPC стрелок в первой комнате
bullet_active2 = False
bullet_x2 = 0
bullet_y2 = 0
npc1_y_l2 = 370
npc1_x_l2 = 800
npc1_health_l2 = 100
is_npc1_shooting_l2 = False
npc1_shot_anim_count_l2 = 0
npc1_shoot_timer_l2 = 0
npc1_x_move_l2 = 1
npc1_death_anim_count_l2 = 0
npc1_death_timer_l2 = 0
npc1_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc1_death_frame_duration_l2 = 12


#NPC стрелок во второй комнате
bullet_active3 = False
bullet_x3 = 0
bullet_y3 = 0
npc2_y_l2 = 370
npc2_x_l2 = 1200
npc2_health_l2 = 100
is_npc2_shooting_l2 = False
npc2_shot_anim_count_l2 = 0
npc2_shoot_timer_l2 = 0
npc2_x_move_l2 = 1
npc2_death_anim_count_l2 = 0
npc2_death_timer_l2 = 0
npc2_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc2_death_frame_duration_l2 = 14

# NPC стрелок в верхней слева
bullet_active4 = False
bullet_x4 = 0
bullet_y4 = 0
npc3_y_l2 = 90
npc3_x_l2 = 250
npc3_health_l2 = 100
is_npc3_shooting_l2 = False
npc3_shot_anim_count_l2 = 0
npc3_shoot_timer_l2 = 0
npc3_x_move_l2 = 1
npc3_death_anim_count_l2 = 0
npc3_death_timer_l2 = 0
npc3_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc3_death_frame_duration_l2 = 13


bullet_active5 = False
bullet_x5 = 0
bullet_y5 = 0
npc4_y_l2 = 250
npc4_x_l2 = 750
npc4_health_l2 = 100
is_npc4_shooting_l2 = False
npc4_shot_anim_count_l2 = 0
npc4_shoot_timer_l2 = 0
npc4_x_move_l2 = 1
npc4_death_anim_count_l2 = 0
npc4_death_timer_l2 = 0
npc4_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc4_death_frame_duration_l2 = 16

bullet_active6 = False
bullet_x6 = 0
bullet_y6 = 0
npc5_y_l2 = 250
npc5_x_l2 = 450
npc5_health_l2 = 100
is_npc5_shooting_l2 = False
npc5_shot_anim_count_l2 = 0
npc5_shoot_timer_l2 = 0
npc5_x_move_l2 = 1
npc5_death_anim_count_l2 = 0
npc5_death_timer_l2 = 0
npc5_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc5_death_frame_duration_l2 = 15



# Блок 8
bullet_active8 = False
bullet_x8 = 0
bullet_y8 = 0
npc7_y_l2 = 110
npc7_x_l2 = 1295
npc7_health_l2 = 100
is_npc7_shooting_l2 = False
npc7_shot_anim_count_l2 = 0
npc7_shoot_timer_l2 = 0
npc7_x_move_l2 = 1
npc7_death_anim_count_l2 = 0
npc7_death_timer_l2 = 0
npc7_death_delay_l2 = 90  # 3 секунды при 60 FPS
npc7_death_frame_duration_l2 = 15


class Healer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = healer_img  # Используем загруженное изображение
        self.rect = self.img.get_rect(center=(x, y))
        self.float_offset = 0
        self.float_direction = 1
        self.float_speed = 0.5
        self.animation_counter = 0

    def update(self):
        # Плавное движение вверх-вниз
        self.float_offset += self.float_speed * self.float_direction
        if abs(self.float_offset) > 5:
            self.float_direction *= -1
        self.rect.y = self.y + self.float_offset

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

healers = []
HEALER_DROP_CHANCE = 0.5
heal = False
heal_text_duration = 0

# Создадим список для эффектов подбора
pickup_effects = []

player_rect = pygame.Rect(player_x, player_y,
                                  walk_left[0].get_width(),
                                  walk_left[0].get_height())

class PickupEffect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 120  # Длительность эффекта
        self.text = "+75 HP"

    def update(self):
        self.timer -= 1
        self.y -= 1  # Текст поднимается вверх

    def draw(self, screen):
        font = pygame.font.SysFont('Arial', 20)
        text_surface = font.render(self.text, True, (0, 255, 0))
        screen.blit(text_surface, (self.x, self.y))


start_healer = None
start_healer2 = None
# В обработке подбора аптечки:


# В главном цикле обновляем и рисуем эффекты


class NPC2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
        self.run_anim_count = 0
        self.attack_anim_count = 0
        self.attack_cooldown = 0
        self.attack_interval = 90
        self.attack_cooldown_max = 66
        self.attack_damage = 10
        self.attack_frame = 4
        self.state = "idle"
        self.rect = pygame.Rect(x, y, npc2_run_left[0].get_width(), npc2_run_left[0].get_height())
        self.death_anim_duration = len(npc2_dead_left) * 3 * 3
        self.death_timer = 0
        self.death_frame = 0
        self.death_delay = 15
        self.death_anim_count = 0
        self.should_remove = False
        self.has_attacked = False
        self.last_attack_time = 0
        self.dead_sound_cd = 0


    def update_death(self):
        if self.death_timer < self.death_anim_duration:
            self.death_frame = min(self.death_timer // 5, len(npc2_dead_left) - 1)
            self.death_timer += 1
        else:
            if random.random() < HEALER_DROP_CHANCE:
                if player_x < self.x:
                  healers.append(Healer(self.x + 35, self.y + 45))
                else:
                    healers.append(Healer(self.x - 36, self.y + 45))
            self.should_remove = True

    def update(self):
        # Обновляем rect при изменении позиции
        if self.state != "dead":
            self.rect.x = self.x
            self.rect.y = self.y


        if self.state == "dead":
            self.update_death()
            return

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1 / 3




    def should_remove(self):
        return self.death_timer > self.death_anim_duration + 1

    def perform_attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_interval * 50:
            global hp
            if hard == "normal":
              hp -= self.attack_damage
            elif hard == "easy":
                hp -= self.attack_damage - 3
            elif hard == "hard":
                hp -= self.attack_damage + 2
            self.last_attack_time = current_time
            self.attack_cooldown = self.attack_interval

    def draw(self, screen):
        if self.state == "dead":
            screen.blit(npc2_dead_left[self.death_frame], (self.x, self.y))
            if self.dead_sound_cd <= 0:
                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                self.dead_sound_cd = 60
            if self.dead_sound_cd > 0:
                self.dead_sound_cd -= 1

        elif self.state == "attack":
            if self.x < player_x:
                frame = self.attack_anim_count // 6 % len(npc2_attack_right)
                screen.blit(npc2_attack_right[frame], (self.x, self.y))
                self.attack_anim_count += 1
            else:
                frame = self.attack_anim_count // 6 % len(npc2_attack_left)
                screen.blit(npc2_attack_left[frame], (self.x, self.y))
                self.attack_anim_count += 1
            if frame == self.attack_anim_count // 6 % len(npc2_attack_left):
                self.perform_attack()
        elif self.state == "run":
            if self.x < player_x - 40:
                frame = self.run_anim_count // 3 % len(npc2_run_right)
                screen.blit(npc2_run_right[frame], (self.x, self.y))
                self.run_anim_count += 1
                self.x += 1.75
            else:
                frame = self.run_anim_count // 3 % len(npc2_run_left)
                screen.blit(npc2_run_left[frame], (self.x, self.y))
                self.run_anim_count += 1
                self.x -= 1.75
        else:
            if self.x < player_x:
                screen.blit(npc2_idle[0], (self.x, self.y))
            else:
                screen.blit(npc2_idle_left[0], (self.x, self.y))



npc_dead_cout = 0
npc_list_in_game8 = []
npc_list_in_game9 = []
npc_list_in_game10 = []
npc_list_in_game11 = []
npc_list_in_game12 = []
npc_list_in_game13 = []
npc_list_in_game14 = []
npc_list_in_game15 = []







npc_list_in_game16 = []
def update_player():
    global player_y, player_speed_y

    # Гравитация (вызывать каждый кадр)
    player_speed_y += 0.5 / 5  # сила тяжести
    player_y += player_speed_y

    # Коллизия с полом
    if floor == 1:
        if player_y + player_height > brick_floor_y:
            player_y = brick_floor_y - player_height
            player_speed_y = 0

    elif player_y < 320 and player_y > 180:
        if player_y + player_height > brick_floor_y2:
            player_y = brick_floor_y2 - player_height
            player_speed_y = 0

    elif floor == 3:
        if player_y + player_height > brick_floor_y3:
            player_y = brick_floor_y3 - player_height
            player_speed_y = 0
            # останавливаем падение


def reset_game_state():
    global hp, player_x, player_y, npc_alive, npc2_alive_l2, npc3_alive_l2, npc4_alive_l2
    global npc5_alive_l2, npc7_alive_l2, npc2_health_l2, door_status, door_status2
    global door_status3, door_status4, door_status5, door_status6, door_status7
    global npc_list_in_game, npc_list_in_game8, npc_list_in_game9, npc_list_in_game10
    global npc_list_in_game11, npc_list_in_game12, npc_list_in_game13, npc_list_in_game14
    global npc_list_in_game15, npc_list_in_game16, boss_alive, boss_hp

    # Сброс параметров игрока
    hp = 300
    player_x = 50

    player_y = 390 - 280

    # Сброс NPC для уровня 1
    npc_alive = 1
    npc_health = 100
    npc_list_in_game.clear()

    # Сброс NPC для уровня 2
    npc1_alive_l2 = 1
    npc1_health_l2 = 100
    npc2_alive_l2 = 1
    npc2_health_l2 = 100
    npc3_alive_l2 = 1
    npc3_health_l2 = 100
    npc4_alive_l2 = 1
    npc4_health_l2 = 100
    npc5_alive_l2 = 1
    npc5_health_l2 = 100
    npc7_alive_l2 = 1
    npc7_health_l2 = 100

    # Очистка всех списков NPC
    npc_list_in_game8.clear()
    npc_list_in_game9.clear()
    npc_list_in_game10.clear()
    npc_list_in_game11.clear()
    npc_list_in_game12.clear()
    npc_list_in_game13.clear()
    npc_list_in_game14.clear()
    npc_list_in_game15.clear()
    npc_list_in_game16.clear()

    # Сброс состояния босса
    boss_alive = True
    boss_hp = 500

    # Сброс состояния дверей
    door_status = "close"
    door_status2 = "close"
    door_status3 = "close"
    door_status4 = "close"
    door_status5 = "close"
    door_status6 = "close"
    door_status7 = "close"

    # При необходимости - повторная инициализация NPC для уровня 2
    if level == 2:
        npc_list_in_game16.append(NPC2(600, 100))
        npc_list_in_game15.append(NPC2(550, 100))
        npc_list_in_game14.append(NPC2(200, 240))
        npc_list_in_game13.append(NPC2(1100, 240))
        npc_list_in_game12.append(NPC2(500, 240))
        npc_list_in_game11.append(NPC2(800, 240))
        npc_list_in_game10.append(NPC2(1000, 380))
        npc_list_in_game9.append(NPC2(400, 380))
        npc_list_in_game8.append(NPC2(700, 380))




npc8_max = 0
npc9_max = 0
npc10_max = 0
npc11_max = 0
npc12_max = 0
npc13_max = 0
npc14_max = 0
npc15_max = 0
npc16_max = 0

elevator_cooldown = 0

boss_y = 104
boss_x = 800
boss_attack_cooldown = 180
boss_anim_count = 0
boss_attack_duration = 45
boss_attacking = False
boss_walk_duration = 360
boss_direction = 1
BOSS_RUN_DURATION = 45 * 3  # 1.5 секунды при 30 FPS (или 22 при 15 FPS)
boss_run_timer = 0
boss_run_direction = 0
BOSS_ATTACK_COOLDOWN = 22.5 * 3 # 2 секунды при 30 FPS (или 30 при 15 FPS)
BOSS_ATTACK_RANGE = 50
boss_hp = 500# Дистанция для начала атаки
BOSS_DEATH_DURATION = 75  # Длительность анимации смерти (5 кадров * 5 кадров на кадр при 15 FPS)
boss_alive = True
boss_death_frame = 0
is_playing_death_animation = False

granade_y = boss_y + 38
granade_x = boss_x - 5
granade_reload = 0
granade_up_max = 0
granade_down_max = 0
granade_lie_max = 0
granade_up = False
granade_down = False
granade_lie = False
granade_go = False
granade_boom = False
granade_boom_max = 0

boom_frame = 0
boom_animation_speed = 0.6  # Скорость анимации (меньше = быстрее)
boom_animation_counter = 0
is_playing_boom_animation = False

hit_sound3 = pygame.mixer.Sound(resource_path('sound/korotkiy-udar-kulakom-po-vozduhu.mp3'))
hit_sound3.set_volume(0.25)

hit_sounds = [
    pygame.mixer.Sound(resource_path('sound/slabyiy-udar-po-litsu-kulakom.mp3')),
    pygame.mixer.Sound(resource_path('sound/udar-gluhoy-myagkiy.mp3')),
    pygame.mixer.Sound(resource_path('sound/popal-v-kulak-popal-v-ranu-42370.mp3')),
    pygame.mixer.Sound(resource_path('sound/ne-silnyiy-udar-kulakom-v-igre.mp3')),
    pygame.mixer.Sound(resource_path('sound/udar-tochnyiy-moschnyiy-bokserskiy.mp3')),
]

hit_sounds2 = [
    pygame.mixer.Sound(resource_path('sound/krepkiy-udar-kulakom-po-litsu.mp3')),
    pygame.mixer.Sound(resource_path('sound/metkiy-udar-kulakom.mp3')),
    pygame.mixer.Sound(resource_path('sound/udar-bokserskiy-rezkiy-tochnyiy.mp3')),
]

boom_sounds = [
    pygame.mixer.Sound(resource_path('sound/oglushitelnyiy-blizkiy-vzryiv.mp3')),
    pygame.mixer.Sound(resource_path('sound/moschnyiy-vzryiv-v-okope.mp3')),
    pygame.mixer.Sound(resource_path('sound/moschnyiy-vzryiv-razorvavsheysya-bombyi.mp3')),
]

for sound in hit_sounds:
    sound.set_volume(0.2)

for sound in hit_sounds2:
    sound.set_volume(0.3)

for sound in boom_sounds:
    sound.set_volume(0.4)

button_sound = pygame.mixer.Sound(resource_path('sound/vyibor-nujnogo-deystviya.mp3'))
button_sound.set_volume(1)

shot3_sound = pygame.mixer.Sound(resource_path('sound/priglushennyiy-zvuk-vyistrelov-iz-avtomata.mp3'))
shot3_sound.set_volume(0.5)

door_sound = pygame.mixer.Sound(resource_path('sound/door.mp3'))
door_sound.set_volume(0.6)

dead_sounds = [
    pygame.mixer.Sound(resource_path('sound/d1.mp3')),
    pygame.mixer.Sound(resource_path('sound/d2.mp3')),
    pygame.mixer.Sound(resource_path('sound/d3.mp3')),
    pygame.mixer.Sound(resource_path('sound/d4.mp3')),
    pygame.mixer.Sound(resource_path('sound/d5.mp3')),
    pygame.mixer.Sound(resource_path('sound/d6.mp3')),
    pygame.mixer.Sound(resource_path('sound/d7.mp3')),
    pygame.mixer.Sound(resource_path('sound/d8.mp3')),
    pygame.mixer.Sound(resource_path('sound/d9.mp3')),
]

for sound in dead_sounds:
    sound.set_volume(0.2)

win_sound = pygame.mixer.Sound(resource_path('sound/win.mp3'))
lose_sound = pygame.mixer.Sound(resource_path('sound/lose.mp3'))

pickup_sound = pygame.mixer.Sound(resource_path('sound/346116__lulyc__retro-game-heal-sound.wav'))
pickup_sound.set_volume(0.5)

walk_sound = pygame.mixer.Sound(resource_path('sound/korotkiy-blizkiy-shag-po-derevyannomu-polu.mp3'))
walk_sound.set_volume(0.19)

run_sound = pygame.mixer.Sound(resource_path('sound/beg-po-betonu-variant-2-25270.mp3'))
run_sound.set_volume(0.5)



hit_sound_cd = 5
hit2_sound_cd = 5
hit3_sound_cd = 5
hit4_sound_cd = 5
hit5_sound_cd = 5
hit6_sound_cd = 5
hit7_sound_cd = 5
hit8_sound_cd = 5
hit9_sound_cd = 5
hit_sound_cd10 = 5
hit_sound_cd11 = 4
hit_sound_cd12 = 4
hit_sound_cd13 = 4
hit_sound_cd14 = 4
hit_sound_cd15 = 4
hit_sound_cd16 = 4
hit_sound_cd17 = 4
hit_sound_cd18 = 4
hit_sound_cd19 = 4
hit_sound_cd20 = 0

hit_sound_cd21 = 5
hit_sound_cd22 = 4
hit_sound_cd23 = 4
hit_sound_cd24 = 4
hit_sound_cd25 = 4
hit_sound_cd26= 4
hit_sound_cd27 = 4
hit_sound_cd28 = 4
hit_sound_cd29 = 4
hit_sound_cd30 = 4
hit_sound_cd31 = 0

dead_sound_cd = 0
dead_sound_cd2 = 0
dead_sound_cd3 = 0
dead_sound_cd4 = 0
dead_sound_cd5 = 0
dead_sound_cd7 = 0
player_attack_cooldown = 0

run_sound_cd = 0
run_sound_cd2 = 0
is_attaking = False


is_paused = False
pause_alpha = 150

hard = "normal"
hp_hard = 0
def draw_pause_menu(screen):
    # Темный фильтр

    if not menu:
        overlay = pygame.Surface((1440, 680), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, pause_alpha))
        screen.blit(overlay, (0, 0))

        # Кнопки
        resume_btn = pygame.Rect(600, 300, 240, 60)
        menu_btn = pygame.Rect(600, 380, 240, 60)

        # Отрисовка кнопок
        pygame.draw.rect(screen, (50, 50, 50), resume_btn)
        pygame.draw.rect(screen, (50, 50, 50), menu_btn)

        # Текст
        font = pygame.font.Font(None, 36)
        if lang == "rus":
            text_resume = font.render("Продолжить", True, (255, 255, 255))
            text_menu = font.render("В меню", True, (255, 255, 255))

        else:
            text_resume = font.render("Resume", True, (255, 255, 255))
            text_menu = font.render("Menu", True, (255, 255, 255))

        screen.blit(text_resume, (resume_btn.x + 50, resume_btn.y + 15))
        screen.blit(text_menu, (menu_btn.x + 70, menu_btn.y + 15))

        return resume_btn, menu_btn


GRAVITY = 0.5  # Сила гравитации (можно регулировать)
JUMP_POWER = 12  # Начальная сила прыжка (высота)
JUMP_DECREMENT = 0.7  # Скорость замедления прыжка

start_healer = Healer(212, 115)
healer_x = random.randint(280, 1100)
start_healer2 = Healer(healer_x, 140)

healer_cd = 0

warn_duration = 0
warn_active = False
warn_max = 0

setting1 = label.render("Легко", True, (1, 255, 1))
setting2 = label.render("Нормально (Базовый)", True, ("YELLOW"))
setting3 = label.render("Сложно (реально сложно!)", True, (255, 1, 1))
setting1_rect = setting1.get_rect(topleft=(50, 160))
setting2_rect = setting2.get_rect(topleft=(50, 192))
setting3_rect = setting3.get_rect(topleft=(50, 224))


show_setting = False
game_won = False
pause_button = pygame.Rect(1340, 620, 80, 50)
idle_status = True
menu = True
gameplay = False
running = True

default_player_x = 390


hit = 0
while running:

    mouse = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    screen.blit(bg_menu, (0, 0))
    keys = pygame.key.get_pressed()
    if not music_channel.get_busy():
        music_channel.play(bg_sound)





    if menu:

        font = pygame.font.SysFont('Arial', 36)

        if lang == "rus":
          author = label.render("Автор: CheburekGames", True, (255, 255, 255))
          text = font.render("Добро пожаловать в игру!", True, (255, 255, 255))
          setting_text = label.render("Уровень сложности", True, (255, 255, 255))
          setting1 = label.render("Легко", True, (1, 255, 1))
          setting2 = label.render("Нормально", True, ("YELLOW"))
          setting3 = label.render("Сложно (реально сложно!)", True, (255, 1, 1))
          exit_label = label.render('Выйти', True, (254, 254, 254))
        else:
            author = label.render("Developer: CheburekGames", True, (255, 255, 255))
            text = font.render("Welcome to the game!", True, (255, 255, 255))
            setting_text = label.render("Difficulty level", True, (255, 255, 255))
            setting1 = label.render("Easy", True, (1, 255, 1))
            setting2 = label.render("Normal", True, ("YELLOW"))
            setting3 = label.render("Hard (Realy HARD!)", True, (255, 1, 1))
            exit_label = label.render('Exit', True, (254, 254, 254))
        if show_setting:
                screen.blit(setting_text, (50, 128))
                screen.blit(setting1, (50, 160))
                screen.blit(setting2, (50, 192))
                screen.blit(setting3, (50, 224))

        exit_button = exit_label.get_rect(topleft=(1290, 624))
        screen.blit(setting, (setting_rect))
        screen.blit(level1_label, level_label_rect1)
        screen.blit(level2_label, level_label_rect2)
        screen.blit(text, (470, 100))
        screen.blit(author, (80, 640))
        screen.blit(exit_label, (exit_button))
        if level_label_rect1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level = 1
            menu = False
            gameplay = True
            button_sound.play()
        elif level_label_rect2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level = 2
            menu = False
            gameplay = True
            button_sound.play()



    if gameplay and not is_paused:



        screen.blit(bg, (bg_scroll % 1440, 0))
        screen.blit(bg, (bg_scroll % 1440 - 1440, 0))
        pause_button = pygame.Rect(1340, 620, 80, 50)
        if hard == "easy":
            HEALER_DROP_CHANCE = 0.6

        elif hard == "hard":
            HEALER_DROP_CHANCE = 0.4
        else:
            HEALER_DROP_CHANCE = 0.5
        if level == 2:

            screen.blit(wall, (0, 20))
            screen.blit(wall, (254, 20))


            window = pygame.Surface((10, 160))
            window.fill((36, 36, 34))
            window2 = pygame.Surface((506, 10))
            window2.fill((36, 36, 34))

            screen.blit(window, (837, 20))
            screen.blit(window, (927, 20))

            screen.blit(window, (1006, 20))
            screen.blit(window, (752, 20))
            screen.blit(window, (667, 20))
            screen.blit(window, (580, 20))
            screen.blit(window, (500, 20))
            screen.blit(window2, (500, 172))
            screen.blit(window2, (500, 40))


            screen.blit(wall, (1016, 20))
            screen.blit(wall, (254 + 1016, 20))
            screen.blit(wall, (508 + 1016, 20))

            screen.blit(wall, (0, 180))
            screen.blit(wall, (254, 180))
            screen.blit(wall, (508, 180))
            screen.blit(wall, (508 + 254, 180))
            screen.blit(wall, (1016, 180))
            screen.blit(wall, (1016 + 254, 180))
            screen.blit(wall, (1016 + 508, 180))

            screen.blit(wall, (0, 340))
            screen.blit(wall, (254, 340))
            screen.blit(wall, (508, 340))
            screen.blit(wall, (508 + 254, 340))
            screen.blit(wall, (1016, 340))
            screen.blit(wall, (1016 + 254, 340))
            screen.blit(wall, (1016 + 508, 340))

            screen.blit(safer, (1355, 119))
            safer_rect = safer.get_rect(topleft=(1355,119))

            screen.blit(elevator, (1300, 365))
            screen.blit(elevator_button, (1370, 397))

            screen.blit(elevator, (1300, 225))
            screen.blit(elevator_button, (1370, 257))

            screen.blit(elevator, (40, 225))
            screen.blit(elevator_button, (110, 257))

            screen.blit(elevator, (40, 85))
            screen.blit(elevator_button, (110, 117))

            screen.blit(piano, (800, 395))
            screen.blit(sofa, (400, 277))
            screen.blit(picture, (901, 223))
            screen.blit(glass, (260, 252))
            screen.blit(glassshell, (1080, 399))
            screen.blit(box3, (210, 430))
            screen.blit(box2, (780, 290))
            screen.blit(box, (190, 148))
            screen.blit(side_door, (100, 372))
            screen.blit(side_door, (1170, 232))
            screen.blit(table, (565, 289))
            screen.blit(tv, (569, 255))
            screen.blit(chair, (550, 410))
            screen.blit(chair, (1200, 410))
            screen.blit(chair, (410, 130))
            screen.blit(chair2_left, (650, 410))
            screen.blit(chair2, (750, 410))
            screen.blit(chair2, (1182, 134))
            screen.blit(game_automat, (1051, 100))
            screen.blit(game_automat, (1111, 100))

            screen.blit(speaker, (610, 269))



        npc1_left_pos = 1
        npc1_left_pos_l2 = 1
        npc2_left_pos_l2 = 1
        npc3_left_pos_l2 = 1
        npc4_left_pos_l2 = 2
        npc8_left_pos_l2 = 2
        npc5_left_pos_l2 = 2
        npc6_left_pos_l2 = 2
        npc7_left_pos_l2 = 1

        player_down = pygame.Surface((20, 5))
        player_down.fill("RED")

        font = pygame.font.SysFont('Arial', 22)
        round_hp = round(hp)
        hp_text = font.render(f"HP: {round_hp}", True, (255, 255, 255))


        player_rect = pygame.Rect(player_x, player_y,
                                  walk_left[0].get_width(),
                                  walk_left[0].get_height())

        if level == 1:
            npc1_rect = pygame.Rect(npc1_x, npc1_y,
                                npc1_shot_left[0].get_width(),
                                npc1_shot_left[0].get_height())







        if bullet_active:
            if npc1_x_move == 2:
                bullet_x += 15 / 3
            elif npc1_x_move == 1:
                bullet_x -= 15 / 3
            screen.blit(bullet_surface, (bullet_x, bullet_y))


            bullet_rect = pygame.Rect(bullet_x, bullet_y, 10, 5)

            if bullet_rect.colliderect(player_rect):
                hp -= 25
                bullet_active = False
            if npc1_x > player_x:
                if bullet_x < player_x - 90:
                    bullet_active = False
            if bullet_x > 1500:
                bullet_active = False

        current_time = pygame.time.get_ticks()
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0] and not is_player_shooting and current_time - last_shot_time > shot_cooldown:
            last_shot_time = current_time
            is_player_shooting = True
            player_shot_anim_count = 0

            shot2_sound = pygame.mixer.Sound(resource_path('sound/shot.mp3'))
            shot2_sound.set_volume(0.7)
            shot2_sound.play()

        if keys[pygame.K_d]:
            front = "right"
        elif keys[pygame.K_a]:
            front = "left"

        if is_player_shooting:
            player_shot_anim_count += 1
            anim_speed = 5
            current_frame = player_shot_anim_count // anim_speed

            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction = -1 if mouse_x < player_x else 1

            if current_frame == bullet_spawn_frame and len(player_bullets) == 0:
                player_bullets.append({
                    'surface': bullet_surface,
                    'x': player_x + (25 if direction == 1 else -10),
                    'y': player_y + 20,
                    'direction': direction
                })

            # Отрисовка анимации выстрела
            if direction == -1:  # Влево
                if current_frame < len(shot_left):
                    screen.blit(shot_left[current_frame], (player_x, player_y))
                else:
                    is_player_shooting = False
            else:  # Вправо
                if current_frame < len(shot):
                    screen.blit(shot[current_frame], (player_x, player_y))
                else:
                    is_player_shooting = False
        else:

            if keys[pygame.K_f]:
                if front == "right":
                    screen.blit(atack[player_anim_count // 23 % len(atack)], (player_x, player_y))
                elif front == "left":
                    screen.blit(atack_left[player_anim_count // 23 % len(atack_left)], (player_x, player_y))
                player_anim_count += 1
                hit = 1
                if level == 1:
                    if player_rect.colliderect(npc1_rect) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                          npc_health -= 0.5

                        else:
                            npc_health -= 1

                        if hit_sound_cd11 <= 0:
                            random.choice(hit_sounds2).play()  # Случайный выбор звука удара
                            hit_sound_cd11 = 45
                        if hit_sound_cd11 > 0:
                            hit_sound_cd11 -= 1

                if level == 2:
                    if player_rect.colliderect(npc1_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc1_health_l2 -= 0.5

                        else:
                          npc1_health_l2 -= 1
                        if hit_sound_cd11 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd11 = 45
                        if hit_sound_cd11 > 0:
                            hit_sound_cd11 -= 1

                    if player_rect.colliderect(npc2_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc2_health_l2 -= 0.5

                        else:
                          npc2_health_l2 -= 1
                        if hit_sound_cd12 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd12 = 45
                        if hit_sound_cd12 > 0:
                            hit_sound_cd12 -= 1

                    if player_rect.colliderect(npc3_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc3_health_l2 -= 0.5

                        else:
                          npc3_health_l2 -= 1
                        if hit_sound_cd13 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd13 = 45
                        if hit_sound_cd13 > 0:
                            hit_sound_cd13 -= 1

                    if player_rect.colliderect(npc4_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc4_health_l2 -= 0.5

                        else:
                          npc4_health_l2 -= 1
                        if hit_sound_cd14 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd14 = 45
                        if hit_sound_cd14 > 0:
                            hit_sound_cd14 -= 1

                    if player_rect.colliderect(npc5_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc5_health_l2 -= 0.5

                        else:
                          npc5_health_l2 -= 1
                        if hit_sound_cd15 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd15 = 45
                        if hit_sound_cd15 > 0:
                            hit_sound_cd15 -= 1

                    if player_rect.colliderect(npc7_rect_l2) and hit == 1:
                        is_attaking = True
                        if hard == "hard":
                            npc7_health_l2 -= 0.5

                        else:
                          npc7_health_l2 -= 1
                        if hit_sound_cd16 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd16 = 45
                        if hit_sound_cd16 > 0:
                            hit_sound_cd16 -= 1

                    if player_rect.colliderect(boss_rect) and hit == 1 and player_attack_cooldown <= 0:
                        is_attaking = True
                        boss_hp -= 10
                        player_attack_cooldown = 30
                        if hit_sound_cd17 <= 0:
                            random.choice(hit_sounds2).play()
                            hit_sound_cd17 = 45
                        if hit_sound_cd17 > 0:
                            hit_sound_cd17 -= 1
                    else:
                        if hit_sound_cd18 <= 0:
                            hit_sound3.play()
                            hit_sound_cd18 = 45
                        if hit_sound_cd18 > 0:
                            hit_sound_cd18 -= 1

                    if player_attack_cooldown > 0:
                        player_attack_cooldown -= 1









            else:




                if keys[pygame.K_SPACE]:
                    screen.blit(jump[player_anim_count // 4 % len(jump)], (player_x, player_y))


                elif keys[pygame.K_d]:
                    idle_status = False

                    if keys[pygame.K_LSHIFT]:
                        screen.blit(run_right[player_anim_count // 8 % len(run_right)], (player_x, player_y))
                        if not is_jump:
                            if run_sound_cd <= 0:
                                walk_sound.play()  # Случайный выбор звука удара
                                run_sound_cd = 30
                            if run_sound_cd > 0:
                                run_sound_cd -= 1

                    else:
                        screen.blit(walk_right[player_anim_count // 9 % len(walk_right)], (player_x, player_y - 2))
                        if run_sound_cd2 <= 0:
                            walk_sound.play()  # Случайный выбор звука удара
                            run_sound_cd2 = 30
                        if run_sound_cd2 > 0:
                            run_sound_cd2 -= 1
                    player_anim_count += 1

                elif keys[pygame.K_a]:
                    idle_status = False
                    if keys[pygame.K_LSHIFT]:
                        screen.blit(run_left[player_anim_count // 5 % len(run_left)], (player_x, player_y))
                        if run_sound_cd <= 0:
                            walk_sound.play()  # Случайный выбор звука удара
                            run_sound_cd = 30
                        if run_sound_cd > 0:
                            run_sound_cd -= 1
                    else:
                        screen.blit(walk_left[player_anim_count // 9 % len(walk_left)], (player_x, player_y - 2))
                        player_anim_count += 1
                        if run_sound_cd2 <= 0:
                            walk_sound.play()  # Случайный выбор звука удара
                            run_sound_cd2 = 30
                        if run_sound_cd2 > 0:
                            run_sound_cd2 -= 1
                else:
                    idle_status = True
                    if front == "right":
                        screen.blit(stay[0], (player_x, player_y))
                    elif front == "left":
                        screen.blit(left_stay[0], (player_x, player_y))

                if keys[pygame.K_a] and player_x > 20:
                    if level == 2:
                        if (not player_rect.colliderect(door_rect) and
                                not player_rect.colliderect(door_rect2) and
                                not player_rect.colliderect(door_rect3) and
                                not player_rect.colliderect(door_rect4) and
                                not player_rect.colliderect(door_rect5) and
                                not player_rect.colliderect(door_rect6) and
                                not player_rect.colliderect(door_rect7)):
                                    player_x -= player_speed
                                    trip -= player_speed
                    if level == 1:
                        player_x -= player_speed
                        trip -= player_speed
                        if player_x < CAMERA_OFFSET:
                           push_amount = (CAMERA_OFFSET - player_x) * 0.1



                        else:
                           bg_scroll += scroll_speed

                    if keys[pygame.K_LSHIFT]:
                        if level == 2:
                            if (not player_rect.colliderect(door_rect) and
                                    not player_rect.colliderect(door_rect2) and
                                    not player_rect.colliderect(door_rect3) and
                                    not player_rect.colliderect(door_rect4) and
                                    not player_rect.colliderect(door_rect5) and
                                    not player_rect.colliderect(door_rect6) and
                                    not player_rect.colliderect(door_rect7)):
                                        player_x -= player_speed * 1
                                        trip -= player_speed * 0.25
                                        bg_scroll += scroll_speed * 0.15

                        if level == 1:
                                        player_x -= player_speed * 0.25
                                        trip -= player_speed * 0.25
                                        bg_scroll += scroll_speed * 0.1





                elif keys[pygame.K_d] and player_x < 1385:
                    if level == 2:
                        if (not player_rect.colliderect(door_rect) and
                            not player_rect.colliderect(door_rect2) and
                            not player_rect.colliderect(door_rect3) and
                            not player_rect.colliderect(door_rect4) and
                            not player_rect.colliderect(door_rect5) and
                            not player_rect.colliderect(door_rect6) and
                            not player_rect.colliderect(door_rect7)):

                                player_x += player_speed
                                trip += player_speed
                    if level == 1:
                        if player_x > 1440 - CAMERA_OFFSET:
                            push_amount = (player_x - (1440 - CAMERA_OFFSET)) * 0.015
                            player_x -= push_amount
                            trip -= push_amount
                            player_x += player_speed
                            trip += player_speed
                        else:
                            bg_scroll -= scroll_speed * 0.2

                    if keys[pygame.K_LSHIFT] and player_x < 3300:
                        if level == 2:
                            if (not player_rect.colliderect(door_rect) and
                                not player_rect.colliderect(door_rect2) and
                                not player_rect.colliderect(door_rect3) and
                                not player_rect.colliderect(door_rect4) and
                                not player_rect.colliderect(door_rect5) and
                                not player_rect.colliderect(door_rect6) and
                                not player_rect.colliderect(door_rect7)):

                                    player_x += player_speed * 0.8
                                    trip += player_speed * 0.9
                                    bg_scroll -= scroll_speed * 0.05

                        if level == 1:
                                   player_x += player_speed * 0.25
                                   trip += player_speed * 0.5
                                   bg_scroll -= scroll_speed * 2






                for bullet in player_bullets[:]:

                    bullet['x'] += 10 * bullet['direction']  # Движение пули
                    screen.blit(bullet_surface, (bullet['x'], bullet['y']))

                    # Проверка выхода за границы
                    if bullet['x'] < -50 or bullet['x'] > 1500:
                        bullet['active'] = False
                        player_bullets.remove(bullet)
                        continue

                    bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 10, 5)

                    if level == 1:
                       if bullet_rect.colliderect(npc1_rect):

                           npc_health -= 35  # Наносим ур8он 35
                           bullet['active'] = False
                           player_bullets.remove(bullet)

                    if level == 2:
                        if bullet_rect.colliderect(npc1_rect_l2):
                            npc1_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)

                        if bullet_rect.colliderect(npc2_rect_l2):
                            npc2_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)

                        if bullet_rect.colliderect(npc3_rect_l2):
                            npc3_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)

                        if bullet_rect.colliderect(npc4_rect_l2):
                            npc4_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)

                        if bullet_rect.colliderect(npc5_rect_l2):
                            npc5_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)



                        if bullet_rect.colliderect(npc7_rect_l2):
                            npc7_health_l2 -= 35  # Наносим ур8он 35
                            bullet['active'] = False
                            player_bullets.remove(bullet)



                        if (bullet_rect.colliderect(door_rect) or
                            bullet_rect.colliderect(door_rect2) or
                            bullet_rect.colliderect(door_rect3) or
                            bullet_rect.colliderect(door_rect4) or
                            bullet_rect.colliderect(door_rect5) or
                            bullet_rect.colliderect(door_rect6) or
                            bullet_rect.colliderect(door_rect7)):
                                bullet['active'] = False
                                player_bullets.remove(bullet)

                        if bullet_rect.colliderect(boss_rect):
                            if hard == "hard":
                                boss_hp - 25
                            else:
                                boss_hp -= 35  # Наносим ур8он 35
                                bullet['active'] = False
                                player_bullets.remove(bullet)






        if level == 1:


            lower_space = pygame.Surface((1440, 200))
            lower_space.fill((46, 46, 48))
            screen.blit(lower_space, (0, 480))
            for npc in npc_list_in_game[:]:
                npc.update()
                # Создаем Rect для текущего NPC


                # Проверка столкновения с пулями
                for bullet in player_bullets[:]:
                    bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 10, 5)
                    if bullet_rect.colliderect(npc.rect):
                        npc.hp -= 50
                        player_bullets.remove(bullet)

                # Логика состояний NPC
                if npc.hp <= 0 and npc.state != "dead":
                    npc.state = "dead"
                    npc.death_timer = 0

                if npc.state == "dead":
                    if npc.should_remove:
                        npc_list_in_game.remove(npc)
                    else:
                        npc.draw(screen)
                    continue

                # Определение поведения
                if player_rect.colliderect(npc.rect):
                    npc.state = "attack"
                    if keys[pygame.K_f]:
                        is_attaking = True
                        npc.hp -= 10
                        if hit_sound_cd21 <= 0:
                            random.choice(hit_sounds2).play()  # Случайный выбор звука удара
                            hit_sound_cd21 = 15
                        if hit_sound_cd21 > 0:
                            hit_sound_cd21 -= 1

                elif abs(npc.x - player_x) < 1350:
                    npc.state = "run"
                else:
                    npc.state = "idle"

                npc.draw(screen)

                # Обработка состояний


                # Удаление NPC за пределами экрана
                if npc.x < -50:
                    npc_list_in_game.remove(npc)

                if npc1_x < player_x - 150:
                    npc1_left_pos = 2
                    npc1_x_move = 2
                elif npc1_x > player_x:
                    npc1_left_pos = 1
                    npc1_x_move = 1

                npc_alive = 1
                if npc_alive == 1:
                    npc1_rect = pygame.Rect(npc1_x, npc1_y,
                                            npc1_shot_left[0].get_width(),
                                            npc1_shot_left[0].get_height())
                if npc_health <= 0:
                    npc_alive = 2  # Устанавливаем состояние "мертв"
                    npc1_shot_anim_count = 0  # Сбрасываем счетчик анимации

                if npc_alive == 1:

                    npc1_shoot_timer += 1
                    if npc1_shoot_timer >= 120:  # 4 секунды при 60 FPS
                        npc1_shoot_timer = 0
                        is_npc1_shooting = True
                        npc1_shot_anim_count = 0
                        bullet_active = True
                        if npc1_x_move == 1:
                            bullet_x = npc1_x - 25  # Начальная позиция пули
                        elif npc1_x_move == 2:
                            bullet_x = npc1_x + 25
                        bullet_y = 426  # Позиция по Y

                    if is_npc1_shooting:
                        if hit_sound_cd29 <= 0:
                            shot3_sound.play()
                            hit_sound_cd29 = 60
                        if hit_sound_cd29 > 0:
                            hit_sound_cd29 -= 1
                        npc1_shot_anim_count += 1
                        if npc1_x_move == 1:
                            screen.blit(npc1_shot_left[npc1_shot_anim_count // 4 % len(npc1_shot_left)], (npc1_x, 390))
                        elif npc1_x_move == 2:
                            screen.blit(npc1_shot_right[npc1_shot_anim_count // 4 % len(npc1_shot_left)], (npc1_x, 390))
                        if npc1_shot_anim_count >= 70:
                            is_npc1_shooting = False
                    else:
                        if npc1_left_pos == 1:
                            screen.blit(npc1_walk_left[player_anim_count // 4 % len(npc1_walk_left)], (npc1_x, 390))
                        elif npc1_left_pos == 2:
                            screen.blit(npc1_idle_right[0], (npc1_x, 390))

                if npc_health <= 0 and npc_alive == 1:
                    npc_alive = 2
                    npc_death_anim_count = 0
                    npc_death_timer = 0

                elif npc_alive == 2:

                    npc_death_anim_count += 1
                    current_frame = npc_death_anim_count // npc_death_frame_duration

                    if current_frame < len(npc1_dead_left):
                        screen.blit(npc1_dead_left[current_frame], (npc1_x, 390))

                    else:

                        npc_alive = 0  # Состояние "можно удалить"
                if hp <= 0:
                    gameplay = False

            for npc in npc_list_in_game9[:]:
                npc.update()
                # Создаем Rect для текущего NPC

                # Проверка столкновения с пулями
                for bullet in player_bullets[:]:
                    bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                    if bullet_rect.colliderect(npc.rect):
                        npc.hp -= 50
                        player_bullets.remove(bullet)

                # Логика состояний NPC
                if npc.hp <= 0 and npc.state != "dead":
                    npc.state = "dead"
                    npc.death_timer = 0

                if npc.state == "dead":
                    npc9_max += 1
                    if npc.should_remove:
                        npc_list_in_game9.remove(npc)
                    else:
                        npc.draw(screen)
                    continue

                # Определение поведения
                if player_rect.colliderect(npc.rect):
                    npc.state = "attack"
                    if hit9_sound_cd <= 0:
                        random.choice(hit_sounds).play()  # Случайный выбор звука удара
                        hit9_sound_cd = 15
                    if hit9_sound_cd > 0:
                        hit9_sound_cd -= 1
                    if keys[pygame.K_f]:
                        is_attaking = True
                        npc.hp -= 10

                elif abs(npc.x - player_x) < 350:
                    npc.state = "run"
                else:
                    npc.state = "idle"

                npc.draw(screen)

            for npc in npc_list_in_game16[:]:
                npc.update()
                # Создаем Rect для текущего NPC

                # Проверка столкновения с пулями
                for bullet in player_bullets[:]:
                    bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                    if bullet_rect.colliderect(npc.rect):
                        npc.hp -= 50
                        player_bullets.remove(bullet)

                # Логика состояний NPC
                if npc.hp <= 0 and npc.state != "dead":
                    npc.state = "dead"
                    npc.death_timer = 0
                    npc16_max += 1

                if npc.state == "dead":
                    if npc.should_remove:
                        npc_list_in_game16.remove(npc)
                    else:
                        npc.draw(screen)
                    continue

                # Определение поведения
                if player_rect.colliderect(npc.rect):
                    npc.state = "attack"
                    if hit2_sound_cd <= 0:
                        random.choice(hit_sounds).play()
                        hit2_sound_cd = 15
                    if hit2_sound_cd > 0:
                        hit2_sound_cd -= 1
                    if keys[pygame.K_f]:
                        is_attaking = True
                        npc.hp -= 1.5
                        if hit_sound_cd23 <= 0:
                            random.choice(hit_sounds2).play()  # Случайный выбор звука удара
                            hit_sound_cd23 = 15
                        if hit_sound_cd23 > 0:
                            hit_sound_cd23 -= 1

                elif abs(npc.x - player_x) < 1250:
                    npc.state = "run"
                else:
                    npc.state = "idle"

                npc.draw(screen)





        elif level == 2:

            screen.blit(down, (-63, 480))
            screen.blit(down, (465, 480))
            screen.blit(down, (465 + 528, 480))



            screen.blit(hp_text, (50, 20))
            build = True
            doors = True
            elevators  = True
            npc1_l2 = True
            npc2_l2 = True
            npc3_l2 = True
            npc4_l2 = True
            npc5_l2 = True
            npc6_l2 = True
            npc7_l2 = True
            npc_fighters = True
            npc_shooters = True
            boss = True

            npc1_rect = pygame.Rect(1600, 0,
                                npc1_shot_left[0].get_width(),
                                npc1_shot_left[0].get_height())

            elevator_cooldown += 1

            if idle_status == True:
                if floor == 1:
                  player_height = 77
                elif floor == 2:
                    player_height = 79
                elif floor == 3:
                    player_height = 75

            if player_y < 319 and player_y > 179:
                floor = 2
            elif player_y < 178 and player_y > 21:
                floor = 3
            elif player_y < 460 and player_y > 320:
                floor = 1

            update_player()
            if build:
                last_brick_x1 = 0
                while last_brick_x1 < 1440:
                    screen.blit(brick, (last_brick_x1, 460))  # <-- передаём кортеж (x, y)
                    last_brick_x1 += 20

                last_brick_x2 = 0
                while last_brick_x2 < 1440:
                    screen.blit(brick, (last_brick_x2, 320))  # <-- передаём кортеж (x, y)
                    last_brick_x2 += 20

                last_brick_x3 = 0
                while last_brick_x3 < 1440:
                    screen.blit(brick, (last_brick_x3, 180))  # <-- передаём кортеж (x, y)
                    last_brick_x3 += 20

                last_brick_x4 = 0
                while last_brick_x4 < 1440:
                    screen.blit(brick, (last_brick_x4, 20))  # <-- передаём кортеж (x, y)
                    last_brick_x4 += 20

                last_brick_y1 = 460
                while last_brick_y1 > 20:
                    screen.blit(brick, (0, last_brick_y1))  # <-- передаём кортеж (x, y)
                    last_brick_y1 -= 20

                last_brick_y2 = 460
                while last_brick_y2 > 20:
                    screen.blit(brick, (1420, last_brick_y2))  # <-- передаём кортеж (x, y)
                    last_brick_y2 -= 20

                last_brick_y3 = 360
                while last_brick_y3 > 320:
                    screen.blit(brick, (466, last_brick_y3))  # <-- передаём кортеж (x, y)
                    last_brick_y3 -= 20


                last_brick_y4 = 360
                while last_brick_y4 > 320:
                    screen.blit(brick, (932, last_brick_y4))  # <-- передаём кортеж (x, y)
                    last_brick_y4 -= 20

                last_brick_y5 = 220
                while last_brick_y5 > 180:
                    screen.blit(brick, (350, last_brick_y5))
                    last_brick_y5 -= 20

                last_brick_y6 = 220
                while last_brick_y6 > 180:
                    screen.blit(brick, (700, last_brick_y6))
                    last_brick_y6 -= 20

                last_brick_y7 = 220
                while last_brick_y7 > 180:
                    screen.blit(brick, (1050, last_brick_y7))
                    last_brick_y7 -= 20

                last_brick_y8 = 80
                while last_brick_y8 > 20:
                    screen.blit(brick, (300, last_brick_y8))
                    last_brick_y8 -= 20

                last_brick_y9 = 80
                while last_brick_y9 > 20:
                    screen.blit(brick, (1250, last_brick_y9))
                    last_brick_y9 -= 20

            if doors:
                door_close = pygame.Surface((13, 80))
                door_close.fill((51, 10, 4))
                door_open = pygame.Surface((35, 80))
                door_open.fill((51, 10, 4))
                if door_status == "close":
                   door_rect = pygame.Rect(465, 380,
                                      door_close.get_width(),
                                      door_close.get_height())
                   if player_rect.colliderect(door_rect):
                       advice = pygame.font.SysFont('Arial', 16)
                       door_advice = advice.render('Нажмите Е', False, (6, 128, 16))
                       screen.blit(door_advice, (380, 370))
                else:
                    door_rect =  pygame.Rect(1500, 0, 1, 1)
                if door_rect.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status = "open"
                if door_status == "close":
                  screen.blit(door_close, (470, 380))

                elif door_status == "open":
                    screen.blit(door_open, (470, 380))

                if door_status2 == "close":
                  door_rect2 = pygame.Rect(932, 380,
                                        door_close.get_width(),
                                        door_close.get_height())
                else:
                    door_rect2 = pygame.Rect(1501, 0, 1, 1)
                if door_rect2.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status2 = "open"
                if door_status2 == "close":
                    screen.blit(door_close, (937, 380))

                elif door_status2 == "open":
                    screen.blit(door_open, (937, 380))

                if door_status3 == "close":
                  door_rect3 = pygame.Rect(350, 240,
                                         door_close.get_width(),
                                         door_close.get_height())
                else:
                    door_rect3 =  pygame.Rect(1502, 0, 1, 1)
                if door_rect3.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status3 = "open"
                if door_status3 == "close":
                    screen.blit(door_close, (355, 240))

                elif door_status3 == "open":
                    screen.blit(door_open, (355, 240))

                if door_status4 == "close":
                   door_rect4 = pygame.Rect(700, 240,
                                         door_close.get_width(),
                                         door_close.get_height())
                else:

                    door_rect4 = pygame.Rect(1503, 0, 1, 1)
                if door_rect4.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status4 = "open"
                if door_status4 == "close":
                    screen.blit(door_close, (705, 240))

                elif door_status4 == "open":
                    screen.blit(door_open, (705, 240))

                if door_status5 == "close":
                  door_rect5 = pygame.Rect(1050, 240,
                                         door_close.get_width(),
                                         door_close.get_height())
                else:
                    door_rect5 =  pygame.Rect(1504, 0, 1, 1)
                if door_rect5.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status5 = "open"
                if door_status5 == "close":
                    screen.blit(door_close, (1055, 240))

                elif door_status5 == "open":
                    screen.blit(door_open, (1055, 240))
                if door_status6 == "close":
                  door_rect6 = pygame.Rect(300, 100,
                                         door_close.get_width(),
                                         door_close.get_height())
                else:
                    door_rect6 =  pygame.Rect(1500, 0, 1, 1)
                if door_rect6.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status6 = "open"
                if door_status6 == "close":
                    screen.blit(door_close, (305, 100))

                elif door_status6 == "open":
                    screen.blit(door_open, (305, 100))

                if door_status7 == "close":
                  door_rect7 = pygame.Rect(1250, 100,
                                         door_close.get_width(),
                                         door_close.get_height())
                else:
                    door_rect7 =  pygame.Rect(1509, 0, 1, 1)
                if door_rect7.colliderect(player_rect) and keys[pygame.K_e]:
                    door_sound.play()
                    door_status7 = "open"
                if door_status7 == "close":
                    screen.blit(door_close, (1255, 100))

                elif door_status7 == "open":
                    screen.blit(door_open, (1255, 100))
            if elevators:

                advice = pygame.font.SysFont('Arial', 16)
                elevator_advice = advice.render('Нажмите Е', False, (6, 128, 16))

                elevator_rect1 = elevator.get_rect(topleft=(1300, 365))
                if player_rect.colliderect(elevator_rect1):
                    screen.blit(elevator_advice, (1337, 345))
                    if keys[pygame.K_e] and elevator_cooldown >= 45:
                      player_y -= 140
                      elevator_cooldown = 0

                elevator_rect2 = elevator.get_rect(topleft=(1300, 225))
                if player_rect.colliderect(elevator_rect2) and keys[pygame.K_e] and elevator_cooldown >= 45:
                    player_y += 140
                    elevator_cooldown = 0

                elevator_rect3 = elevator.get_rect(topleft=(40, 225))
                if player_rect.colliderect(elevator_rect3) and keys[pygame.K_e] and elevator_cooldown >= 45:
                    player_y -= 140
                    elevator_cooldown = 0

                elevator_rect4 = elevator.get_rect(topleft=(40, 85))
                if player_rect.colliderect(elevator_rect4) and keys[pygame.K_e] and elevator_cooldown >= 45:
                    player_y += 140
                    elevator_cooldown = 0

            if not game_won:
                mouse = pygame.mouse.get_pos()
                if player_rect.colliderect(safer_rect):
                   if npc_dead_cout >= 6 and not boss_alive:
                       if lang == "rus":
                         safer_advice =  advice.render('Открыть сейф (E)', False, (6, 128, 16))
                       else:
                           safer_advice = advice.render('OPEN (E)', False, (6, 128, 16))
                       screen.blit(safer_advice, (1280, 90))
                       if keys[pygame.K_e]:
                           game_won = True
                   else:
                       safer_advice_false = advice.render('Сначала убей всех!', False, (6, 128, 16))
                       screen.blit(safer_advice_false, (1280, 90))
            else:
                    screen.fill((0, 0, 0))
                    win_sound.play()
                    font = pygame.font.SysFont('Arial', 62)
                    if lang == "rus":
                        win_text = font.render("ТЫ ПОБЕДИЛ!", True, (255, 255, 255))
                    elif lang == "eng":
                        win_text = font.render("YOU WON!", True, (255, 255, 255))
                    screen.blit(win_text, (500, 200))
                    screen.blit(restart_label, restart_label_rect2)
                    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                        button_sound.play()
                        gameplay = True
                        hp = 350
                        player_x = 30
                        player_y = 390
                        npc2_alive_l2 = 1
                        npc1_health_l2 = 100
                        npc1_alive_l2 = 1
                        npc2_health_l2 = 100
                        npc4_alive_l2 = 1
                        npc4_health_l2 = 100
                        npc5_alive_l2 = 1
                        npc5_health_l2 = 100
                        npc6_alive_l2 = 1
                        npc6_health_l2 = 100
                        npc7_alive_l2 = 1
                        npc7_health_l2 = 100
                        npс8_alive_l2 = 1
                        npc8_health_l2 = 100
                        npc3_alive_l2 = 1
                        npc3_health_l2 = 100
                        game_won = False
                        npc_dead_cout = 0
                        npc_list_in_game8.clear()
                        npc_list_in_game9.clear()
                        npc_list_in_game10.clear()
                        npc_list_in_game11.clear()
                        npc_list_in_game12.clear()
                        npc_list_in_game13.clear()
                        npc_list_in_game14.clear()
                        npc_list_in_game15.clear()
                        npc_list_in_game16.clear()
                        npc_list_in_game16.append(NPC2(600, 100))
                        npc_list_in_game15.append(NPC2(500, 100))
                        npc_list_in_game14.append(NPC2(300, 240))
                        npc_list_in_game13.append(NPC2(1100, 240))
                        npc_list_in_game12.append(NPC2(500, 240))
                        npc_list_in_game11.append(NPC2(800, 240))
                        npc_list_in_game10.append(NPC2(1000, 380))
                        npc_list_in_game9.append(NPC2(400, 380))
                        npc_list_in_game8.append(NPC2(700, 380))
                        door_status = "close"
                        door_status2 = "close"
                        door_status3 = "close"
                        door_status4 = "close"
                        door_status5 = "close"
                        door_status6 = "close"
                        door_status7 = "close"
                        door_status8 = "close"
                        boss_alive = True
                        boss_hp = 500
                        boss_x = 750
            if npc_shooters:
                if npc1_l2:
                    if npc1_x_l2 < player_x - 20:
                        npc1_left_pos_l2 = 2
                        npc1_x_move_l2 = 2
                    elif npc1_x_l2 > player_x:
                        npc1_left_pos_l2 = 1
                        npc1_x_move_l2 = 1

                    npc1_alive_l2 = 1
                    if npc1_alive_l2 == 1:
                        npc1_rect_l2 = pygame.Rect(npc1_x_l2, npc1_y_l2,
                                                npc1_shot_left[0].get_width(),
                                                npc1_shot_left[0].get_height())
                    if npc1_health_l2 <= 0:
                        npc1_alive_l2 = 2  # Устанавливаем состояние "мертв"
                        npc1_shot_anim_count_l2 = 0  # Сбрасываем счетчик анимации

                    if npc1_alive_l2 == 1:

                        npc1_shoot_timer_l2 += 1
                        if npc1_shoot_timer_l2 >= 140  and door_status == "open" and player_y > 380:
                            npc1_shoot_timer_l2 = 0
                            is_npc1_shooting_l2 = True
                            npc1_shot_anim_count_l2 = 0
                            bullet_active2 = True
                            if npc1_x_move_l2 == 1:
                                bullet_x2 = npc1_x_l2 - 25  # Начальная позиция пули
                            elif npc1_x_move_l2 == 2:
                                bullet_x2 = npc1_x_l2 + 25
                            bullet_y2 = 426  # Позиция по Y
                            warn_active = True
                            warn_duration = 0
                            warn_x = npc1_x_l2 + 25.5
                            warn_y = npc1_y_l2 - 5

                        # Отображение восклицательного знака
                        if warn_active and warn_max <= 1:
                            screen.blit(warn, (warn_x, warn_y))
                            warn_duration += 1
                            if warn_duration >= 90:  # Показываем 1 секунду (60 кадров)
                                warn_active = False
                                warn_max += 1




                        if is_npc1_shooting_l2:
                            npc1_shot_anim_count_l2 += 1
                            if npc1_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc1_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc1_x_l2, 383))
                            elif npc1_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc1_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc1_x_l2, 383))
                            if npc1_shot_anim_count_l2 >= 110:
                                is_npc1_shooting_l2 = False
                        else:
                            if npc1_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc1_x_l2, 390))
                            elif npc1_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc1_x_l2, 390))

                    if npc1_health_l2 <= 0 and npc1_alive_l2 == 1:
                        npc1_alive_l2 = 2
                        npc1_death_anim_count_l2 = 0
                        npc1_death_timer_l2 = 0

                    elif npc1_alive_l2 == 2:

                        npc1_death_anim_count_l2 += 1
                        current_frame_l2 = npc1_death_anim_count_l2 // npc1_death_frame_duration_l2
                        npc_dead_cout += 1

                        if current_frame_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame_l2], (npc1_x_l2, 387))
                            if dead_sound_cd <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd = 60
                            if dead_sound_cd > 0:
                                dead_sound_cd -= 1

                        else:

                            npc1_alive_l2 = 0

                            # Состояние "можно удалить"
                    if hp <= 0:
                        gameplay = False

                    if bullet_active2:
                        if npc1_x_move_l2 == 2:
                            bullet_x2 += 2.5
                        elif npc1_x_move_l2 == 1:
                            bullet_x2 -= 2.5
                        screen.blit(bullet_surface, (bullet_x2, bullet_y2))
                        if hit_sound_cd22 <= 0:
                            shot3_sound.play()
                            hit_sound_cd22 = 60
                        if hit_sound_cd22 > 0:
                            hit_sound_cd22 -= 1

                        bullet_rect2 = pygame.Rect(bullet_x2, bullet_y2, 10, 5)

                        if bullet_rect2.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                              hp -= 25
                            bullet_active2 = False
                        if npc1_x_l2 > player_x:
                            if bullet_x2 < player_x - 90:
                                bullet_active2 = False
                        if bullet_x2 > 1500:
                            bullet_active2 = False


                if npc2_l2:
                    if npc2_x_l2 < player_x - 20:
                        npc2_left_pos_l2 = 2
                        npc2_x_move_l2 = 2
                    elif npc2_x_l2 > player_x:
                        npc2_left_pos_l2 = 1
                        npc2_x_move_l2 = 1

                    npc2_alive_l2 = 1
                    if npc2_alive_l2 == 1:
                        npc2_rect_l2 = pygame.Rect(npc2_x_l2, npc2_y_l2,
                                                npc1_shot_left[0].get_width(),
                                                npc1_shot_left[0].get_height())
                    if npc2_health_l2 <= 0:
                        npc2_alive_l2 = 2  # Устанавливаем состояние "мертв"
                        npc2_shot_anim_count_l2 = 0  # Сбрасываем счетчик анимации

                    if npc2_alive_l2 == 1:

                        npc2_shoot_timer_l2 += 1
                        if npc2_shoot_timer_l2 >= 145 and door_status2 == "open" and player_y > 380:
                            npc2_shoot_timer_l2 = 0
                            is_npc2_shooting_l2 = True
                            npc2_shot_anim_count_l2 = 0
                            bullet_active3 = True
                            if npc2_x_move_l2 == 1:
                                bullet_x3 = npc2_x_l2 - 25  # Начальная позиция пули
                            elif npc2_x_move_l2 == 2:
                                bullet_x3 = npc2_x_l2 + 25
                            bullet_y3 = 426  # Позиция по Y

                        if is_npc2_shooting_l2:
                            npc2_shot_anim_count_l2 += 1
                            if npc2_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc2_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc2_x_l2, 383))
                            elif npc2_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc2_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc2_x_l2, 383))
                            if npc2_shot_anim_count_l2 >= 110:
                                is_npc2_shooting_l2 = False
                        else:
                            if npc2_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc2_x_l2, 390))
                            elif npc2_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc2_x_l2, 390))

                    if npc2_health_l2 <= 0 and npc2_alive_l2 == 1:
                        npc2_alive_l2 = 2
                        npc2_death_anim_count_l2 = 0
                        npc2_death_timer_l2 = 0

                    elif npc2_alive_l2 == 2:

                        npc2_death_anim_count_l2 += 1
                        current_frame2_l2 = npc2_death_anim_count_l2 // npc2_death_frame_duration_l2
                        npc_dead_cout += 1

                        if current_frame2_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame2_l2], (npc2_x_l2, 387))
                            if dead_sound_cd2 <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd2 = 60
                            if dead_sound_cd2 > 0:
                                dead_sound_cd2 -= 1

                        else:

                            npc2_alive_l2 = 0  # Состояние "можно удалить"
                    if hp <= 0:
                        gameplay = False

                    if bullet_active3:
                        if npc2_x_move_l2 == 2:
                            bullet_x3 += 2.5
                        elif npc2_x_move_l2 == 1:
                            bullet_x3 -= 2.5
                        screen.blit(bullet_surface, (bullet_x3, bullet_y3))
                        if hit_sound_cd23 <= 0:
                            shot3_sound.play()
                            hit_sound_cd23 = 60
                        if hit_sound_cd23 > 0:
                            hit_sound_cd23 -= 1
                        bullet_rect3 = pygame.Rect(bullet_x3, bullet_y3, 10, 5)

                        if bullet_rect3.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                              hp -= 25
                            bullet_active3 = False
                        if npc2_x_l2 > player_x:
                            if bullet_x3 < player_x - 90:
                                bullet_active3 = False
                        if bullet_x3 > 1500:
                            bullet_active3= False

                if npc3_l2:
                    if npc3_x_l2 < player_x - 20:
                        npc3_left_pos_l2 = 2
                        npc3_x_move_l2 = 2
                    elif npc3_x_l2 > player_x:
                        npc3_left_pos_l2 = 1
                        npc3_x_move_l2 = 1

                    npc3_alive_l2 = 1
                    if npc3_alive_l2 == 1:
                        npc3_rect_l2 = pygame.Rect(npc3_x_l2, npc3_y_l2,
                                                npc1_shot_left[0].get_width(),
                                                npc1_shot_left[0].get_height())
                    if npc3_health_l2 <= 0:
                        npc3_alive_l2 = 2  # Устанавливаем состояние "мертв"
                        npc3_shot_anim_count_l2 = 0  # Сбрасываем счетчик анимации

                    if npc3_alive_l2 == 1:

                        npc3_shoot_timer_l2 += 1
                        if npc3_shoot_timer_l2 >= 135 and player_x < 1000 and player_y < 165:
                            npc3_shoot_timer_l2 = 0
                            is_npc3_shooting_l2 = True
                            npc3_shot_anim_count_l2 = 0
                            bullet_active4 = True
                            if npc3_x_move_l2 == 1:
                                bullet_x4 = npc3_x_l2 - 25  # Начальная позиция пули
                            elif npc3_x_move_l2 == 2:
                                bullet_x4 = npc3_x_l2 + 25
                            bullet_y4 = 146  # Позиция по Y

                        if is_npc3_shooting_l2:
                            npc3_shot_anim_count_l2 += 1
                            if npc3_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc3_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc3_x_l2, 103))
                            elif npc3_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc3_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc3_x_l2, 103))
                            if npc3_shot_anim_count_l2 >= 110:
                                is_npc3_shooting_l2 = False
                        else:
                            if npc3_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc3_x_l2, 110))
                            elif npc3_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc3_x_l2, 110))

                    if npc3_health_l2 <= 0 and npc3_alive_l2 == 1:
                        npc3_alive_l2 = 2
                        npc3_death_anim_count_l2 = 0
                        npc3_death_timer_l2 = 0

                    elif npc3_alive_l2 == 2:

                        npc3_death_anim_count_l2 += 1
                        current_frame3_l2 = npc3_death_anim_count_l2 // npc3_death_frame_duration_l2

                        if current_frame3_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame3_l2], (npc3_x_l2, 107))
                            if dead_sound_cd3 <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd3 = 60
                            if dead_sound_cd3 > 0:
                                dead_sound_cd3 -= 1
                            npc_dead_cout += 1

                        else:

                            npc3_alive_l2 = 0  # Состояние "можно удалить"
                    if hp <= 0:
                        gameplay = False

                    if bullet_active4:
                        if npc3_x_move_l2 == 2:
                            bullet_x4 += 3
                        elif npc3_x_move_l2 == 1:
                            bullet_x4 -= 3
                        screen.blit(bullet_surface, (bullet_x4, bullet_y4))
                        if hit_sound_cd24 <= 0:
                            shot3_sound.play()
                            hit_sound_cd24 = 60
                        if hit_sound_cd24 > 0:
                            hit_sound_cd24 -= 1

                        bullet_rect4 = pygame.Rect(bullet_x4, bullet_y4, 10, 5)

                        if bullet_rect4.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                              hp -= 25
                            bullet_active4 = False
                        if npc3_x_l2 > player_x:
                            if bullet_x4 < player_x - 90:
                                bullet_active4 = False
                        if bullet_x4 > 1500:
                            bullet_active4= False

                if npc4_l2:
                    if npc4_x_l2 < player_x - 20:
                        npc4_left_pos_l2 = 2
                        npc4_x_move_l2 = 2
                    elif npc4_x_l2 > player_x:
                        npc4_left_pos_l2 = 1
                        npc4_x_move_l2 = 1

                    npc4_alive_l2 = 1
                    if npc4_alive_l2 == 1:
                        npc4_rect_l2 = pygame.Rect(npc4_x_l2, npc4_y_l2,
                                                npc1_shot_left[0].get_width(),
                                                npc1_shot_left[0].get_height())
                    if npc4_health_l2 <= 0:
                        npc4_alive_l2 = 2  # Устанавливаем состояние "мертв"
                        npc4_shot_anim_count_l2 = 0  # Сбрасываем счетчик анимации

                    if npc4_alive_l2 == 1:

                        npc4_shoot_timer_l2 += 1
                        if npc4_shoot_timer_l2 >= 140 and door_status5 == "open" and player_y < 300 and player_y > 160:
                            npc4_shoot_timer_l2 = 0
                            is_npc4_shooting_l2 = True
                            npc34_shot_anim_count_l2 = 0
                            bullet_active5 = True
                            if npc4_x_move_l2 == 1:
                                bullet_x5 = npc4_x_l2 - 25  # Начальная позиция пули
                            elif npc4_x_move_l2 == 2:
                                bullet_x5 = npc4_x_l2 + 25
                            bullet_y5 = 286  # Позиция по Y

                        if is_npc4_shooting_l2:
                            npc4_shot_anim_count_l2 += 1
                            if npc4_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc4_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc4_x_l2, 243))
                            elif npc4_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc4_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc4_x_l2, 243))
                            if npc4_shot_anim_count_l2 >= 110:
                                is_npc3_shooting_l2 = False
                        else:
                            if npc4_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc4_x_l2, 250))
                            elif npc4_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc4_x_l2, 250))

                    if npc4_health_l2 <= 0 and npc4_alive_l2 == 1:
                        npc4_alive_l2 = 2
                        npc4_death_anim_count_l2 = 0
                        npc4_death_timer_l2 = 0

                    elif npc4_alive_l2 == 2:

                        npc4_death_anim_count_l2 += 1
                        current_frame4_l2 = npc4_death_anim_count_l2 // npc4_death_frame_duration_l2

                        if current_frame4_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame4_l2], (npc4_x_l2, 247))
                            if dead_sound_cd4 <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd4 = 60
                            if dead_sound_cd4 > 0:
                                dead_sound_cd4-= 1
                            npc_dead_cout += 1

                        else:

                            npc4_alive_l2 = 0  # Состояние "можно удалить"
                    if hp <= 0:
                        gameplay = False

                    if bullet_active5:
                        if npc4_x_move_l2 == 2:
                            bullet_x5 += 2.75
                        elif npc4_x_move_l2 == 1:
                            bullet_x4 -= 2.75
                        screen.blit(bullet_surface, (bullet_x5, bullet_y5))
                        if hit_sound_cd25 <= 0:
                            shot3_sound.play()
                            hit_sound_cd25 = 60
                        if hit_sound_cd25 > 0:
                            hit_sound_cd25 -= 1

                        bullet_rect5 = pygame.Rect(bullet_x5, bullet_y5, 10, 5)

                        if bullet_rect5.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                                hp -= 25
                            bullet_active5 = False
                        if npc4_x_l2 > player_x:
                            if bullet_x5 < player_x - 90:
                                bullet_active5 = False
                        if bullet_x5 > 1500:
                            bullet_active5 = False

                if npc5_l2:
                    if player_y > npc5_y_l2 + 20:

                        npc5_left_pos_l2 = 2
                        npc5_x_move_l2 = 2
                    if not player_y > npc5_y_l2 + 20:
                        if npc5_x_l2 < player_x - 20:
                            npc5_left_pos_l2 = 2
                            npc5_x_move_l2 = 2

                        elif npc5_x_l2 > player_x:
                            npc5_left_pos_l2 = 1
                            npc5_x_move_l2 = 1

                    npc5_alive_l2 = 1
                    if npc5_alive_l2 == 1:
                        npc5_rect_l2 = pygame.Rect(npc5_x_l2, npc5_y_l2,
                                                   npc1_shot_left[0].get_width(),
                                                   npc1_shot_left[0].get_height())
                    if npc5_health_l2 <= 0:
                        npc5_alive_l2 = 2  # Устанавливаем состояние "мертв"
                        npc5_shot_anim_count_l2 = 0  # Сбрасываем счетчик анимации

                    if npc5_alive_l2 == 1:

                        npc5_shoot_timer_l2 += 1
                        if npc5_shoot_timer_l2 >= 105 and player_y < 300 and player_y > 160 and door_status4 == "open":
                            npc5_shoot_timer_l2 = 0
                            is_npc5_shooting_l2 = True
                            npc5_shot_anim_count_l2 = 0
                            bullet_active6 = True
                            if npc5_x_move_l2 == 1:
                                bullet_x6 = npc5_x_l2 - 25  # Начальная позиция пули
                            elif npc5_x_move_l2 == 2:
                                bullet_x6 = npc5_x_l2 + 25
                            bullet_y6 = 280 # Позиция по Y

                        if is_npc5_shooting_l2:
                            npc5_shot_anim_count_l2 += 1
                            if npc5_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc5_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc5_x_l2, 243))
                            elif npc5_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc5_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc5_x_l2, 243))
                            if npc5_shot_anim_count_l2 >= 110:
                                is_npc5_shooting_l2 = False
                        else:
                            if npc5_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc5_x_l2, 250))
                            elif npc5_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc5_x_l2, 250))

                    if npc5_health_l2 <= 0 and npc5_alive_l2 == 1:
                        npc5_alive_l2 = 2
                        npc5_death_anim_count_l2 = 0
                        npc5_death_timer_l2 = 0

                    elif npc5_alive_l2 == 2:

                        npc5_death_anim_count_l2 += 1
                        current_frame_l2 = npc5_death_anim_count_l2 // npc5_death_frame_duration_l2

                        if current_frame_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame_l2], (npc5_x_l2, 247))
                            if dead_sound_cd5 <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd5 = 60
                            if dead_sound_cd5 > 0:
                                dead_sound_cd5 -= 1
                            npc_dead_cout += 1

                        else:

                            npc5_alive_l2 = 0  # Состояние "можно удалить"
                    if hp <= 0:
                        gameplay = False

                    if bullet_active6:
                        if npc5_x_move_l2 == 2:
                            bullet_x6 += 2.5
                        elif npc5_x_move_l2 == 1:
                            bullet_x6 -= 2.5
                        screen.blit(bullet_surface, (bullet_x6, bullet_y6))
                        if hit_sound_cd26 <= 0:
                            shot3_sound.play()
                            hit_sound_cd26 = 60
                        if hit_sound_cd26 > 0:
                            hit_sound_cd26 -= 1

                        bullet_rect6 = pygame.Rect(bullet_x6, bullet_y6, 10, 5)

                        if bullet_rect6.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                              hp -= 25
                            bullet_active6 = False
                        if npc5_x_l2 > player_x:
                            if bullet_x6 < player_x - 90:
                                bullet_active6 = False
                        if bullet_x6 > 1500:
                            bullet_active6 = False



                if npc7_l2:
                    if npc7_x_l2 < player_x - 15:
                        npc7_left_pos_l2 = 2
                        npc7_x_move_l2 = 2
                    elif npc7_x_l2 > player_x:
                        npc7_left_pos_l2 = 1
                        npc7_x_move_l2 = 1

                    npc7_alive_l2 = 1
                    if npc7_alive_l2 == 1:
                      npc7_rect_l2 = pygame.Rect(npc7_x_l2, npc7_y_l2,
                                               npc1_shot_left[0].get_width(),
                                               npc1_shot_left[0].get_height())
                    if npc7_health_l2 <= 0:
                        npc7_alive_l2 = 2
                        npc7_shot_anim_count_l2 = 0

                    if npc7_alive_l2 == 1:
                        npc7_shoot_timer_l2 += 1
                        if npc7_shoot_timer_l2 >= 55 and door_status7 == "open" and player_y < 165:
                            npc7_shoot_timer_l2 = 0
                            is_npc7_shooting_l2 = True
                            npc7_shot_anim_count_l2 = 0
                            bullet_active8 = True
                            if npc7_x_move_l2 == 1:
                                bullet_x8 = npc7_x_l2 - 25
                            elif npc7_x_move_l2 == 2:
                                bullet_x8 = npc7_x_l2 + 25
                            bullet_y8 = 140

                        if is_npc7_shooting_l2:
                            npc7_shot_anim_count_l2 += 1
                            if npc7_x_move_l2 == 1:
                                screen.blit(npc1_shot_left[npc7_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc7_x_l2, 107))
                            elif npc7_x_move_l2 == 2:
                                screen.blit(npc1_shot_right[npc7_shot_anim_count_l2 // 4 % len(npc1_shot_left)], (npc7_x_l2, 107))
                            if npc7_shot_anim_count_l2 >= 105:
                                is_npc7_shooting_l2 = False
                        else:
                            if npc7_left_pos_l2 == 1:
                                screen.blit(npc1_idle_left[0], (npc7_x_l2, 110))
                            elif npc7_left_pos_l2 == 2:
                                screen.blit(npc1_idle_right[0], (npc7_x_l2, 110))

                    if npc7_health_l2 <= 0 and npc7_alive_l2 == 1:
                        npc7_alive_l2 = 2
                        npc7_death_anim_count_l2 = 0
                        npc7_death_timer_l2 = 0

                    elif npc7_alive_l2 == 2:
                        npc7_death_anim_count_l2 += 1
                        current_frame7_l2 = npc7_death_anim_count_l2 // npc7_death_frame_duration_l2

                        if current_frame7_l2 < len(npc1_dead_left):
                            screen.blit(npc1_dead_left[current_frame7_l2], (npc7_x_l2, 117))
                            if dead_sound_cd7 <= 0:
                                random.choice(dead_sounds).play()  # Случайный выбор звука удара
                                dead_sound_cd7 = 60
                            if dead_sound_cd7 > 0:
                                dead_sound_cd7 -= 1
                            npc_dead_cout += 1
                        else:
                            npc7_alive_l2 = 0

                    if hp <= 0:
                        gameplay = False

                    if bullet_active8:
                        if npc7_x_move_l2 == 2:
                            bullet_x8 += 2
                        elif npc7_x_move_l2 == 1:
                            bullet_x8 -= 2
                        screen.blit(bullet_surface, (bullet_x8, bullet_y8))
                        if hit_sound_cd27 <= 0:
                            shot3_sound.play()
                            hit_sound_cd27 = 60
                        if hit_sound_cd27 > 0:
                            hit_sound_cd27 -= 1

                        bullet_rect8 = pygame.Rect(bullet_x8, bullet_y8, 10, 5)

                        if bullet_rect8.colliderect(player_rect):
                            if level == "easy":
                                hp -= 20
                            else:
                              hp -= 25
                            bullet_active8 = False
                        if npc7_x_l2 > player_x:
                            if bullet_x8 < player_x - 90:
                                bullet_active8 = False
                        if bullet_x8 > 1500:
                            bullet_active8 = False
            if npc_fighters:
                for npc in npc_list_in_game9[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0



                    if npc.state == "dead":
                        npc9_max += 1
                        if npc.should_remove:
                            npc_list_in_game9.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit9_sound_cd <= 0:
                            random.choice(hit_sounds).play()  # Случайный выбор звука удара
                            hit9_sound_cd = 15
                        if hit9_sound_cd > 0:
                            hit9_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 2

                    elif abs(npc.x - player_x) < 350:
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)


                for npc in npc_list_in_game8[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc8_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game8.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit8_sound_cd <= 0:
                            random.choice(hit_sounds).play()  # Случайный выбор звука удара
                            hit8_sound_cd = 15
                        if hit8_sound_cd > 0:
                            hit8_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 1.5

                    elif abs(npc.x - player_x) < 290 and player_y > 120 and door_status == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

                for npc in npc_list_in_game10[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc10_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game10.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit7_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit7_sound_cd = 15
                        if hit7_sound_cd > 0:
                            hit7_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 2

                    elif abs(npc.x - player_x) < 490 and player_y > 260 and door_status2 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

                # 5 комната
                for npc in npc_list_in_game11[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0

                    if npc.state == "dead":
                        npc11_max += 1
                        if npc.should_remove:
                            npc_list_in_game11.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit6_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit6_sound_cd = 15
                        if hit6_sound_cd > 0:
                            hit6_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 2

                    elif abs(npc.x - player_x) < 350 and player_y < 260 and player_y > 120 and door_status5 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen) #

                # 6 room
                for npc in npc_list_in_game12[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc12_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game12.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit5_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit5_sound_cd = 15
                        if hit5_sound_cd > 0:
                            hit5_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 2.25

                    elif abs(npc.x - player_x) < 390 and player_y < 260 and player_y > 120 and door_status4 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

                # 5 room
                for npc in npc_list_in_game13[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc13_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game13.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit4_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit4_sound_cd = 15
                        if hit4_sound_cd > 0:
                            hit4_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 1.5

                    elif abs(npc.x - player_x) < 490 and player_y < 260 and player_y > 120:
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

                # 7 room
                for npc in npc_list_in_game14[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC

                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0

                    if npc.state == "dead":
                        npc14_max += 1
                        if npc.should_remove:
                            npc_list_in_game14.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit3_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit3_sound_cd = 15
                        if hit3_sound_cd > 0:
                            hit3_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 1.75

                    elif abs(npc.x - player_x) < 250 and player_y < 260 and player_y > 120 and door_status3 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)


                for npc in npc_list_in_game15[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc15_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game15.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit_sound_cd = 15
                        if hit_sound_cd > 0:
                            hit_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 2.5
                            if hit_sound_cd22 <= 0:
                                random.choice(hit_sounds2).play()  # Случайный выбор звука удара
                                hit_sound_cd22 = 15
                            if hit_sound_cd22 > 0:
                                hit_sound_cd22 -= 1

                    elif abs(npc.x - player_x) < 290 and player_y < 120 and door_status6 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

                for npc in npc_list_in_game16[:]:
                    npc.update()
                    # Создаем Rect для текущего NPC


                    # Проверка столкновения с пулями
                    for bullet in player_bullets[:]:
                        bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 15, 3)
                        if bullet_rect.colliderect(npc.rect):
                            npc.hp -= 50
                            player_bullets.remove(bullet)

                    # Логика состояний NPC
                    if npc.hp <= 0 and npc.state != "dead":
                        npc.state = "dead"
                        npc.death_timer = 0
                        npc16_max += 1

                    if npc.state == "dead":
                        if npc.should_remove:
                            npc_list_in_game16.remove(npc)
                        else:
                            npc.draw(screen)
                        continue

                    # Определение поведения
                    if player_rect.colliderect(npc.rect):
                        npc.state = "attack"
                        if hit2_sound_cd <= 0:
                          random.choice(hit_sounds).play()
                          hit2_sound_cd = 15
                        if hit2_sound_cd > 0:
                            hit2_sound_cd -= 1
                        if keys[pygame.K_f]:
                            is_attaking = True
                            npc.hp -= 1.5
                            if hit_sound_cd23 <= 0:
                                random.choice(hit_sounds2).play()  # Случайный выбор звука удара
                                hit_sound_cd23 = 15
                            if hit_sound_cd23 > 0:
                                hit_sound_cd23 -= 1

                    elif abs(npc.x - player_x) < 490 and player_y < 120 and door_status6 == "open":
                        npc.state = "run"
                    else:
                        npc.state = "idle"

                    npc.draw(screen)

            if boss and boss_alive:
                if boss_x > player_x - 10:
                    boss_rect = pygame.Rect(
                        boss_x - 15,  # Расширяем зону атаки
                        boss_y - 5,
                        boss_attack_left[0].get_width() + 20,
                        boss_attack_left[0].get_height() + 10
                    )
                else:
                    boss_rect = pygame.Rect(
                        boss_x + 15,  # Расширяем зону атаки
                        boss_y - 5,
                        boss_attack_left[0].get_width() + 20,
                        boss_attack_left[0].get_height() + 10
                    )

                player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

                if boss_attacking:
                    if hit_sound_cd10 <= 0:
                        random.choice(hit_sounds).play()  # Случайный выбор звука удара
                        hit_sound_cd10 = 45
                    if hit_sound_cd10 > 0:
                        hit_sound_cd10 -= 1
                    # Проигрываем анимацию атаки
                    boss_anim_count += 1
                    boss_attack_frame = boss_anim_count // (boss_attack_duration // 4)

                    # Определяем направление атаки
                    if player_x < boss_x:
                        screen.blit(boss_attack_left[boss_attack_frame % 4], (boss_x, boss_y))
                    else:
                        screen.blit(boss_attack[boss_attack_frame % 4], (boss_x, boss_y))

                    # Наносим урон в середине анимации
                    if boss_anim_count == boss_attack_duration // 6 and boss_rect.colliderect(player_rect):
                        hp -= 35



                    if boss_anim_count >= boss_attack_duration:
                        boss_attacking = False
                        boss_attack_cooldown = BOSS_ATTACK_COOLDOWN

                else:
                    # Обычное состояние
                    if not granade_boom:
                        if player_x < boss_x:
                            screen.blit(boss_idle_left[0], (boss_x, boss_y))
                        else:
                            screen.blit(boss_idle[0], (boss_x, boss_y))

                    # Проверка возможности атаки
                    if boss_attack_cooldown <= 0:
                        # Проверяем дистанцию до игрока
                        distance_to_player = abs(player_x - boss_x)
                        if distance_to_player < BOSS_ATTACK_RANGE and boss_rect.colliderect(player_rect):
                            boss_attacking = True
                            boss_anim_count = 0
                    else:
                        boss_attack_cooldown -= 1
                    granade_rect = pygame.Rect(granade_x, granade_y,
                                               granade.get_width(),
                                               granade.get_height())
                    if player_y < 130 and door_status6 == "open":
                        boss_text = font.render(f"Здоровье БОССА: {boss_hp}", True, (255, 1, 1))
                        screen.blit(boss_text, (610, 560))
                        healer_cd += 1
                        if healer_cd >= 500:
                          if start_healer2:
                            start_healer2.update()
                            start_healer2.draw(screen)


                            if player_rect.colliderect(start_healer2.rect):
                                hp = min(hp + 50, MAX_HP)
                                start_healer2 = None  # Удаляем аптечку после подбора
                                pickup_sound.play()
                                healer_cd = 0
                        if not granade_go and not boss_attacking:

                            granade_reload += 1
                            if granade_reload >= 105:
                                granade_go = True
                                granade_up = True
                                granade_down = False
                                granade_lie = False
                                granade_boom = False
                                granade_up_max = 0
                                granade_down_max = 0
                                granade_lie_max = 0
                                granade_boom_max = 0
                                granade_reload = 0
                                granade_x = boss_x - 5
                                granade_y =  boss_y + 18

                                boom_frame = 0
                                boom_animation_speed = 0.04  # Скорость анимации (меньше = быстрее)
                                boom_animation_counter = 0
                                is_playing_boom_animation = False



                    if granade_go:
                                screen.blit(granade, (granade_x, granade_y))

                                if granade_up:
                                    granade_up_max += 1
                                    if player_x < boss_x - 500:
                                        granade_x -= random.randint(8, 14)
                                        granade_y -= random.uniform(3.5, 6.5)
                                    elif player_x < boss_x - 300 and player_x >= boss_x - 500:
                                        granade_x -= random.randint(6, 11)
                                        granade_y -= random.uniform(2.5, 5)
                                    elif player_x < boss_x - 50 and player_x >= boss_x - 300:
                                        granade_x -= random.uniform(0.75, 4)
                                        granade_y -= random.uniform(1.25, 2.5)

                                    elif player_x > boss_x + 100:
                                        granade_x += random.randint(2, 12)
                                        granade_y -= random.uniform(3.5, 7)





                                    if granade_up_max >= 20:
                                            granade_up = False
                                            granade_down = True
                                            granade_up_max = 0

                                    # Движение вниз
                                elif granade_down:
                                    if player_x < boss_x - 500:
                                        granade_x -= random.randint(5, 16)
                                        granade_y += random.uniform(2, 5)
                                    elif player_x < boss_x - 300 and player_x >= boss_x - 500:
                                        granade_x -= random.randint(8, 10)
                                        granade_y += random.uniform(3, 6)
                                    elif player_x < boss_x - 100 and player_x >= boss_x - 300:
                                        granade_x -= random.randint(2, 5)
                                        granade_y += random.uniform(1, 5)

                                    elif player_x > boss_x + 100:
                                        granade_x += random.randint(1, 7)
                                        granade_y += random.uniform(4, 8)
                                    granade_down_max += 1

                                    if granade_y >= 160:
                                            granade_down = False
                                            granade_lie = True
                                            granade_down_max = 0

                                        # Лежание на земле
                                elif granade_lie:
                                        granade_lie_max += 1

                                        if granade_lie_max >= 40:  # 5 кадров = ~0.33 сек
                                            granade_lie = False
                                            granade_boom = True
                                            granade_lie_max = 0

                                        # Взрыв
                                elif granade_boom:
                                        if hit_sound_cd20 <= 0:
                                            random.choice(boom_sounds).play()
                                            hit_sound_cd20 = 50
                                        if hit_sound_cd20 > 0:
                                            hit_sound_cd20 -= 1
                                        if not is_playing_boom_animation:
                                            is_playing_boom_animation = True
                                            boom_frame = 0
                                            boom_animation_counter = 0

                                            # Обновление анимации
                                        boom_animation_counter += 1

                                        # Меняем кадр с учетом скорости анимации (для 15 FPS)
                                        if boom_animation_counter >= boom_animation_speed * 60:
                                            boom_frame += 1
                                            boom_animation_counter = 0

                                            # Проверка завершения анимации
                                            if boom_frame >= len(boom):
                                                boom_frame = 0
                                                is_playing_boom_animation = False
                                                granade_boom = False
                                                granade_go = False
                                                boss_run_timer = BOSS_RUN_DURATION
                                                if player_x < boss_x:
                                                    boss_run_direction = 1  # Бежим вправо
                                                elif player_x >= boss_x:
                                                    boss_run_direction = -1

                                        if boss_run_timer > 0 and abs(boss_x - player_x) < 400 and boss_x < 1210:
                                            boss_run_timer -= 1

                                            boss_x += 0.5 * boss_run_direction


                                            boss_anim_count += 1
                                            if boss_run_direction == 1:
                                                screen.blit(boss_walk[boss_anim_count // 6 % len(boss_walk)], (boss_x, boss_y))
                                            else:
                                                screen.blit(boss_walk_left[boss_anim_count // 6 % len(boss_walk_left)],
                                                            (boss_x, boss_y))

                                            # Проверка границ экрана
                                            boss_x = max(0, min(boss_x, SCREEN_WIDTH - 150 - boss_walk[0].get_width()))

                                        else:
                                        # Обычное состояние (idle)
                                            if boss_x < player_x or floor == 1 or floor == 2:
                                                screen.blit(boss_idle[0], (boss_x, boss_y))
                                            else:
                                                screen.blit(boss_idle_left[0], (boss_x, boss_y))

                                                # Вывод текущего кадра анимации
                                        current_boom_frame = boom[boom_frame]
                                        screen.blit(current_boom_frame, (granade_x - 7 - current_boom_frame.get_width() // 2,
                                                                         granade_y - 13 - current_boom_frame.get_height() // 2))

                                        if player_x < granade_x:
                                          boom_rect = pygame.Rect(granade_x - 1, granade_y,
                                                   boom[7].get_width(),
                                                   boom[7].get_height())
                                        else:
                                            boom_rect = pygame.Rect(granade_x + 1, granade_y,
                                                                    boom[7].get_width(),
                                                                    boom[7].get_height())
                                        if boom_rect.colliderect(player_rect):
                                            if hard == "hard":
                                                hp -= 0.4
                                            elif hard == "easy":
                                                hp -= 0.2

                                            else:
                                              hp -= 0.3
                                        # Вернуть гранату в начальную позицию здесь
                if boss_hp <= 0 and boss_alive:
                    is_playing_death_animation = True
                    boss_death_frame = 0
                    boss_alive = False  # Отключаем обычное поведение сразу
                    # Отключаем все атаки и гранаты
                    boss_attacking = False
                    granade_go = False
                    # Сбрасываем все таймеры
                    boss_attack_cooldown = 0
                    boss_run_timer = 0
            elif is_playing_death_animation:
                if player_x < boss_x:  # Игрок слева от босса
                    current_death_animation = boss_dead_left
                else:
                    current_death_animation = boss_dead

                boss_death_frame += 1
                if boss_death_frame >= len(current_death_animation) * 20:  # 5 кадров на каждый спрайт
                    is_playing_death_animation = False
                    boss_alive = False
                else:
                    # Вычисляем текущий кадр анимации
                    frame_index = boss_death_frame // 20
                    screen.blit(current_death_animation[frame_index], (boss_x, boss_y))

            if start_healer:
                start_healer.update()
                start_healer.draw(screen)

                if player_rect.colliderect(start_healer.rect):
                    hp = min(hp + 50, MAX_HP)
                    start_healer = None  # Удаляем аптечку после подбора
                    pickup_sound.play()
            # Инициализация NPC для уровня 2

        screen.blit(player_down, (player_x + 10, player_y + 82))
    elif gameplay and is_paused:
        resume_btn, menu_btn = draw_pause_menu(screen)

        # Обработка кликов в меню паузы
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if resume_btn.collidepoint(event.pos):
                    is_paused = False
                    button_sound.play()
                elif menu_btn.collidepoint(event.pos):
                    is_paused = False
                    gameplay = False
                    menu = True
                    hp = 300
                    hp_hard = 0
                    button_sound.play()
                    reset_game_state()



    if not menu and not game_won:


        pygame.draw.rect(screen, (100, 100, 100), pause_button)
        font = pygame.font.Font(None, 24)
        if lang == "rus":
          text_pause = font.render("Пауза", True, (255, 255, 255))
        else:
            text_pause = font.render("Pause", True, (255, 255, 255))
        screen.blit(text_pause, (pause_button.x + 10, pause_button.y + 15))

    if gameplay == False and menu == False:
            lose_sound.play()
            screen.fill('Black')
            if lang == "rus":
              lose_text = font.render("ВЫ ПРОИГРАЛИ!", True, (255, 255, 255))
            elif lang == "eng":
              lose_text = font.render("YOU LOSE!", True, (255, 255, 255))
            screen.blit(lose_text, (600, 100))
            screen.blit(restart_label, restart_label_rect)
            is_npc1_shooting_l2 = False
            is_npc2_shooting_l2 = False
            is_npc3_shooting_l2 = False
            is_npc4_shooting_l2 = False
            is_npc5_shooting_l2 = False
            is_npc7_shooting_l2 = False




            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                button_sound.play()
                gameplay = True
                hp = 350
                hp_hard = 0
                if level == 1:
                   player_x = 50 - trip / 10
                   npc_alive = 1
                   npc_health = 100
                   npc_list_in_game.clear()
                   player_y = 390
                elif level == 2:
                    player_x = 70
                    npc1_alive_l2 = 1
                    npc1_health_l2 = 100
                    npc2_alive_l2 = 1
                    npc2_health_l2 = 100
                    npc3_alive_l2 = 1
                    npc3_health_l2 = 100
                    npc4_alive_l2 = 1
                    npc4_health_l2 = 100
                    npc5_alive_l2 = 1
                    npc5_health_l2 = 100
                    npc6_alive_l2 = 1
                    npc6_health_l2 = 100
                    npc7_alive_l2 = 1
                    npc7_health_l2 = 100
                    npс8_alive_l2 = 1
                    npc8_health_l2 = 100
                    player_y = 370
                    npc_dead_cout = 0
                    npc_list_in_game9.clear()
                    npc_list_in_game8.clear()
                    npc_list_in_game10.clear()
                    npc_list_in_game11.clear()
                    npc_list_in_game12.clear()
                    npc_list_in_game13.clear()
                    npc_list_in_game14.clear()
                    npc_list_in_game15.clear()
                    npc_list_in_game16.clear()
                    npc_list_in_game16.append(NPC2(600, 100))
                    npc_list_in_game15.append(NPC2(550, 100))
                    npc_list_in_game14.append(NPC2(200, 240))
                    npc_list_in_game13.append(NPC2(1100, 240))
                    npc_list_in_game12.append(NPC2(500, 240))
                    npc_list_in_game11.append(NPC2(800, 240))
                    npc_list_in_game10.append(NPC2(1000, 380))
                    npc_list_in_game9.append(NPC2(400, 380))
                    npc_list_in_game8.append(NPC2(700, 380))
                    door_status = "close"
                    door_status2 = "close"
                    door_status3 = "close"
                    door_status4 = "close"
                    door_status5 = "close"
                    door_status6 = "close"
                    door_status7 = "close"
                    door_status8 = "close"

                    boss_alive = True
                    boss_hp = 500
                    boss_x = 750






    if player_x >= 1450:
            mouse = pygame.mouse.get_pos()
            win = True
            win_sound.play()
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Arial', 62)
            if lang == "rus":
              win_text = font.render("ТЫ ПОБЕДИЛ!", True, (255, 255, 255))
            elif lang == "eng":
                win_text = font.render("YOU WON!", True, (255, 255, 255))
            screen.blit(win_text, (500, 200))
            screen.blit(restart_label, restart_label_rect2)
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                button_sound.play()
                gameplay = True
                hp = 300

                if level == 1:
                  player_x = 50 - trip / 10
                  npc_alive = 1
                  npc_health = 100
                elif level == 2:
                    player_x = 30

                npc_list_in_game.clear()
            pygame.display.update()

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            jump_count = 13  # Начальная сила прыжка (было 2)
    else:
        if jump_count >= -13:  # Увеличиваем диапазон (было -2)
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 20  # Ослабляем делитель (было 38)
            else:
                player_y += (jump_count ** 2) / 20  # То же самое для падения

            jump_count -= 0.5  # Замедляем уменьшение (было 1)
        else:
            is_jump = False
            jump_sound = pygame.mixer.Sound(resource_path('sound/gluhoy-zvuk-padeniya-myagkogo-predmeta.mp3'))
            jump_sound.set_volume(0.4)
            jump_sound.play()
            jump_count = 13  # Сброс (было 2)

    if not menu and not is_paused:
        for healer in healers[:]:
            healer.update()
            healer.draw(screen)

            # Проверка подбора игроком
            if player_rect.colliderect(healer.rect):
                if hard == "easy" or hard == "norm":
                  hp = min(hp + 75, MAX_HP)  # Или любое другое значение лечения
                elif hard == "hard":
                    hp = min(hp + 65, MAX_HP)
                healers.remove(healer)
                # Можно добавить звук подбора

                pickup_sound.play()

                heal = True


        if heal_text_duration < 160 and heal:
                  if hard == "hard":
                      healer_text = font.render("+ 65 HP!", True, (255, 1, 1))
                  else:
                    healer_text = font.render("+ 75 HP!", True, (255, 1, 1))
                  screen.blit(healer_text, (245, 490))
                  heal_text_duration += 1
        else:
                heal = False
                heal_rext_duration = 0




        # В главном цикле обновляем и рисуем эффекты
    for effect in pickup_effects[:]:
            effect.update()
            effect.draw(screen)
            if effect.timer <= 0:
                pickup_effects.remove(effect)





    if player_anim_count == 9:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if npc1_x_move == 1:
        if npc1_x > 1000:
            npc1_x -= 4

    if not menu:
      if lang == "eng":
        hp_text = font.render(f"HP: {round_hp}", True, (255, 255, 255))
      elif lang == "rus":
        hp_text = font.render(f"ЗДОРОВЬЕ: {round_hp}", True, (255, 255, 255))
      screen.blit(hp_text, (40, 490))

    else:

        if lang == "rus":
            screen.blit(lang_label_eng, (lang_label_rect_eng))
            screen.blit(eng, (1280, 52))


        elif lang == 'eng':
            screen.blit(lang_label_rus, (lang_label_rect_rus))
            screen.blit(rus, (1280, 52))

    if lang == "rus":
        restart_label = label.render('Начать сначала', True, (6, 128, 16))
        level1_label = label.render('Уровень 1', True, (254, 254, 254))
        level2_label = label.render('Уровень 2', True, (254, 254, 254))
        boss_text = font.render(f"Здоровье БОССА: {boss_hp}", True, (255, 1, 1))
    elif lang == "eng":
        restart_label = label.render('Try again!', True, (6, 128, 16))
        level1_label = label.render('Level 1', True, (254, 254, 254))
        level2_label = label.render('Level 2', True, (254, 254, 254))
        boss_text = font.render(f"BOSS HP: {boss_hp}", True, (255, 1, 1))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if exit_button.collidepoint(event.pos):
                event.type = pygame.QUIT

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause_button.collidepoint(event.pos):
                is_paused = not is_paused
                button_sound.play()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu:  # Если нажата ЛКМ
            if lang == "rus":
              if eng_rect.collidepoint(event.pos) or lang_label_rect_eng.collidepoint(event.pos):
                  button_sound.play()
                  lang = "eng"
            elif lang == "eng":
              if rus_rect.collidepoint(event.pos) or lang_label_rect_rus.collidepoint(event.pos):
                  button_sound.play()
                  lang = "rus"

            if setting_rect.collidepoint(event.pos) and not show_setting:
                show_setting = True
                button_sound.play()
            elif setting_rect.collidepoint(event.pos) and show_setting:
                show_setting = False
                button_sound.play()

            if show_setting:
                if setting1_rect.collidepoint(event.pos):
                    hard = "easy"
                    button_sound.play()
                    show_setting = False
                elif setting2_rect.collidepoint(event.pos):
                    hard = "norm"
                    button_sound.play()
                    show_setting = False
                elif setting3_rect.collidepoint(event.pos):
                    hard = "hard"
                    show_setting = False
                    button_sound.play()

            if hp_hard < 1:
                if hard == "easy":
                    hp = 400
                    hp_hard += 1
                elif hard == "hard":
                    hp_hard += 1
                    hp = 300




        if len(npc_list_in_game16) < 1 and npc16_max < 1 and level == 2:
            npc_list_in_game16.append(NPC2(600, 100))

        if len(npc_list_in_game16) < 1 and level == 1 and player_x >= 250:
            npc_list_in_game16.append(NPC2(0, 380))

        if len(npc_list_in_game15) < 1 and npc15_max < 1 and level == 2:
            npc_list_in_game15.append(NPC2(550, 100))

        if len(npc_list_in_game14) < 1 and npc14_max < 1 and level == 2:
            npc_list_in_game14.append(NPC2(200, 240))

        if len(npc_list_in_game13) < 1 and npc13_max < 1 and level == 2:
          npc_list_in_game13.append(NPC2(1100, 240))

        if len(npc_list_in_game12) < 1 and npc12_max < 1 and level == 2:
          npc_list_in_game12.append(NPC2(500, 240))

        if len(npc_list_in_game11) < 1 and npc11_max < 1 and level == 2:
          npc_list_in_game11.append(NPC2(800, 240))

        if len(npc_list_in_game10) < 1 and npc9_max < 1 and level == 2:
          npc_list_in_game10.append(NPC2(1000, 380))

        if len(npc_list_in_game9) < 1 and npc9_max < 1 and level == 2:
          npc_list_in_game9.append(NPC2(400, 380))

        if len(npc_list_in_game8) < 1 and npc8_max < 1 and level == 2:
          npc_list_in_game8.append(NPC2(700, 380))
        if event.type == npc_timer and not menu:

            if len(npc_list_in_game) < 3:
                if player_x < 1000:
                  npc_list_in_game.append(NPC2(1400, 390))

                else:
                  npc_list_in_game.append(NPC2(1000, 390))


    clock.tick(60)