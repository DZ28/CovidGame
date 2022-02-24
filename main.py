import pygame
import random
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 127)
days = 0
death = False

HEALTHY = 1
INFECTED = 2
DEATH = 3
RECOVERED = 4
MEDIC = 5
VACCINE = 6


print('/')
print('/')
print('/')
print('/')
print('/')
print('/')
print('/')
print('Welcome to the CORONAVIRUS SIMULATOR! Please answer the questions given to you in the next few moments')


class Person:
    def __init__(self):
        self.status = HEALTHY
        self.x = random.randint(6, 794)
        self.y = random.randint(6, 594)

    def draw(self, color):
        pygame.draw.circle(screen, color, (self.x, self.y), 6, 1)

    def draw_self(self):
        if self.status == HEALTHY:
            self.draw(GREEN)
        elif self.status == INFECTED:
            self.draw(RED)
        elif self.status == DEATH:
            self.draw(WHITE)
        elif self.status == RECOVERED:
            self.draw(PINK)
        elif self.status == MEDIC:
            self.draw(CYAN)
        elif self.status == VACCINE:
            self.draw(YELLOW)
        else:
            self.draw(BLUE)

    def move(self):
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        if self.x < 10:
            self.x = 10
        elif self.x > 794:
            self.x = 794
        elif self.y < 6:
            self.y = 6
        elif self.y > 594:
            self.y = 594

    def move_redraw(self):
        self.draw(BLACK)
        self.move()
        self.draw_self()

    def become_sick(self):
        self.status = INFECTED

    def become_dead(self):
        self.status = DEATH

    def become_recovered(self):
        self.status = RECOVERED

    def become_medic(self):
        self.status = MEDIC

    def is_close(self, other):
        return ((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) <= 676

    def is_healthy(self):
        return self.status == HEALTHY

    def update_status(self):
        if self.status == INFECTED:
            rate = random.randint(1, 1000)
            if rate <= 1:
                self.status = RECOVERED



all_people = []


class MedicalDude:
    def __init__(self):
        self.medicx = random.randint(6, 794)
        self.medicy = random.randint(6, 594)

    def draw_self(self):
        pygame.draw.rect(screen, CYAN, (self.medicx, self.medicy, 10, 10), True)

    def move(self):
        self.medicx += random.randint(-20, 20)
        self.medicy += random.randint(-20, 20)
        if self.medicx < 10:
            self.medicx = 10
        elif self.medicx > 794:
            self.medicx = 794
        elif self.medicy < 6:
            self.medicy = 6
        elif self.medicy > 594:
            self.medicy = 594

    def draw(self, color):
        pygame.draw.rect(screen, color, (self.medicx, self.medicy, 10, 10), True)

    def medic_redraw(self):
        self.draw(BLACK)
        self.move()
        self.draw_self()

    def touch_then_healthy(self):
        for y in all_people:
            if y.status != HEALTHY:
                continue
            if ((self.medicx - y.x) ** 2) + ((self.medicy - y.y) ** 2) <= 400:
                y.status = VACCINE


def touch_then_sick():
    for a1 in all_people:
        if a1.status != INFECTED:
            continue
        for a2 in all_people:
            if a2.status != HEALTHY:
                continue
            if a1.is_close(a2):
                a2.become_sick()


def count_infected():
    infected = 0
    recovered = 0
    # print('start')
    for a3 in all_people:
        if a3.status == INFECTED:
            infected += 1
            # print(a3.status)
        if a3.status == RECOVERED:
            recovered += 1
            # print(a3.status)
    infected += recovered
    # print('end')
    return infected, recovered


def display_status(number_infected, number_recovered, days2):
    full_days = int(days2)
    myfont = pygame.font.SysFont('Garamond', 30)
    text_surface = myfont.render('Infected: ' + str(number_infected)
                                 + ' Recovered: ' + str(number_recovered)
                                 + ' Days: ' + str(full_days), False, WHITE)
    screen.blit(text_surface, (2, 0))

def title():
    title_font = pygame.font.SysFont('Comic Sans Ms', 70)
    title_text_surface = title_font.render('Welcome to the', False, GREEN)
    coronavirus_surface = title_font.render('Coronavirus Simulation', False, GREEN)

    screen.blit(title_text_surface, (110, 110))
    screen.blit(coronavirus_surface, (30, 200))

def start_screen():
    screen.fill(BLACK)

    start_font = pygame.font.SysFont('Comic Sans Ms', 40)
    beginning_text_surface = start_font.render('Press Enter to Begin', False, WHITE)
    screen.blit(beginning_text_surface, (200, 300))

def rules_kinda():
    rules_font = pygame.font.SysFont('Comic Sans Ms', 20)
    healthy_text_surface = rules_font.render('Green shows a healthy person', False, GREEN)
    sick_text_surface = rules_font.render('Red shows a sick person', False, RED)
    pink_text_surface = rules_font.render('Pink shows a person that recovered', False, PINK)
    yellow_text_surface = rules_font.render('Yellow shows a person that is vaccined', False, YELLOW)
    cyan_text_surface = rules_font.render('Blue shows a person who hands out the vaccines', False, CYAN)
    screen.blit(healthy_text_surface, (200, 340))
    screen.blit(sick_text_surface, (200, 360))
    screen.blit(pink_text_surface, (200, 380))
    screen.blit(yellow_text_surface, (200, 400))
    screen.blit(cyan_text_surface, (200, 420))

def question_0():
    screen.fill(pygame.Color('black'))
    screen.fill(pygame.Color('black'), (0, 0, 110, 40))
    question_0_font = pygame.font.SysFont('Comic Sans Ms', 20)
    question_0_text_surface = question_0_font.render('We will ask a couple questions first. Press Space to continue.',
                                                     False, WHITE)
    screen.blit(question_0_text_surface, (100, 300))


def question_1():
    screen.fill(pygame.Color('black'))
    question_1_font = pygame.font.SysFont('Comic Sans Ms', 20)
    question_1_text_surface = question_1_font.render('What is the population count? ', False, WHITE)
    question_1_text_surface_II = question_1_font.render(
        'Type 1 for 100, Type 2 for 200, Type 3 for 300, or Type c for Custom ', False, WHITE)
    screen.blit(question_1_text_surface, (250, 300))
    screen.blit(question_1_text_surface_II, (100, 350))


def custom_question():
    question_1_custom_font = pygame.font.SysFont('Comic Sans Ms', 20)
    question_1_custom_text_surface = question_1_custom_font.render('Go to the input bar in the other window', False,
                                                                   WHITE)
    screen.blit(question_1_custom_text_surface, (250, 400))


def question_2():
    screen.fill(pygame.Color('black'))
    question_2_font = pygame.font.SysFont('Comic Sans Ms', 20)
    question_2_text_surface = question_2_font.render('How many people will be infected in the beginning? ', False,
                                                     WHITE)
    question_2_text_surface_II = question_2_font.render(
        'Type 1 for 1, Type 2 for 2, Type 3 for 3, or Type c for Custom', False, WHITE)
    screen.blit(question_2_text_surface, (150, 300))
    screen.blit(question_2_text_surface_II, (100, 350))


def question_3():
    screen.fill(pygame.Color('black'))
    question_3_font = pygame.font.SysFont('Comic Sans Ms', 20)
    question_3_text_surface = question_3_font.render('Will there be vaccines? Type y for yes or n for no', False, WHITE)
    screen.blit(question_3_text_surface, (150, 300))


def ending_word():
    ending_word_font = pygame.font.SysFont('Comic Sans Ms', 20)
    ending_word_text_surface = ending_word_font.render('Press e to end simulation', False, WHITE)
    screen.blit(ending_word_text_surface, (550, 560))


def stats(days2):
    percent_infected = int(infected)/int(population_count)
    percent_infected *= 100
    full_days = int(days2)

    screen.fill(pygame.Color('black'))
    stat_font = pygame.font.SysFont('Garamond', 30)
    stat_font_text_surface_beginning = stat_font.render('Final Statistics', False, WHITE)
    screen.blit(stat_font_text_surface_beginning, (200, 100))
    stat_days_text_surface = stat_font.render('Total Days: ' + str(full_days), False, WHITE)
    screen.blit(stat_days_text_surface, (200, 150))
    stat_infected_text_surface = stat_font.render('Percent Infected: ' + str(percent_infected) + '%', False, WHITE)
    screen.blit(stat_infected_text_surface, (200, 200))



Medic = []

start = False
running = True
everyone_infected = False
questions_answered = False
question_0_answered = False
question_1_answered = False
question_2_answered = False
question_3_answered = False
end_not_there_yet = True
set_numbers = 0
lets_go = False
screen.fill(pygame.Color('black'))
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if end_not_there_yet:

        if not start:
            start_screen()
            title()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
        pygame.display.flip()

        if start:
            if not question_0_answered:
                question_0()
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type != pygame.KEYDOWN:
                        continue
                    if event.key == pygame.K_SPACE:
                        question_0_answered = True
            if question_0_answered:
                if not question_1_answered:
                    question_1()
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                population_count = 100
                                set_numbers += 1
                                question_1_answered = True
                            if event.key == pygame.K_2:
                                population_count = 200
                                set_numbers += 1
                                question_1_answered = True
                            if event.key == pygame.K_3:
                                population_count = 300
                                set_numbers += 1
                                question_1_answered = True
                            if event.key == pygame.K_c:
                                custom_question()
                                pygame.display.flip()
                                population_count = int(input('Please Enter Your Custom Population Count: '))
                                set_numbers += 1
                                question_1_answered = True

                if question_1_answered:
                    if not question_2_answered:
                        question_2()
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    people_infected_at_the_beginning = 1
                                    set_numbers += 1
                                    question_2_answered = True
                                if event.key == pygame.K_2:
                                    people_infected_at_the_beginning = 2
                                    set_numbers += 1
                                    question_2_answered = True
                                if event.key == pygame.K_3:
                                    people_infected_at_the_beginning = 3
                                    set_numbers += 1
                                    question_2_answered = True
                                if event.key == pygame.K_c:
                                    custom_question()
                                    pygame.display.flip()
                                    people_infected_at_the_beginning = int(
                                        input('Enter your custom number of infected at the beginning: '))
                                    set_numbers += 1
                                    question_2_answered = True
                    if question_2_answered:
                        if not question_3_answered:
                            question_3()
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_y:
                                        custom_question()
                                        pygame.display.flip()
                                        print('Try to start with 1% or less of your population')
                                        medical_number = int(
                                            input('Please Enter your custom number of medical people: '))
                                        set_numbers += 1
                                        question_3_answered = True

                                    if event.key == pygame.K_n:
                                        medical_number = 0
                                        set_numbers += 1
                                        question_3_answered = True

                        if question_3_answered:

                            if not lets_go:
                                start_screen()
                                rules_kinda()
                                pygame.display.flip()

                                for event in pygame.event.get():

                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RETURN:
                                            questions_answered = True
                                            lets_go = True

            if set_numbers == 3:

                for w in range(int(medical_number)):
                    m1 = MedicalDude()
                    Medic.append(m1)

                for i in range(int(population_count)):
                    p1 = Person()
                    all_people.append(p1)

                for h in all_people:
                    hh = 0
                    if hh < people_infected_at_the_beginning:
                        hh = int(hh)
                        all_people[hh].become_sick()
                        hh += 1
                set_numbers -= 1

            if questions_answered:
                screen.fill(BLACK)

                touch_then_sick()
                infected, recovered = count_infected()
                display_status(infected, recovered, days)

                for z in Medic:
                    z.medic_redraw()
                    z.touch_then_healthy()

                for a in all_people:
                    a.move_redraw()
                    a.update_status()
                    
                days += 0.05
                ending_word()
                pygame.display.flip()
                time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        stats(days)
                        pygame.display.flip()
                        end_not_there_yet = False






















