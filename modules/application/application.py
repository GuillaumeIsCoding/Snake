from modules.application.window.window_build import WindowBuild
from modules.application.surfaces.surface_manager import SurfaceManager
from modules.objects.object import Object


from pygame import display,time, event, USEREVENT,KEYDOWN,K_w,K_a,K_d,K_s, K_SPACE,K_ESCAPE, Color
from pygame_gui import UI_BUTTON_PRESSED
from random import randint

import time as temps

class Application():
    #
    clock = time.Clock()
    #
    is_gui_running = True
    #
    first_object = True
    #
    gameplay = {
        "heading_x"     :   -1,
        "heading_y"     :    0,
        "difficulty"    :    1,
        "score"         :    0, 
    }
    # 
    game ={
        "pause"             :   False,
        "first_object"      :   True,
        "is_gui_running"    :   True
    }
    #
    body_part = []
    # 
    apple = []


    def __init__(self) -> None:
        
        """
        
        """

        start = temps.time()    # Ne fait pas partie du code
        #
        self.applicationSurface, self.width, self.height = WindowBuild().__build__()

        end = temps.time()      # Ne fait pas partie du code
        
        print(end - start)      # Ne fait pas partie du code
        
        #
        self.Surface_Init()
        #
        self.Surface_Init_Color()
    
    def __app__(self) -> None:
        
        """
        
        """

        while self.game["is_gui_running"] != False:
            #
            self.dT = self.clock.tick_busy_loop(9)/1000.0          # pour difficulter changer le busy loop
                                                                   # self.gameplay["difficulty"]
            # Fill up the map 
            self.game_surface.fill(Color(255,255,255))
            # Game here 
            self.__Game__()
            # Event here 
            self.__Events__()
            # Update here     
                # Update frames here
            self.Upddate_Frame() 
                # Update gui here - - -
            display.update()
        #
        print(self.gameplay)
    def __Events__(self) -> None:
        
        """
        
        """

        self.colision_listener()

        for self.event in event.get():
        
            if self.event.type == USEREVENT:

                if self.event.user_type == UI_BUTTON_PRESSED:
                    # 
                    pass

            if self.event.type == KEYDOWN:

                if self.game["pause"] == False:
                
                    if self.event.key == K_w:
                        # 
                        self.gameplay["heading_x"], self.gameplay["heading_y"] = 0, -1

                    if self.event.key == K_s:
                        # 
                        self.gameplay["heading_x"], self.gameplay["heading_y"] = 0, 1

                    if self.event.key == K_a:
                        # 
                        self.gameplay["heading_x"], self.gameplay["heading_y"] = -1, 0

                    if self.event.key == K_d:
                        # 
                        self.gameplay["heading_x"], self.gameplay["heading_y"] = 1, 0

                if self.event.key == K_SPACE:
                    # lorsque la touche est cliqué met la partie sur pause 
                    
                    if self.game["pause"] == False:
                        
                        self.game["pause"] = True
                    
                    elif self.game["pause"] == True:

                        self.game["pause"] = False

                if self.event.key == K_ESCAPE:
                    # This function close the game when "Esc" key is pressed
                    self.game["is_gui_running"] = False
            
        if self.game["pause"]   == False:
            #
            self.move_snake()        
                
            
            
    
    # ================================================================================================================================================= #
    #                                                                     Frames                                              
    # ================================================================================================================================================= #
    
    def Surface_Init(self) -> None:

        """
        Initialisation des surfaces de jeux, de menues et de scoreboard
        """

        # Menu part
        self.menu_surface, self.menu_surface_manager = SurfaceManager(self.width/3 - (((self.width)/3)/20 + 1)/2, self.height, "menu_surface").build_surface_manager()
        # Game part
        self.game_surface, self.game_surface_manager = SurfaceManager(self.width/3 + (((self.width)/3)/20 + 1), 800 + ((800/20)+1), "game_surface").build_surface_manager()
        # Upper part
        self.upper_game_surface, self.upper_game_surface_manager = SurfaceManager(self.width/3 + (((self.width)/3)/20 + 1), 140 - ((800/20)+1)/2, "game_upper_surface").build_surface_manager()
        # Lower part
        self.lower_game_surface, self.lower_game_surface_manager = SurfaceManager(self.width/3 + (((self.width)/3)/20 + 1), 140 - ((800/20)+1)/2, "game_lower_surface").build_surface_manager()
        # Score part
        self.score_surface, self.score_surface_manager = SurfaceManager(self.width/3 - (((self.width)/3)/20 + 1)/2, self.height, "score_surface").build_surface_manager()
    
    def Surface_Init_Color(self) -> None:

        """
        Initialisation de la couleur des surfaces
        """

        # Menu Color 
        self.menu_surface.fill(Color(0,0,0))
        # Game Color 
        self.game_surface.fill(Color(255,255,255))
        # Upper Game Color
        self.upper_game_surface.fill(Color(0,0,0))
        # Lower Game Color
        self.lower_game_surface.fill(Color(0,0,0))
        # Score Color
        self.score_surface.fill(Color(0,0,0))
    
    def Upddate_Frame(self) -> None:

        """
        Mise à jour des surfaces
        """

        # Menu surface part
        self.menu_surface_manager.update(self.dT)
        self.applicationSurface.blit(self.menu_surface, (0,0))
        self.menu_surface_manager.draw_ui(self.applicationSurface)
        # Game surface part
        self.game_surface_manager.update(self.dT)
        self.applicationSurface.blit(self.game_surface, ((self.width)/3 - (((self.width)/3)/20 + 1)/2, 140 - ((800/20)+1)/2))
        self.game_surface_manager.draw_ui(self.applicationSurface)
        # Game upper part 
        self.upper_game_surface_manager.update(self.dT)
        self.applicationSurface.blit(self.upper_game_surface, ((self.width)/3 - (((self.width)/3)/20 + 1)/2,0))
        self.upper_game_surface_manager.draw_ui(self.applicationSurface)
        # Game lower part
        self.lower_game_surface_manager.update(self.dT)
        self.applicationSurface.blit(self.lower_game_surface, ((self.width)/3 - (((self.width)/3)/20 + 1)/2,self.height - 140 + ((800/20)+1)/2))
        self.lower_game_surface_manager.draw_ui(self.applicationSurface)
        # Score surface part
        self.score_surface_manager.update(self.dT)
        self.applicationSurface.blit(self.score_surface, ((2/3)*(self.width) + (((self.width)/3)/20 + 1)/2,0))
        self.score_surface_manager.draw_ui(self.applicationSurface)
    
    # ================================================================================================================================================= #
    #                                                                     Game                                              
    # ================================================================================================================================================= #

    def __Game__(self) -> None:

        """
        Affichage des objects
        """
        self.initialisation()

        for obj in self.body_part:

            obj.build_bloc(self.game_surface, (0,0,0))
        
        for obj in self.apple:

            obj.build_bloc(self.game_surface,(255,0,0))

    def initialisation(self) -> None:
        
        """
        Initialisation de la position du serpent et de la pomme
        """
        #
        if self.game["first_object"] == True:
            #
            self.game["first_object"] = False
            #
            ishead = True
            #
            self.gameplay["heading_x"], self.gameplay["heading_y"] = self.direction()
            for i in range(5):
                #
                if ishead == True:

                    ishead = False

                    #
                    head_x, head_y = self.random_spawn(5,27,35)

                    obj = Object(head_x , head_y, 20, 20)     # self.head_x + self.width/3 - (((self.width)/3)/20 + 1)/2, self.head_y +  140 - ((800/20)+1)/2
                
                elif ishead == False:

                    prev_obj = self.body_part[i - 1]

                    obj = Object(prev_obj.x - 21 * self.gameplay["heading_x"], prev_obj.y - 21 * self.gameplay["heading_y"], 20, 20)

                self.body_part.append(obj)
            
            apple_x, apple_y = self.random_spawn(0,29,39)

            self.apple.append(Object(apple_x,apple_y,20,20))


    def random_spawn(self,min,max_1,max_2) -> tuple[int,int]:
        
        """
        Retourne un spawn aléatoire dépendament des paramètres utilisé lors de l'exécution de la fonction
        """

        n1 = randint(min,max_1)
        n2 = randint(min,max_2)
        
        return ((20 * n1) + n1 * 1 + 1), ((20 * n2) + n2 * 1 + 1)

# ================================================================================================================================================= #
#                                                                     Logique de jeu                                              
# ================================================================================================================================================= #
    
    def move_snake(self) -> None:

        """
        Déplacement du serpent 
        """

        # nombre de partie que le serpent a
        indice = len(self.body_part) - 1 

        # déplaçons le serpent de la fin au début
        while indice > 0:
            # prend la position avant de la partie [indice - 1] pour la donner a [indice]
            self.body_part[indice].x, self.body_part[indice].y = self.body_part[indice - 1].x, self.body_part[indice - 1].y
        
            indice = indice - 1
        # déplace la tete indépendament du reste du corps        
        self.body_part[0].x, self.body_part[0].y = self.body_part[0].x + 21 * self.gameplay["heading_x"], self.body_part[0].y + 21 * self.gameplay["heading_y"]
    
    def difficulty(self) -> None:

        """
        À un certain nombre de point la difficulté augmente
        """
        
        if self.gameplay["score"] % 100 == 0:

            # augmentons la difficulté
            self.gameplay["difficulty"] = self.gameplay["difficulty"] + 0.05

    def score(self) -> None:

        """
        Suit en direct le score 
        """
        
        self.gameplay["score"] = self.gameplay["score"] + 50

    def colision_listener(self) -> None:

        """
        Verifie si toute les colisions que la tete fait sont conforme au jeu
        """

        # lorsque la tete du serpent est sur la pomme 
        if (self.body_part[0].x >= self.apple[0].x and self.body_part[0].x  <= self.apple[0].x + 20) and (self.body_part[0].y >= self.apple[0].y and self.body_part[0].y <= self.apple[0].y + 20):
            # detruire la pomme 
            for obj in self.apple:
                # pop l'item dans la liste
                self.apple.pop(self.apple.index(obj))
            # prenons le dernier index du corps du serpent
            prev = self.body_part[-1]
            # spawn la pomme 
            apple_x, apple_y = self.random_spawn(0,29,39)
            # ajoutons la pomme a la liste
            self.apple.append(Object(apple_x,apple_y,20,20))
            # ajoutons une nouvelle partie au serpent
            self.body_part.append(Object(prev.x + 21 * self.gameplay["heading_x"], prev.y + 21 * self.gameplay["heading_y"], 20, 20))
            # update le score
            self.score()
            # ajoutons la difficulté
            self.difficulty()
        # lorsque la tete du serpent touche les bords du jeu
        if (self.body_part[0].x <= 0) or (self.body_part[0].x >= (self.width)/3 + (((self.width)/3)/20 + 1)) or (self.body_part[0].y <= 0) or (self.body_part[0].y >= 800 + ((800/20)+1)):
            
            self.game["is_gui_running"] = False

            print("GAME OVER")
        # analysons laposition de chaque partie du corps du serpent
        for indice in range(1,len(self.body_part)):
            # lorsque la tete du serpent touche son corps
            if (self.body_part[0].x >= self.body_part[indice].x and self.body_part[0].x  <= self.body_part[indice].x + 20) and (self.body_part[0].y >= self.body_part[indice].y and self.body_part[0].y <= self.body_part[indice].y + 20):
                
                self.game["is_gui_running"] = False

                print("GAME OVER")

                break
                
    def direction(self) -> tuple[int,int]:
        
        """
        La direction initiale du serpent lorsque une game est lancée
        """

        d = {
            "0" :  (1,0),
            "1" : (-1,0),
            "2" :  (1,0),
            "3" : (0,-1)
        }
        # retourne une direction que la tete prendra
        return d[str(randint(0,3))]

# ================================================================================================================================================= #
#                                                                     Surfaces                                            
# ================================================================================================================================================= #