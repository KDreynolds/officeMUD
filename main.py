import tcod
import tcod.event
import time
import tcod.console

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TITLE = "H@x0r"

def handle_main_menu(event):
    if isinstance(event, tcod.event.KeyDown):
        if event.sym == tcod.event.KeySym.RETURN and event.mod & tcod.event.KMOD_ALT:
            # Alt+Enter: toggle fullscreen
            return {'fullscreen': True}
        elif event.sym == tcod.event.KeySym.ESCAPE:
            # Exit the game
            return {'exit': True}
        elif event.sym == tcod.event.KeySym.UP:
            # Move selection up
            return {'move': -1}
        elif event.sym == tcod.event.KeySym.DOWN:
            # Move selection down
            return {'move': 1}
        elif event.sym == tcod.event.KeySym.RETURN:
            # Confirm selection
            return {'select': True}
    return {}

def display_main_menu(console, current_selection):
    options = ['New Game', 'Options', 'Quit']
    console.clear()
    # Calculate the center coordinates
    title_x = (SCREEN_WIDTH - len(TITLE)) // 2
    title_y = SCREEN_HEIGHT // 2 - 5

    console.print(x=title_x, y=title_y, string=TITLE, fg=(255, 255, 255))

    for i, option in enumerate(options):
        option_x = (SCREEN_WIDTH - len(option)) // 2
        option_y = SCREEN_HEIGHT // 2 + i

        if i == current_selection:
            fg_color = (0, 255, 0)
        else:
            fg_color = (255, 255, 255)
        console.print(x=option_x, y=option_y, string=option, fg=fg_color)

def display_hacker_screen(console, context):
    console.clear(fg=(0, 255, 0), bg=(0, 0, 0))
    
    text = "Hello, World."
    delay = 0.1  # Delay between each character (in seconds)

    for i in range(len(text)):
        console.print(x=0, y=0, string=text[:i+1])
        context.present(console)  # Present after each character is printed
        time.sleep(delay)

    # Wait for a key press before returning to the main menu
    key_wait = True
    while key_wait:
        for event in tcod.event.get():
            if event.type == "KEYDOWN":
                key_wait = False
                break

def main():
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        title=TITLE,
        vsync=True,
    ) as context:
        console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        current_selection = 0

        while True:
            display_main_menu(console, current_selection)
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)
                action = handle_main_menu(event)

                move = action.get('move')
                select = action.get('select')
                exit = action.get('exit')

                if move:
                    current_selection = (current_selection + move) % len(['New Game', 'Options', 'Quit'])
                elif select:
                    print(f"Selection made: {current_selection}")  # Debugging line
                    if current_selection == 0:  # New Game
                        display_hacker_screen(console, context)
                    elif current_selection == 1:  # Options
                        pass  # Show options menu
                    elif current_selection == 2:  # Quit
                        return  # Exit the game
                elif exit:
                    return  # Exit the game

if __name__ == "__main__":
    main()