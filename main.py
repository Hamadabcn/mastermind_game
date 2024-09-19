import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 800  # Screen size
ROWS, COLS = 10, 4  # Number of rows and columns for guesses
SQUARE_SIZE = 50  # Size of each color square
PADDING = 15  # Padding between squares
TOP_PADDING = 160  # Space at the top for instructions and title
BUTTON_PADDING = 20  # Space between color selection buttons

# Define colors with their respective RGB values
COLORS = {
    "R": (255, 0, 0),  # Red
    "G": (0, 255, 0),  # Green
    "B": (0, 0, 255),  # Blue
    "Y": (255, 255, 0),  # Yellow
    "W": (255, 255, 255),  # White
    "O": (255, 165, 0)  # Orange
}
TRIES = 10  # Maximum number of guesses allowed
CODE_LENGTH = 4  # Length of the secret code

# Set up the screen for the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")  # Title of the window

# Define fonts for rendering text
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)


def draw_text(text, x, y, color=(0, 0, 0), font=font):
    """Render text at the specified position."""
    img = font.render(text, True, color)  # Create text image
    screen.blit(img, (x, y))  # Draw text on the screen


def draw_text_with_outline(text, x, y, color=(255, 255, 255), outline_color=(0, 0, 0), font=font):
    """Render text with an outline for better visibility."""
    outline = font.render(text, True, outline_color)  # Draw outline
    # Draw outline in 4 directions
    screen.blit(outline, (x - 1, y - 1))
    screen.blit(outline, (x + 1, y - 1))
    screen.blit(outline, (x - 1, y + 1))
    screen.blit(outline, (x + 1, y + 1))
    img = font.render(text, True, color)  # Draw main text
    screen.blit(img, (x, y))  # Draw main text on the screen


def draw_board(guesses):
    """Draw the game board showing previous guesses."""
    for row in range(ROWS):
        y = row * (SQUARE_SIZE + PADDING) + TOP_PADDING  # Calculate vertical position
        draw_text(f"{row + 1}.", 10, y + 10, color=(0, 0, 0), font=small_font)  # Draw row number
        for col in range(COLS):
            x = col * (SQUARE_SIZE + PADDING) + 50  # Calculate horizontal position
            pygame.draw.rect(screen, (200, 200, 200), (x, y, SQUARE_SIZE, SQUARE_SIZE))  # Draw square
            # Draw the color if a guess exists in that row
            if row < len(guesses):
                color = COLORS[guesses[row][col]]
                pygame.draw.circle(screen, color, (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)


def draw_feedback(feedback):
    """Draw the feedback area to display the results of guesses."""
    feedback_box_y = TOP_PADDING  # Y position for the feedback box
    feedback_height = 30  # Height for each feedback entry
    # Draw feedback background rectangle
    pygame.draw.rect(screen, (200, 200, 200), (400, feedback_box_y, 380, 320))  # Background for feedback

    # Feedback title at the top of the feedback box
    draw_text_with_outline("You Have 10 Tries...", 410, feedback_box_y + 10, (200, 200, 200), font=small_font)

    # Draw feedback information for each guess
    for row in range(len(feedback)):
        correct_pos, incorrect_pos = feedback[row]  # Unpack feedback data
        feedback_text = f"Guess {row + 1}: Correct: {correct_pos} | Incorrect: {incorrect_pos}"
        draw_text(feedback_text, 410, feedback_box_y + 30 + row * feedback_height, color=(0, 0, 0), font=small_font)


def draw_color_buttons():
    """Draw color selection buttons for the user to choose from."""
    buttons = []
    x_offset = 50 + (COLS * (SQUARE_SIZE + PADDING)) + BUTTON_PADDING  # Positioning buttons next to guess boxes
    for i, color in enumerate(COLORS):
        y = TOP_PADDING + (i * (SQUARE_SIZE + BUTTON_PADDING))  # Arrange buttons vertically
        pygame.draw.rect(screen, COLORS[color], (x_offset, y, SQUARE_SIZE, SQUARE_SIZE))  # Draw color button
        buttons.append((color, pygame.Rect(x_offset, y, SQUARE_SIZE, SQUARE_SIZE)))  # Save button data
    return buttons


def generate_code():
    """Generate a random code for the player to guess."""
    return [random.choice(list(COLORS.keys())) for _ in range(CODE_LENGTH)]  # Randomly select colors for the code


def check_code(guess, real_code):
    """Check the player's guess against the actual code and return feedback."""
    color_counts = {}  # Dictionary to count occurrences of each color
    correct_pos = 0  # Count of correct colors in the correct position
    incorrect_pos = 0  # Count of correct colors in incorrect positions

    # Count the occurrences of each color in the actual code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Check for correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1  # Increment count for correct positions
            color_counts[guess_color] -= 1  # Reduce count since this color is correctly guessed

    # Check for incorrect positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1  # Increment count for correct color but incorrect position
            color_counts[guess_color] -= 1  # Reduce count since this color is accounted for

    return correct_pos, incorrect_pos  # Return feedback counts


def draw_reset_button(hovered):
    """Draw the reset button at the top of the screen."""
    color = (0, 255, 0) if hovered else (0, 200, 0)  # Change color on hover
    reset_button = pygame.Rect(WIDTH - 150, 20, 120, 40)  # Create the button rectangle
    pygame.draw.rect(screen, color, reset_button, border_radius=5)  # Draw the button rectangle
    draw_text("Reset Game", WIDTH - 140, 30, (255, 255, 255), small_font)  # Draw button text
    return reset_button  # Return the button rectangle for collision detection


def main():
    """Main game loop."""
    code = generate_code()  # Generate the secret code
    guesses = []  # List to store the player's guesses
    feedback = []  # List to store feedback for each guess
    current_guess = []  # List to store the current guess being built

    running = True  # Game loop control
    while running:
        screen.fill((75, 75, 75))  # Fill background with a gray color

        # Instructions and Title
        draw_text_with_outline("Mastermind Game", 10, 10, font=pygame.font.SysFont(None, 48))  # Title
        draw_text_with_outline("Guess the 4-color code using R, G, B, Y, W, O.", 10, 60, font=small_font)  # Instructions
        draw_text_with_outline(
            "Click the colors on the right to select. Press Enter after selecting 4 colors. You have 10 tries good luck!", 10, 80,
            font=small_font)  # More instructions
        draw_text_with_outline(f"Tries left: {TRIES - len(guesses)}", 10, 120)  # Show tries left

        # Draw the game board with previous guesses
        draw_board(guesses)

        # Draw feedback on the right side for previous guesses
        draw_feedback(feedback)

        # Draw color selection buttons on the right side for the player to choose
        color_buttons = draw_color_buttons()

        # Show the current guess being built below the feedback box
        if current_guess:
            draw_text_with_outline(f"Current Guess: {' '.join(current_guess)}", 410, 500)

        # Draw the reset button at the top of the screen
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
        reset_hovered = pygame.Rect(WIDTH - 150, 20, 120, 40).collidepoint(mouse_pos)  # Check if hovered
        reset_button = draw_reset_button(reset_hovered)  # Draw the reset button

        # End game messages if the player has exhausted tries or guessed correctly
        if len(guesses) >= TRIES:  # Check if the player has exhausted their tries
            draw_text_with_outline(f"You lost! The code was: {' '.join(code)}", 500, HEIGHT - 80)  # Display losing message
        elif len(guesses) > 0 and guesses[-1] == code:  # Check if the last guess was correct
            draw_text_with_outline("Congratulations! You guessed the code!", 200, HEIGHT - 80)  # Display winning message

        pygame.display.flip()  # Update the display with the drawn content

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit event
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button pressed
                for color, rect in color_buttons:  # Check for clicks on color buttons
                    if rect.collidepoint(event.pos):  # If button is clicked
                        if len(current_guess) < CODE_LENGTH:  # Ensure guess is not too long
                            current_guess.append(color)  # Add selected color to current guess
                if reset_button.collidepoint(event.pos):  # Check if reset button is clicked
                    code = generate_code()  # Generate new code
                    guesses = []  # Clear previous guesses
                    feedback = []  # Clear previous feedback
                    current_guess = []  # Clear current guess
            elif event.type == pygame.KEYDOWN:  # Key pressed
                if event.key == pygame.K_RETURN and len(current_guess) == CODE_LENGTH:  # Check for Enter key
                    guesses.append(current_guess)  # Save current guess
                    correct_pos, incorrect_pos = check_code(current_guess, code)  # Check guess against code
                    feedback.append((correct_pos, incorrect_pos))  # Save feedback for the guess
                    current_guess = []  # Clear current guess for next input

    pygame.quit()  # Quit Pygame when the game loop ends


if __name__ == "__main__":
    main()  # Start the game
