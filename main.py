import pygame as pg
import sys
import objetos
import random
from pygame.locals import * 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 125, 0)
WIN_PRIMER_NIVEL = 3000 # pongo el valor de puntos para la condición de victoria
WIN_SEGUNDO_NIVEL = 7000


class Main(): # creo la clase principal
   
    clock = pg.time.Clock() # instancio el reloj
    def __init__(self, w, h):
        self.pantalla = pg.display.set_mode((w, h)) # creo la pantalla
        self.portadon = pg.image.load("./resources/images/portada.jpg") # cargo la imagen background de la portada
        self.espacio = pg.image.load("./resources/images/espace.png") # cargo la imagen background
        self.titulo_juego = pg.font.Font('./resources/fonts/LexendZetta-Regular.ttf', 50) # cargo una fuente para el titulo
        self.pulsa_espacio = pg.font.Font('./resources/fonts/Modak-Regular.ttf', 30) # cargo una fuente para pulsar espacio
        self.instrucciones = pg.font.Font('./resources/fonts/LexendZetta-Regular.ttf', 20) # cargo una fuente para las instrucciones
        self.numeros = pg.font.Font('./resources/fonts/DancingScript-Bold.ttf', 35) # cargo fuente para la puntuacion
        self.gameOver = pg.font.Font('./resources/fonts/Modak-Regular.ttf', 100)
        self.status = 'Portada' # inicializo el nivel por el que empieza
        
        self.text_inicial = self.titulo_juego.render("THE QUEST", False, WHITE, DARK_GREEN) # fuente texto inicial
        self.text_espacio = self.pulsa_espacio.render("Pulsar tecla <ESPACIO> para continuar", False, BLACK) #fuente texto pulsar
        self.text_aterrizar = self.pulsa_espacio.render("Coloque la nave en el centro para aterrizar", False, WHITE)
        self.text_instrucciones = self.instrucciones.render("La búsqueda comienza en un planeta tierra", False, WHITE, BLACK)
        self.text_instrucciones_1 = self.instrucciones.render("moribundo por el cambio climático.", False, WHITE, BLACK)
        self.text_instrucciones_2 = self.instrucciones.render("Partiremos a la búsqueda de un planeta", False, WHITE, BLACK)
        self.text_instrucciones_3 = self.instrucciones.render("compatible con la vida humana para colonizarlo", False, WHITE, BLACK)
        self.text_enhorabuena = self.titulo_juego.render("ENHORABUENA JUEGO COMPLETADO", False, WHITE)
        pg.display.set_caption("THE QUEST") # le pongo nombre a la ventana
        
        self.nave = objetos.Nave(800, 600) # creo la nave

        self.asteroid0 = objetos.AsteroidSilver() # creo los asteroides
        self.asteroid1 = objetos.AsteroidSilver()
        self.asteroid2 = objetos.AsteroidSilver()
        self.asteroid3 = objetos.AsteroidSilver()
        self.asteroid4 = objetos.AsteroidSilver()
        self.asteroid5 = objetos.AsteroidSilver()

        self.asteroidGold0 = objetos.AsteroidGold()
        self.asteroidGold1 = objetos.AsteroidGold()

        self.escritura = objetos.Alias_records("")
        self.escritura.pos((337, 315))


        self.planeta = objetos.Planeta() # creo el planeta
        self.planeta1 = objetos.Planeta_Final()

        self.asteroidNivel1 = pg.sprite.Group() # creo un grupo de asteroides para añadirlo en el nivel 1
        self.asteroidNivel1.add(self.asteroid0)
        self.asteroidNivel1.add(self.asteroid1)
        self.asteroidNivel1.add(self.asteroid2)
        self.asteroidNivel1.add(self.asteroidGold0)
        self.asteroidsGroup = pg.sprite.Group() # creo un grupo de asteroides para el nivel 2
        self.asteroidsGroup.add(self.asteroid0) # añado los asteroides al grupo
        self.asteroidsGroup.add(self.asteroid1)
        self.asteroidsGroup.add(self.asteroid2)
        self.asteroidsGroup.add(self.asteroid3)
        self.asteroidsGroup.add(self.asteroid4)
        self.asteroidsGroup.add(self.asteroid5)
        self.asteroidsGroup.add(self.asteroidGold0)
        self.asteroidsGroup.add(self.asteroidGold1)


        #self.puntuacion = self.instrucciones.render(str(self.score), True, WHITE) # creo la puntuación y la cargo con la fuente
        self.score = 0


    def portada_principal(self): # Creo la primera pantalla
        portada = False  
        self.status = 'Portada'
          
        while not portada:
            for events in pg.event.get():
                if events.type == pg.KEYDOWN:
                    if events.key == pg.K_SPACE:
                        portada = True
                        self.status = 'Nivel'

            
            self.pantalla.blit(self.portadon, (0, 0))
            self.pantalla.blit(self.text_inicial, (200, 100))
            self.pantalla.blit(self.text_espacio, (120, 450))
            self.pantalla.blit(self.text_instrucciones, (15, 220))
            self.pantalla.blit(self.text_instrucciones_1, (15, 250))
            self.pantalla.blit(self.text_instrucciones_2, (15, 280))
            self.pantalla.blit(self.text_instrucciones_3, (15, 310))

            pg.display.flip()
            #self.clock.tick(30)

        
        self.status = 'Nivel'

    def handlenEvent(self): # creo los eventos de teclado
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                return self.quit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.nave.vy  = -5
                elif event.key == pg.K_DOWN:
                    self.nave.vy  = 5





        key_pressed = pg.key.get_pressed() # Aumenta la velocidad con tecla pulsada
        if key_pressed[pg.K_UP]:
            self.nave.vy -= 1
                
        elif key_pressed[pg.K_DOWN]:
            self.nave.vy += 1
        else:
            self.nave.vy = 0

        return False

          
    def primer_nivel(self): # Creo la partida de juego
        Primer = False 
        p = 0
        self.puntuacion = self.numeros.render(str(self.score), True, WHITE)
        self.status = 'Nivel'

        while not Primer:
            Primer = self.handlenEvent()
            if self.nave.estado is True:
                Primer = True
                self.status = 'Final'

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Primer = True
                    self.quit()
            
            self.nave.update(800, 600)
            self.nave.rotate()
            self.nave.boom()
            
            self.asteroidNivel1.update(800, 600)
            self.nave.estrellado(self.asteroidsGroup)




            #self.nave.aterrizado(self.allsprite)
            
            # puntos al pasar la pantalla

            if self.asteroid0.rect.centerx <= 0 or self.asteroid1.rect.centerx <= 0 or self.asteroid2.rect.centerx <= 0:
                self.score += 20
                self.puntuacion = self.numeros.render(str(self.score), True, WHITE)
            elif self.asteroidGold0.rect.centerx <= 0:
                self.score += 40
                self.puntuacion = self.numeros.render(str(self.score), True, WHITE)
            else:
                self.score = int(self.score)

                if self.nave.estado == True:
                    Primer = False
                    self.status = 'Nivel_2'

                if self.score >= WIN_PRIMER_NIVEL:
                    self.planeta.update(800, 600)
                    self.nave.rotando = True
                    if self.planeta.rect.centerx <= 800 and self.nave.angle % 180 <= 0:
                        self.nave.rotando = False
                        self.nave.rect.centerx += self.nave.vx
                        if self.nave.rect.centery > 300:                            
                            self.nave.rect.centery -= self.nave.vx
                        elif self.nave.rect.centery < 300:
                            self.nave.rect.centery += self.nave.vx
                        else:
                            pass

                    if self.asteroid0.rect.centerx >= 1200 or self.asteroid1.rect.centerx >= 1200 or self.asteroid2.rect.centerx >= 1200 or self.asteroidGold0.rect.centerx >= 1200:
                        pg.sprite.Group.empty(self.asteroidNivel1)
                        


                    if self.nave.rect.centerx >= 570:
                        self.score += 1000
                        Primer = True
                        self.status = 'Nivel_2'
                    

                        

            p -= 0.5
            if p <= -3000:
                p = 0

            
            self.pantalla.blit(self.espacio, (p, 0))   
            self.pantalla.blit(self.espacio, (p+3000, 0))
            self.pantalla.blit(self.nave.image, self.nave.rect)
            self.pantalla.blit(self.planeta.image, (self.planeta.rect))
            self.asteroidNivel1.draw(self.pantalla)
            self.pantalla.blit(self.puntuacion, (700, 30))
            

            pg.display.flip()
            self.clock.tick(30)




    def segundo_nivel(self):
        Segundo = False
        p = 0
        self.puntuacion = self.numeros.render(str(self.score), True, WHITE)
        self.status = 'Nivel_2'
        self.nave.rotando = True
        while not Segundo:
            Segundo = self.handlenEvent()
            if self.nave.estado is True:
                Primer = True
                self.status = 'Final'

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Segundo = True
                    self.quit()


            self.nave.update(800, 600)
            self.nave.rotate()
            self.nave.boom()

            if self.nave.rect.centerx == 570 and self.nave.angle % 180 >= 0:
                self.nave.rotando = False
                self.nave.vx -= 1

            if self.nave.rect.centerx <= 40:
                self.nave.vx = 0
                self.planeta.despegue(800, 600)
                self.asteroidsGroup.update(800, 600)

                if self.asteroid0.rect.centerx == 1200 or self.asteroid1.rect.centerx == 1200 or self.asteroid2.rect.centerx == 1200 or self.asteroid3.rect.centerx == 1200 or self.asteroid4.rect.centerx == 1200 or self.asteroid5.rect.centerx == 1200:
                    self.score += 40
                    self.puntuacion = self.numeros.render(str(self.score), True, WHITE)
                elif self.asteroidGold0.rect.centerx == 1200 or self.asteroidGold1.rect.centerx == 1200:
                    self.score += 60
                    self.puntuacion = self.numeros.render(str(self.score), True, WHITE)

            if self.score >= WIN_SEGUNDO_NIVEL:
                self.planeta1.update(800, 600)
                self.nave.rotando = True
                if self.asteroid0.rect.centerx <= 0 or self.asteroid1.rect.centerx <=0 or self.asteroid2.rect.centerx <=0 or self.asteroid3.rect.centerx <=0 or self.asteroid4.rect.centerx <=0 or self.asteroid5.rect.centerx <=0 or self.asteroidGold0.rect.centerx <=0 or self.asteroidGold1.rect.centerx <=0:
                    pg.sprite.Group.empty(self.asteroidsGroup)
            if self.planeta1.rect.centerx == 800 and self.nave.angle % 180 <= 0:
                self.nave.rotando = False
                self.nave.vx = 1

                if self.nave.rect.centery > 300:
                    self.nave.rect.centery -= self.nave.vx
                elif self.nave.rect.centery < 300:
                    self.nave.rect.centery += self.nave.vx
            
                if self.planeta1.rect.centerx == 800 and self.nave.rect.centerx >= 570:
                    Segundo = True
                    self.status = 'Final'                    



            p -= 0.5
            if p <= -3000:
                p = 0

            
            self.pantalla.blit(self.espacio, (p, 0))   
            self.pantalla.blit(self.espacio, (p+3000, 0))
            self.pantalla.blit(self.nave.image, self.nave.rect)
            self.pantalla.blit(self.planeta.image, (self.planeta.rect))
            self.pantalla.blit(self.planeta1.image, (self.planeta1.rect))
            self.asteroidsGroup.draw(self.pantalla)
            self.pantalla.blit(self.puntuacion, (700, 30))
            pg.display.flip()
            self.clock.tick(30)
        
        
        
        
        self.status = 'Final'

    def game_final(self):
        self.status = 'Final'
        game_over = False
        while not game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return self.quit()
                if event.type == KEYDOWN:
                    if event.unicode in "abcdefghijklmnñopqrstuvwyz" and len(self.escritura.caracteres) <= 5:
                        self.escritura.caracteres += event.unicode
                        self.escritura.valor += 1
                    elif event.key == pg.K_BACKSPACE:
                        self.escritura.caracteres = self.escritura.caracteres[:-1]
                        self.escritura.valor -= 1
                        if self.escritura.valor < 0:
                            self.escritura.valor = 0





            game_over = self.handlenEvent()
            self.acabado = self.gameOver.render("GAME OVER", False, (255, 0, 0))
            self.intro = self.pulsa_espacio.render("Pulsa <INTRO> para continuar", False, (BLACK))
            self.text_alias = self.pulsa_espacio.render("Escribe tu alias", False, (BLACK))
            self.text_puntuacion = self.pulsa_espacio.render("Tu puntuación :", False, (BLACK))
            self.puntuacion = self.numeros.render(str(self.score), True, WHITE)

            self.pantalla.fill(DARK_GREEN)

            self.pantalla.blit(self.acabado, (125, 50))
            self.pantalla.blit(self.text_alias, (305, 275))
            self.pantalla.blit(self.text_puntuacion, (140, 350))
            self.pantalla.blit(self.puntuacion, (400, 350))
            self.pantalla.blit(self.intro, (200, 500))
            text = self.escritura.render()
            pg.draw.rect(self.pantalla, (WHITE), text[0])
            self.pantalla.blit(text[1], self.escritura.pos())
            


            pg.display.flip()


    def main_loop(self):
        while True:
            if self.status == 'Portada':
                self.portada_principal()
            if self.status == 'Nivel':
                self.primer_nivel()
            if self.status == 'Nivel_2':
                self.segundo_nivel()
            if self.status == 'ganaste':
                self.congratulation()
            if self.status == 'Final':
                self.game_final()

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init(), 
    game = Main(800, 600)
    game.main_loop()
    game.quit()
