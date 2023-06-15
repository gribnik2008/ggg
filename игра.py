import arcade ##библиотека аркейд
import random
SCREEN_WIDTH = 1200 ##ширина окна
SCREEN_HEIGHT = 720 ##высота окна
SCREEN_TITLE = "игра" ##название окна
class Ball (arcade.Sprite):
    def update (self): ##задаёт логику мяча ии как он должен двигатся
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.top >=SCREEN_HEIGHT or self.bottom <=0:
            self.change_y = -self.change_y
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
class Bar (arcade.Sprite): ## задаёт логику платформы и её движения
    def update (self):
        self.center_x += self.change_x 
        if self.left <= 0:
            self.left = 0
        if self.right >= 1200:
            self.right = 1200

class Main_game (arcade.Window): ##основной класс, в него добавляются переменные
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball2.png", 0.1)
        self.bar = Bar("bar.png", 0.1)
        self.setup ()
        self.score = 0
        self.game = False
        self.attempts = 5
    def setup (self): 
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT-200
        direction = random.randint (1, 2)
        if direction == 2:
            self.ball.change_x = -5
        else:
            self.ball.change_x = 5
        self.ball.change_x = random.randint (-5, 5)
        self.ball.change_y = 5
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 2
        self.bar.change_x = 0
    def on_key_press (self, key, modifiers): ## этот метод для нажатия на клавиши
        if self.game == False:
            if key == arcade.key.A:
                self.bar.change_x = -10
            if key == arcade.key.D:
                self.bar.change_x = 10
    def on_key_release (self, key, modifiers): ## этот метод для оптускания клавиш
        if key == arcade.key.A or key == arcade.key.D:
            self.bar.change_x = 0

    def on_draw (self): ## МЕТОД отрисовывает бгшники, спрайты и тексты
        self.clear ((115, 13, 50))
        self.ball.draw ()
        self.bar.draw ()
        arcade.draw_text(f"количество очков {self.score}", 10, 20, (175, 99, 42), 40, font_name="RDR Lino")
        arcade.draw_text(f"количество попыток {self.attempts}", 650, 20, (175, 99, 42), 40, font_name="RDR Lino")
        if self.attempts==0:
            arcade.draw_text("ты проиграл", 600, 300, (15, 99, 42), 40, font_name="RDR Lino")
        if self.score==15:
            arcade.draw_text("ты выиграл", 600, 300, (15, 99, 42), 40, font_name="RDR Lino")
            
        
    def update (self, delta_time): ##задаёт логику у игры
        self.ball.update ()
        self.bar.update ()
        if arcade.check_for_collision (self.ball, self.bar): ##условия если они касаются
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1
            if self.ball.change_x > 0:
                self.ball.change_x += 2
            if self.ball.change_x < 800:
                self.ball.change_x -= 2
        if self.ball.bottom <= 0:
            self.attempts -= 1
            self.ball.center_y = 300
            self.ball.center_x = 400
        if self.attempts == 0:
            self.bar.stop ()
            self.ball.stop ()
            self.game = True
        if self.score == 15:
            self.ball.stop ()
            self.game = True

window = Main_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) 
arcade.run () ## он заставляет окно нормально работать до тех пор, пока мы его сами не закроем
    
