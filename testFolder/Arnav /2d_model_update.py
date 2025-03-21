import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1300, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Solar System - Click to Compare Planets")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Sun
GRAY = (169, 169, 169)  # Mercury
LIGHT_GRAY = (192, 192, 192)  # Venus
DODGER_BLUE = (30, 144, 255)  # Earth
TOMATO = (255, 99, 71)  # Mars
GOLD = (255, 165, 0)  # Jupiter
LIGHT_SKY_BLUE = (135, 206, 250)  # Saturn
STEEL_BLUE = (70, 130, 180)  # Uranus
MIDNIGHT_BLUE = (25, 25, 112)  # Neptune

# Font setup
font = pygame.font.SysFont('arial', 16)
title_font = pygame.font.SysFont('arial', 24, bold=True)
button_font = pygame.font.SysFont('arial', 20, bold=True)

# Planet data: (name, color, radius, distance from sun, speed, real radius(km), mass(10^24 kg), gravity(m/s^2), temperature(°C))
planets = [
    ("Sun", YELLOW, 20, 0, 0, 696340, 1988500000, 274, 5505),
    ("Mercury", GRAY, 5, 50, 4, 2439.7, 0.33, 3.7, 167),
    ("Venus", LIGHT_GRAY, 8, 90, 3.5, 6051.8, 4.87, 8.9, 464),
    ("Earth", DODGER_BLUE, 10, 140, 2.5, 6371, 5.97, 9.8, 15),
    ("Mars", TOMATO, 7, 190, 2, 3389.5, 0.642, 3.7, -65),
    ("Jupiter", GOLD, 25, 300, 1.8, 69911, 1898, 23.1, -110),
    ("Saturn", LIGHT_SKY_BLUE, 22, 450, 1.4, 58232, 568, 9.0, -140),
    ("Uranus", STEEL_BLUE, 19, 600, 1.2, 25362, 86.8, 8.7, -195),
    ("Neptune", MIDNIGHT_BLUE, 18, 750, 1, 24622, 102, 11.0, -200),
]

# Variables to track selected planets
selected_planets = []
displaying_info = False
info_timer = 0
INFO_DISPLAY_TIME = 10 * 60  # 10 seconds at 60 FPS

# Freeze button variables
frozen = False
button_width, button_height = 100, 40
button_x = WIDTH - button_width - 20
button_y = 20
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Function to check if a point is inside a circle
def point_in_circle(point, center, radius):
    return math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2) <= radius

# Function to display planet comparison
def display_planet_comparison(planet1, planet2):
    # Create info panel
    panel_width, panel_height = 500, 400
    panel_x = (WIDTH - panel_width) // 2
    panel_y = (HEIGHT - panel_height) // 2
    
    # Draw panel background
    pygame.draw.rect(screen, (50, 50, 50), (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, WHITE, (panel_x, panel_y, panel_width, panel_height), 2)
    
    # Draw title
    title = f"Comparing {planet1[0]} and {planet2[0]}"
    title_surf = title_font.render(title, True, WHITE)
    screen.blit(title_surf, (panel_x + (panel_width - title_surf.get_width()) // 2, panel_y + 20))
    
    # Draw comparison data
    y_offset = panel_y + 70
    line_height = 30
    
    # Headers
    screen.blit(font.render("Property", True, WHITE), (panel_x + 20, y_offset))
    screen.blit(font.render(planet1[0], True, planet1[1]), (panel_x + 200, y_offset))
    screen.blit(font.render(planet2[0], True, planet2[1]), (panel_x + 350, y_offset))
    
    # Separator line
    pygame.draw.line(screen, WHITE, (panel_x + 10, y_offset + line_height - 5), 
                    (panel_x + panel_width - 10, y_offset + line_height - 5))
    y_offset += line_height
    
    # Radius
    screen.blit(font.render("Radius (km)", True, WHITE), (panel_x + 20, y_offset))
    screen.blit(font.render(f"{planet1[5]:,}", True, WHITE), (panel_x + 200, y_offset))
    screen.blit(font.render(f"{planet2[5]:,}", True, WHITE), (panel_x + 350, y_offset))
    y_offset += line_height
    
    # Mass
    screen.blit(font.render("Mass (10^24 kg)", True, WHITE), (panel_x + 20, y_offset))
    screen.blit(font.render(f"{planet1[6]:,}", True, WHITE), (panel_x + 200, y_offset))
    screen.blit(font.render(f"{planet2[6]:,}", True, WHITE), (panel_x + 350, y_offset))
    y_offset += line_height
    
    # Gravity
    screen.blit(font.render("Surface Gravity (m/s²)", True, WHITE), (panel_x + 20, y_offset))
    screen.blit(font.render(f"{planet1[7]}", True, WHITE), (panel_x + 200, y_offset))
    screen.blit(font.render(f"{planet2[7]}", True, WHITE), (panel_x + 350, y_offset))
    y_offset += line_height
    
    # Temperature
    screen.blit(font.render("Avg. Temperature (°C)", True, WHITE), (panel_x + 20, y_offset))
    screen.blit(font.render(f"{planet1[8]}", True, WHITE), (panel_x + 200, y_offset))
    screen.blit(font.render(f"{planet2[8]}", True, WHITE), (panel_x + 350, y_offset))
    y_offset += line_height
    
    # Size comparison
    screen.blit(font.render(f"Size ratio: {planet1[0]} is {planet1[5]/planet2[5]:.2f}x {planet2[0]}" if planet1[5] > planet2[5] else 
                           f"Size ratio: {planet2[0]} is {planet2[5]/planet1[5]:.2f}x {planet1[0]}", 
                True, WHITE), (panel_x + 20, y_offset))
    y_offset += line_height
    
    # Mass comparison
    screen.blit(font.render(f"Mass ratio: {planet1[0]} is {planet1[6]/planet2[6]:.2f}x {planet2[0]}" if planet1[6] > planet2[6] else 
                           f"Mass ratio: {planet2[0]} is {planet2[6]/planet1[6]:.2f}x {planet1[0]}", 
                True, WHITE), (panel_x + 20, y_offset))
    y_offset += line_height
    
    # Distance comparison
    distance = abs(planet1[3] - planet2[3])
    screen.blit(font.render(f"Orbital separation: {distance} units", True, WHITE), (panel_x + 20, y_offset))
    y_offset += line_height

    # Info text
    screen.blit(font.render("Click anywhere to close this panel", True, (200, 200, 200)), 
               (panel_x + (panel_width - font.size("Click anywhere to close this panel")[0]) // 2, panel_y + panel_height - 30))

# Function to draw the freeze button
def draw_freeze_button():
    # Draw button background
    button_color = (100, 100, 255) if not frozen else (255, 100, 100)
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)
    
    # Draw button text
    text = "Freeze" if not frozen else "Unfreeze"
    text_surf = button_font.render(text, True, WHITE)
    screen.blit(text_surf, (button_x + (button_width - text_surf.get_width()) // 2, 
                           button_y + (button_height - text_surf.get_height()) // 2))

# Game loop
running = True
angle = 0
clock = pygame.time.Clock()

while running:
    # Handle planet comparison display
    if displaying_info:
        screen.fill(BLACK)
        
        # Draw dimmed planets in background
        # Draw sun
        pygame.draw.circle(screen, (YELLOW[0]//3, YELLOW[1]//3, YELLOW[2]//3), (WIDTH // 2, HEIGHT // 2), 20)
        
        # Draw planets
        for name, color, radius, distance, speed, real_radius, mass, gravity, temp in planets[1:]:
            x = WIDTH // 2 + int(distance * math.cos(math.radians(angle * speed)))
            y = HEIGHT // 2 + int(distance * math.sin(math.radians(angle * speed)))
            dim_color = (color[0]//3, color[1]//3, color[2]//3)
            pygame.draw.circle(screen, dim_color, (x, y), radius)
            
        # Display comparison information
        display_planet_comparison(selected_planets[0], selected_planets[1])
        
        # Timer for info display
        info_timer += 1
        if info_timer >= INFO_DISPLAY_TIME:
            displaying_info = False
            info_timer = 0
            selected_planets = []
    else:
        screen.fill(BLACK)
        
        # Get planet positions for click detection
        planet_positions = []
        
        # Draw sun at center
        sun_pos = (WIDTH // 2, HEIGHT // 2)
        pygame.draw.circle(screen, YELLOW, sun_pos, 20)
        planet_positions.append((planets[0], sun_pos))
        
        # Draw planets
        for planet_data in planets[1:]:
            name, color, radius, distance, speed = planet_data[:5]
            x = WIDTH // 2 + int(distance * math.cos(math.radians(angle * speed)))
            y = HEIGHT // 2 + int(distance * math.sin(math.radians(angle * speed)))
            pygame.draw.circle(screen, color, (x, y), radius)
            planet_positions.append((planet_data, (x, y)))
        
        # Draw selection indicators
        for planet_data, pos in planet_positions:
            if planet_data in selected_planets:
                pygame.draw.circle(screen, WHITE, pos, planet_data[2] + 3, 2)  # Draw selection ring
        
        # Display planet labels for better UX
        for planet_data, pos in planet_positions:
            name = planet_data[0]
            label = font.render(name, True, WHITE)
            screen.blit(label, (pos[0] - label.get_width() // 2, pos[1] + planet_data[2] + 5))
        
        # Display instruction if no planets are selected
        if not selected_planets:
            instruction = font.render("Click on two planets to compare them", True, WHITE)
            screen.blit(instruction, (10, 10))
        # Display which planet is selected if only one is selected
        elif len(selected_planets) == 1:
            instruction = font.render(f"Selected: {selected_planets[0][0]}. Click another planet to compare.", True, WHITE)
            screen.blit(instruction, (10, 10))
        
        # Draw the freeze button
        draw_freeze_button()

    # Update display
    pygame.display.flip()
    
    # Only update angle if not frozen
    if not frozen:
        angle += 0.5  # Slower animation for better visibility
    
    clock.tick(60)  # Limit to 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_pos = pygame.mouse.get_pos()
            
            # Check if freeze button was clicked
            if button_rect.collidepoint(mouse_pos) and not displaying_info:
                frozen = not frozen
                continue
                
            if displaying_info:
                # Close the info panel on click
                displaying_info = False
                info_timer = 0
                selected_planets = []
            else:
                # Check if a planet was clicked
                for planet_data, pos in planet_positions:
                    if point_in_circle(mouse_pos, pos, planet_data[2]):
                        # If planet already selected, deselect it
                        if planet_data in selected_planets:
                            selected_planets.remove(planet_data)
                        # Otherwise select it if we don't already have 2 planets
                        elif len(selected_planets) < 2:
                            selected_planets.append(planet_data)
                        
                        # If two planets are selected, show comparison
                        if len(selected_planets) == 2:
                            displaying_info = True
                            info_timer = 0
                        
                        break  # Only select one planet per click

pygame.quit()