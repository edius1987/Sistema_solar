#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criado em qui ago 01 23:29:20 2024

@autor: Edius Ferreira 
email: ediusferreira@gmail.com
licença: MIT
"""
import pygame
import math
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema Solar")

# Cores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)  # Sol
GRAY = (150, 150, 150)  # Mercúrio
WHITE = (255, 255, 255)  # Vênus
BLUE = (100, 149, 237)  # Terra
RED = (188, 39, 50)  # Marte
BROWN = (165, 42, 42)  # Júpiter
ORANGE = (255, 165, 0)  # Saturno
CYAN = (0, 255, 255)  # Urano
LIGHT_BLUE = (173, 216, 230)  # Netuno

# Fonte para os nomes dos planetas
font = pygame.font.SysFont('Arial', 16)

# Classe para representar um planeta
class Planet:
    def __init__(self, name, color, radius, distance, speed, has_rings=False):
        self.name = name
        self.color = color
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.has_rings = has_rings
    
    def update(self):
        self.angle += self.speed
    
    def draw(self, surface):
        # Calcular a posição do planeta
        x = WIDTH // 2 + math.cos(self.angle) * self.distance
        y = HEIGHT // 2 + math.sin(self.angle) * self.distance
        
        # Desenhar a órbita
        pygame.draw.circle(surface, (50, 50, 50), (WIDTH // 2, HEIGHT // 2), self.distance, 1)
        
        # Desenhar o planeta
        pygame.draw.circle(surface, self.color, (int(x), int(y)), self.radius)
        
        # Desenhar os anéis de Saturno
        if self.has_rings:
            pygame.draw.ellipse(surface, (200, 200, 200), 
                               (int(x - self.radius * 1.5), int(y - self.radius * 0.5), 
                                self.radius * 3, self.radius), 1)
        
        # Desenhar o nome do planeta
        name_text = font.render(self.name, True, WHITE)
        surface.blit(name_text, (int(x) - name_text.get_width() // 2, int(y) - self.radius - 20))

# Criar os planetas
planets = [
    Planet("Mercúrio", GRAY, 5, 80, 0.04),
    Planet("Vênus", WHITE, 8, 120, 0.015),
    Planet("Terra", BLUE, 10, 180, 0.01),
    Planet("Marte", RED, 7, 240, 0.008),
    Planet("Júpiter", BROWN, 20, 320, 0.004),
    Planet("Saturno", ORANGE, 18, 400, 0.002, True),
    Planet("Urano", CYAN, 12, 480, 0.001),
    Planet("Netuno", LIGHT_BLUE, 12, 560, 0.0007)
]

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preencher a tela com preto
    screen.fill(BLACK)
    
    # Desenhar o Sol
    pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), 30)
    
    # Atualizar e desenhar os planetas
    for planet in planets:
        planet.update()
        planet.draw(screen)
    
    # Atualizar a tela
    pygame.display.flip()
    
    # Controlar a velocidade da animação
    clock.tick(60)

pygame.quit()
sys.exit()
