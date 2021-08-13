import arcade

# the width and the heigth of the window

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600 
SCREEN_TITLE = "DinoGame"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background=arcade.load_texture("desert.png")
        self.dino=Dino(0.5)
        self.dino.textures=[arcade.load_texture("dino1.png"),arcade.load_texture("dino2.png"),arcade.load_texture("dino3.png")]
        self.cactus=Cactus("cactus2.png",0.5)
        self.score=0
        self.level=1
        self.lives=3
        # adding background 
    
    def setup(self):
        self.dino.center_x=100
        self.dino.center_y=200
        self.cactus.center_x=SCREEN_WIDTH
        self.cactus.center_y=200
        self.cactus.change_x=3
        


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        arcade.draw_text(f"Score: {self.score}",350,550,arcade.color.BLACK)
        arcade.draw_text(f"Lives: {self.lives}",450,550,arcade.color.BLACK)
        arcade.draw_text(f"Level: {self.level}",550,550,arcade.color.BLACK)
        self.dino.draw()
        self.cactus.draw()
        if (self.score==30):
            arcade.draw_text("You Win!",300,300,arcade.color.RED_DEVIL, 60)
            self.setup()
            self.dino.stop()
            self.cactus.stop()
    
    def update(self, delta_time):
        self.dino.update()
        self.dino.update_animation()
        self.cactus.update()
        if arcade.check_for_collision(self.dino,self.cactus):
            self.lives-=1
            self.setup()
        if self.lives==0:
            self.dino.stop()
            self.cactus.stop()
            self.score==0
            self.level==1
        if self.cactus.center_x<1:
            self.score+=1
        if self.score==5:
            self.level = 2
        elif self.score==10:
            self.level = 3       
        elif self.score==15:
            self.level = 4
        elif self.score==20:
            self.level = 5
        elif self.score==25:
            self.level = 6
        

               

    def on_key_press(self, key, modifiers):
        if key==arcade.key.SPACE and self.dino.center_y<=200:
            self.dino.change_y=15
        

class Cactus(arcade.Sprite):
    def update(self):
        self.center_x-=self.change_x
        if self.center_x<0:
            self.center_x=SCREEN_WIDTH
            
        

class Dino(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y+=self.change_y
        self.change_y -= 0.5
        if self.center_y<200:
            self.center_y=200

    
game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
