import tcod

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TITLE = "Office Escape MUD"

def handle_main_menu(key):
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        return {'fullscreen': True}
    elif key.vk == tcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    elif key.vk == tcod.KEY_UP:
        # Move selection up
        return {'move': -1}
    elif key.vk == tcod.KEY_DOWN:
        # Move selection down
        return {'move': 1}
    elif key.vk == tcod.KEY_ENTER:
        # Confirm selection
        return {'select': True}
    return {}

def display_main_menu(console, current_selection):
    options = ['New Game', 'Options', 'Quit']

    # Calculate the center coordinates
    title_x = (SCREEN_WIDTH - len(TITLE)) // 2
    title_y = SCREEN_HEIGHT // 2 - 5

    tcod.console_set_default_foreground(console, tcod.white)
    tcod.console_print(console, title_x, title_y, TITLE)

    for i, option in enumerate(options):
        option_x = (SCREEN_WIDTH - len(option)) // 2
        option_y = SCREEN_HEIGHT // 2 + i

        if i == current_selection:
            tcod.console_set_default_foreground(console, tcod.green)
        else:
            tcod.console_set_default_foreground(console, tcod.white)
        tcod.console_print(console, option_x, option_y, option)

def main():
    # Initialize the libtcod console
    #tcod.console_set_custom_font("arial10x10.png", tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, False)

    console = tcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    current_selection = 0

    # Set up the game loop
    while True:
        # Clear the console
        tcod.console_clear(console)

        # Display the main menu
        display_main_menu(console, current_selection)

        # Blit the console to the root console
        tcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

        # Flush the console
        tcod.console_flush()

        # Handle user input
        key = tcod.console_wait_for_keypress(True)
        action = handle_main_menu(key)

        move = action.get('move')
        select = action.get('select')
        exit = action.get('exit')

        if move:
            current_selection = (current_selection + move) % 3
        elif select:
            if current_selection == 0:  # New Game
                # Start a new game
                pass
            elif current_selection == 1:  # Options
                # Show options menu
                pass
            elif current_selection == 2:  # Quit
                # Exit the game
                break
        elif exit:
            # Exit the game
            break

if __name__ == "__main__":
    main()