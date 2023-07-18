import pygame
import sys
import random

class Card:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.is_visible = True

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def hide(self):
        self.is_visible = False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Whack the Snack!')
clock = pygame.time.Clock()
the_font = pygame.font.Font('font/gooddog.ttf', 50)
score = 0

# Hole positions
hole_positions = [
    (500, 500),
    (200, 500),
    (800, 500),
    (600, 650),
    (300, 650)
]

# Card images
card_images = [
    "graphics/apple.png",
    "graphics/banana.png",
    "graphics/bread.png",
    "graphics/cake.png",
    "graphics/carrot.png",
    "graphics/egg.png",
    "graphics/orange.png",
    "graphics/potato.png",
    "graphics/tomato.png"
]

# Shuffle the cards
random.shuffle(card_images)

# Surfaces
background_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = the_font.render('Score: ' + str(score), False, 'Brown')

# Initialize Pygame sound mixer
pygame.mixer.init()

# Load the audio files
apple_sound = pygame.mixer.Sound('audio/fc_apple.mp3')
banana_sound = pygame.mixer.Sound('audio/fc_banana.mp3')
bread_sound = pygame.mixer.Sound('audio/fc_bread.mp3')
cake_sound = pygame.mixer.Sound('audio/fc_cake.mp3')
tick_sound = pygame.mixer.Sound('audio/tick.mp3')

# Initialize the tick image and rect
tick_image = pygame.image.load('graphics/tick.png')
tick_rect = tick_image.get_rect()

# Tick duration and frame count
tick_duration = 30  # Number of frames to display the tick
tick_frame_count = 0

# Game loop
click_count = 0  # Counter for the number of clicks
correct_clicks = 0  # Counter for the number of correct clicks

#------------------------------------------------------------------------------------#

# Apple round
while score < 3:
    # Initialize display_tick
    display_tick = False

    # Determine the card to appear
    card_path = "graphics/apple.png"
    random_position = random.choice(hole_positions)
    card = Card(card_path, random_position)
    card.is_visible = True

    # Play the audio
    apple_sound.play()

    # Card interaction loop (Apple round)
    while card.is_visible:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if card.is_clicked(mouse_pos):
                        card.hide()
                        correct_clicks += 1
                        score += 1
                        text_surface = the_font.render('Score: ' + str(score), False, 'Brown')
                        display_tick = True
                        tick_frame_count = 0
                        tick_sound.play()
                    else:
                        card.hide()
                        random_position = random.choice(hole_positions)

        # Render the game
        screen.blit(background_surface, (0, 0))
        pygame.draw.ellipse(screen, (92, 64, 51), (500, 700, 190, 90))  # bottom right
        pygame.draw.ellipse(screen, (92, 64, 51), (100, 550, 190, 90))  # top left hole
        pygame.draw.ellipse(screen, (92, 64, 51), (700, 550, 190, 90))  # top right
        pygame.draw.ellipse(screen, (92, 64, 51), (200, 700, 190, 90))  # bottom left
        pygame.draw.ellipse(screen, (92, 64, 51), (400, 550, 190, 90))  # top middle
        if display_tick and tick_frame_count < tick_duration:
            tick_rect.center = card.rect.center
            screen.blit(tick_image, tick_rect)
            tick_frame_count += 1

        card.draw(screen)
        screen.blit(text_surface, (800, 50))

        pygame.display.flip()

    # Delay before the next card appears
    pygame.time.delay(2000)

#------------------------------------------------------------------------------------#

# Initialize play_banana_audio flag
play_banana_audio = True
banana_round_completed = False

# Banana round
banana_channel = pygame.mixer.Channel(1)  # Create a channel for the banana sound
while score < 9:
    if not banana_round_completed:
        # Determine the cards to appear (banana and any other card)
        banana_path = "graphics/banana.png"

        # Delay before initializing the cards and playing the audio
        pygame.time.delay(500)  # Adjust the delay duration as needed

        # Play the audio if it's the first iteration of the banana round or after each correct selection
        if play_banana_audio:
            pygame.time.delay(200)  # Delay before playing the banana audio
            banana_channel.play(banana_sound)
            play_banana_audio = False

        # Delay before initializing the cards
        pygame.time.delay(200)  # Adjust the delay duration as needed

        # Determine the position for the banana card
        banana_position = random.choice(hole_positions)
        banana_card = Card(banana_path, banana_position)
        banana_card.is_visible = True

        # Determine the position for the other card (not the same as banana position)
        other_card_path = random.choice(card_images)
        other_position = random.choice([pos for pos in hole_positions if pos != banana_position])
        other_card = Card(other_card_path, other_position)
        other_card.is_visible = True

        # Flag to keep track of the wrong card selection
        wrong_card_selected = False

        # Card interaction loop (Banana round)
        while banana_card.is_visible or other_card.is_visible:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()
                        if banana_card.is_visible and banana_card.is_clicked(mouse_pos):
                            banana_card.hide()
                            score += 1
                            text_surface = the_font.render('Score: ' + str(score), False, 'Brown')
                            display_tick = True
                            tick_frame_count = 0
                            tick_sound.play()

                            # Check if the score is still less than 6
                            if score < 6:
                                # Reset cards and play_banana_audio flag
                                banana_card.hide()
                                other_card.hide()
                                play_banana_audio = True
                            elif score == 6:
                                # Transition to the Bread round
                                banana_round_completed = True
                                other_card.hide()  # Hide the other card
                                pygame.time.delay(1000)  # Delay before the Bread round begins
                                break  # Exit the Banana round loop

                            elif other_card.is_visible and other_card.is_clicked(mouse_pos):
                                # Hide both cards
                                banana_card.hide()
                                other_card.hide()
                                wrong_card_selected = True

            # If wrong card selected, replay banana audio
            if wrong_card_selected and not banana_channel.get_busy():
                banana_channel.play(banana_sound)

            # Render the game
            screen.blit(background_surface, (0, 0))
            pygame.draw.ellipse(screen, (92, 64, 51), (500, 700, 190, 90))  # bottom right
            pygame.draw.ellipse(screen, (92, 64, 51), (100, 550, 190, 90))  # top left hole
            pygame.draw.ellipse(screen, (92, 64, 51), (700, 550, 190, 90))  # top right
            pygame.draw.ellipse(screen, (92, 64, 51), (200, 700, 190, 90))  # bottom left
            pygame.draw.ellipse(screen, (92, 64, 51), (400, 550, 190, 90))  # top middle
            if display_tick and tick_frame_count < tick_duration:
                tick_rect.center = banana_card.rect.center
                screen.blit(tick_image, tick_rect)
                tick_frame_count += 1

            banana_card.draw(screen)
            other_card.draw(screen)
            screen.blit(text_surface, (800, 50))

            pygame.display.flip()

        # Delay before the next round or end of the game
        pygame.time.delay(2000)

#------------------------------------------------------------------------------------#

    # Bread round
    play_bread_audio = True
    bread_channel = pygame.mixer.Channel(2)
    while banana_round_completed and score < 9:
        # Determine the card to appear
        bread_path = "graphics/bread.png"

        # Play the audio if it's the first iteration of the bread round or after each correct selection
        if play_bread_audio:
            bread_channel.play(bread_sound)
            play_bread_audio = False

        # Determine the position for the bread card
        bread_position = random.choice(hole_positions)
        bread_card = Card(bread_path, bread_position)
        bread_card.is_visible = True

        # Determine the position for the other cards (not the bread)
        other_card_path = random.choice(card_images)
        other_position = random.choice([pos for pos in hole_positions if pos != bread_position])
        other_card = Card(other_card_path, other_position)
        other_card.is_visible = True

        extra_card_path = random.choice(card_images)
        extra_card_position = random.choice([pos for pos in hole_positions if pos != bread_position and pos != other_position])
        extra_card = Card(extra_card_path, extra_card_position)
        extra_card.is_visible = True

        # Flag to keep track of the wrong card selection
        wrong_card_selected = False

        # Card interaction loop (Bread round)
        while bread_card.is_visible or other_card.is_visible or extra_card.is_visible:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()
                        if bread_card.is_visible and bread_card.is_clicked(mouse_pos):
                            bread_card.hide()
                            score += 1
                            text_surface = the_font.render('Score: ' + str(score), False, 'Brown')
                            display_tick = True
                            tick_frame_count = 0
                            tick_sound.play()

                        # Check if the score is still less than 9
                            if score < 9:
                            # Reset cards and play_bread_audio flag
                                bread_card.hide()
                                other_card.hide()
                                extra_card.hide()
                                play_bread_audio = True
                            elif score == 9:
                                # Hide the other cards
                                other_card.hide()
                                extra_card.hide()
                                break  # Exit the Bread round loop

                        elif other_card.is_visible and other_card.is_clicked(mouse_pos):
                            # Hide the other cards
                            other_card.hide()
                            extra_card.hide()
                            wrong_card_selected = True
                        elif extra_card.is_visible and extra_card.is_clicked(mouse_pos):
                            # Hide the other cards
                            other_card.hide()
                            extra_card.hide()
                            wrong_card_selected = True

            # If wrong card selected, replay bread audio
            if wrong_card_selected and not bread_channel.get_busy():
                bread_channel.play(bread_sound)

            # Render the game
            screen.blit(background_surface, (0, 0))
            pygame.draw.ellipse(screen, (92, 64, 51), (500, 700, 190, 90))  # bottom right
            pygame.draw.ellipse(screen, (92, 64, 51), (100, 550, 190, 90))  # top left hole
            pygame.draw.ellipse(screen, (92, 64, 51), (700, 550, 190, 90))  # top right
            pygame.draw.ellipse(screen, (92, 64, 51), (200, 700, 190, 90))  # bottom left
            pygame.draw.ellipse(screen, (92, 64, 51), (400, 550, 190, 90))  # top middle
            if display_tick and tick_frame_count < tick_duration:
                tick_rect.center = bread_card.rect.center
                screen.blit(tick_image, tick_rect)
                tick_frame_count += 1

            bread_card.draw(screen)
            other_card.draw(screen)
            extra_card.draw(screen)
            screen.blit(text_surface, (800, 50))

            pygame.display.flip()

        # Delay before the next round or end of the game
        pygame.time.delay(2000)

        if score == 9:
            other_card.hide()  # Hide the other card
            extra_card.hide()  # Hide the extra card
            bread_card.hide()  # Hide the bread card
            pygame.time.delay(1000)  # Delay before the Cake round begins
            cake_round_completed = True  # Set the flag to True to enter the Cake round
            break  # Exit the Bread round loop

#------------------------------------------------------------------------------------#
# Initialize play_cake_audio flag
play_cake_audio = True
cake_round_completed = False

cake_channel = pygame.mixer.Channel(3)
while not cake_round_completed and score < 12:
    # Determine the card to appear
    cake_path = "graphics/cake.png"

    # Play the audio if it's the first iteration of the cake round or after each correct selection
    if play_cake_audio:
        cake_channel.play(cake_sound)
        play_cake_audio = False

    # Determine the position for the cake card
    cake_position = random.choice(hole_positions)
    cake_card = Card(cake_path, cake_position)
    cake_card.is_visible = True

    # Determine the position for the other cards (not the cake)
    other_card_path = random.choice(card_images)
    other_position = random.choice([pos for pos in hole_positions if pos != cake_position])
    other_card = Card(other_card_path, other_position)
    other_card.is_visible = True

    extra_card_path = random.choice(card_images)
    extra_card_position = random.choice([pos for pos in hole_positions if pos != cake_position and pos != other_position])
    extra_card = Card(extra_card_path, extra_card_position)
    extra_card.is_visible = True

    third_card_path = random.choice(card_images)
    third_card_position = random.choice([pos for pos in hole_positions if pos != cake_position and pos != other_position and pos != extra_card_position])
    third_card = Card(third_card_path, third_card_position)
    third_card.is_visible = True

    # Flag to keep track of the wrong card selection
    wrong_card_selected = False

    # Card interaction loop (Cake round)
    while cake_card.is_visible or other_card.is_visible or extra_card.is_visible or third_card.is_visible:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if cake_card.is_visible and cake_card.is_clicked(mouse_pos):
                        cake_card.hide()
                        score += 1
                        text_surface = the_font.render('Score: ' + str(score), False, 'Brown')
                        display_tick = True
                        tick_frame_count = 0
                        tick_sound.play()

                        # Check if the score is still less than 9
                        if score < 12:
                            # Reset cards and play_cake_audio flag
                            cake_card.hide()
                            other_card.hide()
                            extra_card.hide()
                            third_card.hide()
                            play_cake_audio = True
                        elif score == 12:
                            # End the game or perform necessary actions
                            pass

                    elif other_card.is_visible and other_card.is_clicked(mouse_pos):
                        # Hide all cards
                        cake_card.hide()
                        other_card.hide()
                        extra_card.hide()
                        third_card.hide()
                        wrong_card_selected = True
                    elif extra_card.is_visible and extra_card.is_clicked(mouse_pos):
                        # Hide all cards
                        cake_card.hide()
                        other_card.hide()
                        extra_card.hide()
                        third_card.hide()
                        wrong_card_selected = True
                    elif third_card.is_visible and third_card.is_clicked(mouse_pos):
                        # Hide all cards
                        cake_card.hide()
                        other_card.hide()
                        extra_card.hide()
                        third_card.hide()
                        wrong_card_selected = True

        # If wrong card selected, replay cake audio
        if wrong_card_selected and not cake_channel.get_busy():
            cake_channel.play(cake_sound)

        # Render the game
        screen.blit(background_surface, (0, 0))
        pygame.draw.ellipse(screen, (92, 64, 51), (500, 700, 190, 90))  # bottom right
        pygame.draw.ellipse(screen, (92, 64, 51), (100, 550, 190, 90))  # top left hole
        pygame.draw.ellipse(screen, (92, 64, 51), (700, 550, 190, 90))  # top right
        pygame.draw.ellipse(screen, (92, 64, 51), (200, 700, 190, 90))  # bottom left
        pygame.draw.ellipse(screen, (92, 64, 51), (400, 550, 190, 90))  # top middle
        if display_tick and tick_frame_count < tick_duration:
            tick_rect.center = cake_card.rect.center
            screen.blit(tick_image, tick_rect)
            tick_frame_count += 1

        cake_card.draw(screen)
        other_card.draw(screen)
        extra_card.draw(screen)
        third_card.draw(screen)
        screen.blit(text_surface, (800, 50))

        pygame.display.flip()

    # Delay before the next round or end of the game
    pygame.time.delay(2000)

#------------------------------------------------------------------------------------#



pygame.quit()
sys.exit()
