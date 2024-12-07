import pygame
import random
from abc import ABC, abstractmethod
import time


max_populatie_iepuri = 5
max_populatie_arici = 5
max_populatie_vulpi = 4
ecosist_humidity=100


pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ecosistem")
FPS = 60

bg = pygame.image.load('img/map.png')


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

win_width = 712
win_height = 731

window = pygame.display.set_mode((win_width, win_height))

# Clasă abstractă Ecosistem
class Ecosistem(ABC):

    def __init__(self, nume, pozitie, energie, total_age):
        self.nume = nume
        self.total_age = total_age
        self.age_remaning = total_age
        self.energie = energie
        self.pozitie = pozitie
        self.energie_ecosistem=50
        self.erbivor_rata_supravetuire=100
        self.carnivor_rata_supravetuire=100
        self.omnivor_rata_supravetuire=100
        self.rata_supravetuire=100
        self.start_time = None
        
    @abstractmethod
    def actioneaza(self):
        pass
        
class StatusEcosistem(Ecosistem):
    def __init__(self,numar_plante,numar_animale,numar_iepuri,numar_arici,numar_vulpi):
        super().__init__(nume="Status", pozitie=(0, 0), energie=numar_plante+numar_animale, total_age=0)
        self.energie_ecosistem = numar_plante+numar_animale
        self.numar_animale = numar_animale
        self.numar_iepuri = numar_iepuri
        self.numar_arici = numar_arici
        self.numar_vulpi=numar_vulpi
        self.cantitate_plante=numar_plante


    def status(self):
        return (f"Energie totală a ecosistemului: {self.energie_ecosistem},\n"
                f"Cantitatea de plante este: {self.cantitate_plante}\n"
                f"Număr animale: {self.numar_animale}\n"
                f"Număr animale erbivore: {self.numar_iepuri}\n"
                f"Număr animale carnivore: {self.numar_vulpi}\n"
                f"Număr animale omnivore: {self.numar_arici}")

    def actioneaza(self):
       
        print(self.status()) 
        
    
    
class weather_conditions(Ecosistem):

    
    def __init__(self, nume, x, y, imagine_rain, imagine_seceta):
        super().__init__(nume, pozitie=(x, y), energie=50, total_age=5)
        self.x = x
        self.y = y
        self.state = "normal"
        self.imagine_rain = pygame.image.load(imagine_rain)
        self.imagine_seceta = pygame.image.load(imagine_seceta)
        self.image_to_show = None

    def actioneaza(self):
        pass 
    
    def weather_type(self, nume ,rata_supravetuire):

        self.imagine_rain = pygame.transform.scale(self.imagine_rain, (750, 750))
        self.imagine_seceta = pygame.transform.scale(self.imagine_seceta, (750, 750))

        
        print(f"Evaluating weather condition with rate: {rata_supravetuire}")
        if rata_supravetuire < 50 and nume=='Iepure':
            self.image_to_show = self.imagine_rain
            
            
            print("Rain image set")
            self.start_time = pygame.time.get_ticks()  # Momentul când afișăm ploaia
            # Adăugarea iepurelui
            new_rabbit = Erbivor(
                "Iepure",
                random.randint(0, win_width),
                random.randint(0, win_height),
                100,
                100,
                5,
                iepure_imagine,
            )
            animal_list.append(new_rabbit)
            self.erbivor_rata_supravetuire = 100 

        if rata_supravetuire < 50 and nume=='arici':
            self.image_to_show = self.imagine_rain
           
            print("Rain image set")
            self.start_time = pygame.time.get_ticks()  # Momentul când afișăm ploaia
            # Adăugarea iepurelui
            new_arici = Omnivor(
                "arici",
                random.randint(0, win_width),
                random.randint(0, win_height),
                100,
                100,
                5,
                omnivor_img,
            )
            animal_list.append(new_arici)
            self.omnivor_rata_supravetuire = 100 

        if rata_supravetuire < 50 and nume=='plante':
            self.image_to_show = self.imagine_seceta
           
            print("seceta image set")
            self.start_time = pygame.time.get_ticks()  # Momentul când afișăm ploaia
        if rata_supravetuire > -10 and rata_supravetuire<10 and nume=='plante':
            self.image_to_show = self.imagine_rain
           
            print("seceta image set")
            self.start_time = pygame.time.get_ticks()  # Momentul când afișăm ploai
            
                  
      
                

       


    def draw(self, window):
        if self.image_to_show is not None:
            current_time = pygame.time.get_ticks()
            if self.start_time and current_time - self.start_time > 2000:  # 5 secunde
                self.image_to_show = None
                self.start_time = None
                print("Weather image cleared after 5 seconds")
            else:
                window.blit(self.image_to_show, (self.x, self.y))



def coliziune(animal1, animal2):
    distanta = ((animal1.x - animal2.x) ** 2 + (animal1.y - animal2.y) ** 2) ** 0.5
    return distanta < 50  # Dacă distanța este mai mică de 50, se consideră colizi

# Clasa Animal ca clasa virtuală de bază
class Animal(Ecosistem):
    def __init__(self, nume, x, y, energie, total_age, speed, imagine):
        self.x = x
        self.y = y
        self.imagine = pygame.image.load(imagine)
        super().__init__(nume, (self.x, self.y), energie, total_age)
        self.speed = speed
        self.recent_reproduction_time = 0  # Ultimul moment când animalul s-a reprodus
    def actioneaza():
        for self in animal_list[:]: 
            self.deplaseaza()
            self.mananca(animal_list, plante)
            self.reproduce(animal_list, animale_noi)    

    def reproduce(self, animale, animale_noi):
        global populatie_iepuri, populatie_arici, populatie_vulpi

        current_time = pygame.time.get_ticks()
        if current_time - self.recent_reproduction_time > 5000:  # Poate reproduce la fiecare 5 secunde
            for alt_animal in animale:
                if (
                    alt_animal != self
                    and type(self) == type(alt_animal)
                    and coliziune(self, alt_animal)
                    and current_time - alt_animal.recent_reproduction_time > 5000
                ):
                    
                    if self.nume == "Iepure" and populatie_iepuri < max_populatie_iepuri:
                        print(f"Reproducere: {self.nume} și {alt_animal.nume}")
                        new_rabbit = Erbivor(
                            "Iepure",
                            random.randint(0, win_width),
                            random.randint(0, win_height),
                            100,
                            100,
                            5,
                            iepure_imagine,
                        )

                        animale_noi.append(new_rabbit)

                        populatie_iepuri += 1

                    
                    elif self.nume == "arici" and populatie_arici < max_populatie_arici:
                        print(f"Reproducere: {self.nume} și {alt_animal.nume}")
                        new_omnivor = Omnivor(
                            "arici",
                            random.randint(0, win_width),
                            random.randint(0, win_height),
                            100,
                            100,
                            5,
                            omnivor_img,
                        )
                        animale_noi.append(new_omnivor)
                        populatie_arici += 1

                    
                    elif self.nume == "vulpe" and populatie_vulpi < max_populatie_vulpi:
                        print(f"Reproducere: {self.nume} și {alt_animal.nume}")
                        new_fox = Carnivor(
                            "vulpe",
                            random.randint(0, win_width),
                            random.randint(0, win_height),
                            100,
                            100,
                            5,
                            fox_img,
                        )
                        animale_noi.append(new_fox)
                        populatie_vulpi += 1

                    self.recent_reproduction_time = current_time
                    alt_animal.recent_reproduction_time = current_time
                    break  


    def actioneaza(self):
        pass         
                


    @abstractmethod
    def tip_hrana(self):
        pass

    @abstractmethod
    def mananca(self, animale, plante):
        pass

    def deplaseaza(self):
       
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

        
        self.x = max(0, min(self.x, win_width - 20))
        self.y = max(0, min(self.y, win_height - 20))

       
        self.pozitie = (self.x, self.y)

    def status(self):
        return f"Animal {self.nume}: Energie={self.energie}, Vârstă rămasă={self.age_remaning}"

    def draw(self, window):
    
        window.blit(self.imagine, (self.x, self.y))


# Clasa Erbivor, subclasă a clasei Animal
class Erbivor(Animal):

    

    def __init__(self, nume, x, y, energie, total_age, speed, imagine):
        super().__init__(nume, x, y, energie, total_age, speed, imagine)

    def tip_hrana(self):
        return "ierbivor"

    def mananca(self, animale, plante):
        for planta in plante:
            distanta = ((self.x - planta.pozitie[0]) ** 2 + (self.y - planta.pozitie[1]) ** 2) ** 0.5
            if distanta < 50: 
                self.energie += 20
                planta.age_remaning -= 10
                plante.remove(planta)  

               



# Clasa Carnivor, subclasă a clasei Animal
class Carnivor(Animal):
    def __init__(self, nume, x, y, energie, total_age, speed, imagine):
        super().__init__(nume, x, y, energie, total_age, speed, imagine)

    def tip_hrana(self):
        return "carnivor"

    def mananca(self, animale, plante=None):
        global populatie_iepuri, populatie_arici

        for prada in animale:
            if prada.tip_hrana() == "ierbivor" or prada.tip_hrana() == "omnivor":
                distanta = ((self.x - prada.x) ** 2 + (self.y - prada.y) ** 2) ** 0.5
                if distanta < 50:
                    self.energie += 30
                    prada.age_remaning = 0
                    animale.remove(prada)
                    
                    
                    if prada.nume == "Iepure":
                        populatie_iepuri -= 1
                    elif prada.nume == "arici":
                        populatie_arici -= 1

# Clasa Omnivor, subclasă a clasei Animal
class Omnivor(Animal):
    def __init__(self, nume, x, y, energie, total_age, speed, imagine):
        super().__init__(nume, x, y, energie, total_age, speed, imagine)

    def tip_hrana(self):
        return "omnivor"

    def mananca(self, animale, plante):
        global populatie_iepuri

        for planta in plante:
            distanta = ((self.x - planta.pozitie[0]) ** 2 + (self.y - planta.pozitie[1]) ** 2) ** 0.5
            if distanta < 50:  
                self.energie += 20
                planta.age_remaning -= 10
                plante.remove(planta)

        for prada in animale:
            if prada.tip_hrana() == "ierbivor":
                distanta = ((self.x - prada.x) ** 2 + (self.y - prada.y) ** 2) ** 0.5
                if distanta < 50:
                    self.energie += 30
                    prada.age_remaning = 0
                    animale.remove(prada)
                    
                    
                    if prada.nume == "Iepure":
                        populatie_iepuri -= 1



# Clasa Plante care moștenește Ecosistem
class Plante(Ecosistem):
    def __init__(self, nume, pozitie, energie, age_remaning, imagine):
        super().__init__(nume, pozitie, energie, age_remaning)
        self.imagine = pygame.image.load(imagine) 
        self.imagine = pygame.transform.scale(self.imagine, (30, 50)) 
        self.humidity = 1000 

    def status(self):
        return f"Plantă {self.nume}: Energie={self.energie}, Vârstă rămasă={self.age_remaning}"

    def draw(self, window):
       
        window.blit(self.imagine, self.pozitie)
    def actioneaza(self):
        pass

def plant_grow(plante):
    


    # Creăm plante noi la intervale regulate
    current_time = pygame.time.get_ticks()
    if current_time % 10000 < 50:
        new_planta = Plante("Iarbă", (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 30, 20, 'img/carot.jpeg')
        plante.append(new_planta)


    # Creăm plante noi la intervale regulate
    if current_time % 10000 < 50:
        new_planta = Plante("Iarbă", (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 30, 20, 'img/carot.jpeg')
        plante.append(new_planta)




iepure_imagine = 'img/rabit.jpeg'
fox_img = 'img/fox.jpeg'
omnivor_img = 'img/arici.jpeg'
rian_img='img/rain.png'
seceta_img='img/seceta.jpeg'


iepure = Erbivor('Iepure', 400, 300, 100, 100, 5, iepure_imagine)
iepure_2 = Erbivor('Iepure', 100, 130, 100, 100, 5, iepure_imagine)
iepure2 = Erbivor('Iepure', 650, 150, 100, 100, 5, iepure_imagine)
fox_1 = Carnivor('vulpe', 450, 350, 100, 100, 5, fox_img)
fox_2 = Carnivor('vulpe', 150, 350, 100, 100, 5, fox_img)
arici = Omnivor('arici', 200, 500, 100, 100, 3, omnivor_img)
arici_2 = Omnivor('arici', 200, 450, 100, 100, 2, omnivor_img)
arici_3 = Omnivor('arici', 50, 600, 100, 100, 3, omnivor_img)


coldown = 2000 
last_time = pygame.time.get_ticks()

animal_list = [iepure,iepure_2, iepure2, fox_1, arici,arici_2,arici_3,fox_2]  # Lista cu iepuri și vulpi
plante = [Plante("morcovi", (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 30, 20, 'img/carot.jpeg') for _ in range(10)]
weather=weather_conditions('normal',0,0,rian_img,seceta_img)

def redraw_game_window():
    bg = pygame.image.load('img/map.png')
    window.blit(bg, (0, 0))

  
    for planta in plante:
        planta.draw(window)

 
    for animal in animal_list:
        animal.draw(window)
    weather.draw(window)    


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    animale_noi = []
    for animal in animal_list[:]: 
        animal.deplaseaza()
        animal.mananca(animal_list, plante)
        animal.reproduce(animal_list, animale_noi)
    
    animal_list.extend(animale_noi)

      
            
    if ecosist_humidity>30: #am facut ca plantele cresc doar daca umiditatea e mai mare de 30
        plant_grow(plante)
    numar_animale=len([animal for animal in animal_list])
    populatie_iepuri = len([animal for animal in animal_list if animal.nume == "Iepure"])
    populatie_arici = len([animal for animal in animal_list if animal.nume == "arici"])
    populatie_vulpi = len([animal for animal in animal_list if animal.nume == "vulpe"])
    cantitate_plante = len([planta for planta in plante])

    if populatie_iepuri<3:
       
        iepure.erbivor_rata_supravetuire=20
        
        weather.weather_type('Iepure',iepure.erbivor_rata_supravetuire)
        ecosist_humidity+=20
   
    if populatie_arici<3:
       
        arici.omnivor_rata_supravetuire=20
        
        weather.weather_type('arici',arici.omnivor_rata_supravetuire)
        ecosist_humidity+=20
    
    current_time = pygame.time.get_ticks()

    if current_time - last_time >= coldown:  
         ecosisitem_status=StatusEcosistem(numar_animale,cantitate_plante,populatie_iepuri,populatie_arici,populatie_vulpi)

         print(ecosisitem_status.actioneaza())
         ecosist_humidity-=5
         
         if ecosist_humidity<0:
           
            weather.weather_type('plante',40)
            ecosist_humidity=100



                                    
         last_time = current_time  
  
    redraw_game_window()
    pygame.display.update()

pygame.quit()







