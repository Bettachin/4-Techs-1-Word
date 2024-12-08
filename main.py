from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.clock import Clock

# Define puzzles
puzzles = [
    {"level": 1,
     "images": ["images/Computer1.jpg", "images/Computer2.jpg", "images/Computer3.jpg", "images/Computer4.jpg"],
     "answer": "COMPUTER", "hint": "A device used to compute."},
    {"level": 2,
     "images": ["images/Internet1.jpeg", "images/Internet2.jpeg", "images/Internet3.jpeg", "images/Internet4.jpeg"],
     "answer": "INTERNET", "hint": "Connects the world through \na global network."},
    {"level": 3, "images": ["images/Python1.jpg", "images/Python2.jpg", "images/Python3.jpg", "images/Python4.jpg"],
     "answer": "PYTHON", "hint": "Popular programming language."},
    {"level": 4, "images": ["images/Dart1.jpg", "images/Dart2.jpg", "images/Dart3.jpg", "images/Dart4.jpg"],
     "answer": "DART", "hint": "Google's programming language \nfor building mobile apps."},
    {"level": 5,
     "images": ["images/Database1.jpg", "images/Database2.jpg", "images/Database3.jpg", "images/Database4.jpg"],
     "answer": "DATABASE", "hint": "Used to store and manage structured data."},
    {"level": 6, "images": ["images/Binary1.jpg", "images/Binary2.jpg", "images/Binary3.jpg", "images/Binary4.jpg"],
     "answer": "BINARY", "hint": "The language of computers, \nmade up of 1s and 0s."},
    {"level": 7, "images": ["images/Console1.jpg", "images/Console2.jpg", "images/Console3.jpg", "images/Console4.jpg"],
     "answer": "CONSOLE", "hint": "A tool for interacting \nwith the computer directly."},
    {"level": 8, "images": ["images/Crypto1.jpg", "images/Crypto2.jpg", "images/Crypto3.jpg", "images/Crypto4.jpg"],
     "answer": "CRYPTO", "hint": "Refers to encrypted digital \nassets like Bitcoin."},
    {"level": 9, "images": ["images/Website1.jpg", "images/Website2.jpg", "images/Website3.jpg", "images/Website4.jpg"],
     "answer": "WEBSITE", "hint": "A collection of web pages \nhosted on the internet."},
    {"level": 10, "images": ["images/Domain1.jpg", "images/Domain2.jpg", "images/Domain3.jpg", "images/Domain4.jpg"],
     "answer": "DOMAIN", "hint": "The unique address of a website."},
    {"level": 11,
     "images": ["images/Language1.jpg", "images/Language2.jpg", "images/Language3.jpg", "images/Language4.jpg"],
     "answer": "LANGUAGE", "hint": "A system for coding and communication."},
    {"level": 12, "images": ["images/Virus1.jpg", "images/Virus2.jpg", "images/Virus3.jpg", "images/Virus4.jpg"],
     "answer": "VIRUS", "hint": "A malicious program that\n can harm systems."},
    {"level": 13, "images": ["images/Programming1.jpg", "images/Programming2.jpg", "images/Programming3.jpg",
                             "images/Programming4.jpg"],
     "answer": "PROGRAMMING", "hint": "The process of writing \nsoftware instructions."},
    {"level": 14,
     "images": ["images/Processor1.jpg", "images/Processor2.jpg", "images/Processor3.jpg", "images/Processor4.jpg"],
     "answer": "CPU", "hint": "The brain of the computer \nthat processes instructions."},
    {"level": 15,
     "images": ["images/Security1.jpg", "images/Security2.jpg", "images/Security3.jpg", "images/Security4.jpg"],
     "answer": "SECURITY", "hint": "Protects systems from \nunauthorized access."},
    {"level": 16,
     "images": ["images/Storage1.jpg", "images/Storage2.jpg", "images/Storage3.jpg", "images/Storage4.jpg"],
     "answer": "STORAGE", "hint": "Where data is saved \nfor future use."},
    {"level": 17,
     "images": ["images/Networking1.jpg", "images/Networking2.jpg", "images/Networking3.jpg", "images/Networking4.jpg"],
     "answer": "NETWORKING", "hint": "Connecting computers to\n share resources and data."}

]

# Create a draggable image class using DragBehavior
class DraggableImage(DragBehavior, Image):
    pass

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add background image
        background = Image(source="images/background.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        # Center layout for the StartScreen
        layout = BoxLayout(orientation="vertical", spacing=-10, padding=50)
        layout.size_hint = (None, None)
        layout.size = (400, 400)
        layout.pos_hint = {"center_x": 0.5, "center_y": 0.4}

        # Add the draggable game logo
        logo = DraggableImage(source="images/logo.png", size_hint=(None, None), size=(220, 220), pos_hint={"center_x": 0.5, "center_y": 0.7})
        layout.add_widget(logo)

        # Add image-based buttons
        start_button = Button(size_hint=(None, None), size=(250, 100), pos_hint={"center_x": 0.5, "center_y": 0.5},
                              background_normal="images/start_button.png", background_down="images/start_button.png")
        start_button.bind(on_press=self.start_game)
        layout.add_widget(start_button)

        self.music_button = Button(size_hint=(None, None), size=(230, 90), pos_hint={"center_x": 0.5, "center_y": 0.5},
                                   background_normal="images/mute.png", background_down="images/unmute.png")
        self.music_button.bind(on_press=self.toggle_music)
        layout.add_widget(self.music_button)

        exit_button = Button(size_hint=(None, None), size=(180, 80), pos_hint={"center_x": 0.5, "center_y": 0.3},
                             background_normal="images/exit_button.png", background_down="images/exit_button.png")
        exit_button.bind(on_press=App.get_running_app().stop)
        layout.add_widget(exit_button)

        # Add layout to the screen
        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = "game"

    def toggle_music(self, instance):
        app = App.get_running_app()
        if app.music_on:
            app.music.stop()
            self.music_button.background_normal = "images/unmute.png"
        else:
            app.music.play()
            self.music_button.background_normal = "images/mute.png"
        app.music_on = not app.music_on

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add background image
        background = Image(source="images/background.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        # Initial layout for the GameScreen using FloatLayout for flexible positioning
        self.layout = FloatLayout(size_hint=(None, None), size=(400, 600))  # Use FloatLayout here
        self.layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.add_widget(self.layout)

    def load_level(self, level):
        self.layout.clear_widgets()
        app = App.get_running_app()
        puzzle = next(p for p in puzzles if p["level"] == level)
        app.current_puzzle = puzzle

        # Create a GridLayout to arrange images in a 2x2 grid
        grid_layout = GridLayout(cols=2, rows=2, spacing=10, size_hint=(None, None), size=(300, 300))
        grid_layout.pos_hint = {"center_x": 0.565, "center_y": 0.68}  # Place images towards the top center

        # Add images to the grid
        for img_path in puzzle["images"]:
            img = Image(source=img_path, size_hint=(None, None), size=(120, 120))
            grid_layout.add_widget(img)

        # Add the grid layout to the main layout
        self.layout.add_widget(grid_layout)

        # Answer entry (TextInput) with position hints, below the images
        self.answer_entry = TextInput(
            hint_text="Enter your answer",
            font_size=20,
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            halign="center"  # Align the hint text to the center
        )

        self.layout.add_widget(self.answer_entry)

        # Buttons layout (Stacked vertically below the input field)
        button_layout = BoxLayout(orientation="vertical", size_hint=(None, None), height=80, spacing=-15)
        button_layout.pos_hint = {"center_x": 0.5,"center_y": 0.08}

        # Add image-based Submit button
        submit_button = Button(size_hint=(None, None), size=(220, 80), pos_hint={"center_x": 0.5},
                               background_normal="images/submit_button.png", background_down="images/submit_button.png")
        submit_button.bind(on_press=self.check_answer)
        button_layout.add_widget(submit_button)

        # Add image-based Hint button
        hint_button = Button(size_hint=(None, None), size=(200, 80), pos_hint={"center_x": 0.5},
                             background_normal="images/hint_button.png", background_down="images/hint_button.png")
        hint_button.bind(on_press=self.show_hint)
        button_layout.add_widget(hint_button)

        # Add image-based Back button
        back_button = Button(size_hint=(None, None), size=(200, 80), pos_hint={"center_x": 0.5},
                             background_normal="images/back_button.png", background_down="images/back_button.png")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', "start"))
        button_layout.add_widget(back_button)

        self.layout.add_widget(button_layout)

    def check_answer(self, instance):
        app = App.get_running_app()
        user_answer = self.answer_entry.text.strip().upper()
        puzzle = app.current_puzzle

        # Clear any previous 'Incorrect!' or 'Correct!' labels or GIFs
        for widget in self.layout.children:
            if isinstance(widget, Label):
                if widget.text == "Incorrect! Try Again!" or widget.text == "Correct! Well Done!":
                    self.layout.remove_widget(widget)
            if isinstance(widget, Image):
                if widget.source == "images/incorrect_animation.gif" or widget.source == "images/correct_animation.gif":
                    self.layout.remove_widget(widget)

        if user_answer == puzzle["answer"]:
            app.correct_sound.play()
            app.solved_levels.add(puzzle["level"])
            app.current_level += 1
            if app.current_level > len(puzzles):
                self.show_congratulations()
            else:
                self.load_level(app.current_level)

            # Display 'Correct!' message
            correct_label = Label(
                text="Correct! Well Done!",
                font_size=30,
                color=(0, 1, 0, 1),  # Green color for success message
                halign='center',
                valign='middle',
                size_hint=(None, None),
                size=(300, 50)
            )
            correct_label.pos_hint = {"center_x": 0.5, "center_y": 0.5}
            self.layout.add_widget(correct_label)

            # Add GIF for correct answer (Ensure the GIF file path is correct)
            correct_gif = Image(
                source="images/correct.gif",  # Path to your celebratory GIF
                size_hint=(None, None),
                size=(250, 250),
                pos_hint={"center_x": 0.5, "center_y": 0.7}  # Position the GIF below the message
            )
            self.layout.add_widget(correct_gif)

            # Optionally, remove the message and GIF after a few seconds:
            Clock.schedule_once(lambda dt: self.layout.remove_widget(correct_label), 2)  # Remove label after 5 seconds
            Clock.schedule_once(lambda dt: self.layout.remove_widget(correct_gif), 2)  # Remove GIF after 5 seconds

        else:
            app.incorrect_sound.play()

            # Display 'Incorrect!' message
            incorrect_label = Label(
                text="Incorrect! Try Again!",
                font_size=30,
                color=(1, 0, 0, 1),  # Red color for error message
                halign='center',
                valign='middle',
                size_hint=(None, None),
                size=(300, 50)
            )
            incorrect_label.pos_hint = {"center_x": 0.5, "center_y": 0.5}
            self.layout.add_widget(incorrect_label)

            # Add GIF for incorrect answer (Ensure the GIF file path is correct)
            incorrect_gif = Image(
                source="images/meme.gif",  # Path to your meme GIF
                size_hint=(None, None),
                size=(150, 150),
                pos_hint={"center_x": 0.5, "center_y": 0.65}  # Position the GIF below the message
            )
            self.layout.add_widget(incorrect_gif)

            # Optionally, you can remove the message and GIF after a few seconds:
            Clock.schedule_once(lambda dt: self.layout.remove_widget(incorrect_label),
                                4.2)  # Remove label after 5 seconds
            Clock.schedule_once(lambda dt: self.layout.remove_widget(incorrect_gif), 4.2)  # Remove GIF after 5 seconds

    def show_hint(self, instance):
        puzzle = App.get_running_app().current_puzzle
        hint_label = Label(text=f"Hint: {puzzle['hint']}", font_size=15, halign='center', valign='middle', size_hint=(None, None), size=(100, 50))
        hint_label.pos_hint = {"center_x": 0.5, "center_y": 0.48}

        self.layout.add_widget(hint_label)

    def show_congratulations(self):
        self.layout.clear_widgets()

        # Display "Congratulations" label
        congrat_label = Label(text="Congratulations!", font_size=30, halign='center', valign='middle',
                              size_hint=(None, None), size=(300, 50))
        congrat_label.pos_hint = {"center_x": 0.5, "center_y": 0.4}
        self.layout.add_widget(congrat_label)

        # Display "Thank you for playing" label
        thank_you_label = Label(text="Thank you for playing!", font_size=20, halign='center', valign='middle',
                                size_hint=(None, None), size=(300, 50))
        thank_you_label.pos_hint = {"center_x": 0.5, "center_y": 0.3}
        self.layout.add_widget(thank_you_label)

        # Display Exit button to close the game
        exit_button = Button(size_hint=(None, None), size=(200, 80), pos_hint={"center_x": 0.5, "center_y": 0.2},
                             background_normal="images/exit_button.png", background_down="images/exit_button.png")
        exit_button.bind(on_press=App.get_running_app().stop)  # Exit the game
        self.layout.add_widget(exit_button)

        # Display a GIF (Make sure the file path is correct)
        congrat_gif = Image(
            source="images/congrats.gif",  # Path to your GIF
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={"center_x": 0.5, "center_y": 0.6}  # Position the GIF
        )
        self.layout.add_widget(congrat_gif)

class GameApp(App):
    def build(self):
        self.music_on = True
        self.music = SoundLoader.load("music/background.mp3")
        self.correct_sound = SoundLoader.load("sounds/correct.wav")
        self.incorrect_sound = SoundLoader.load("sounds/incorrect.wav")
        self.music.loop = True
        self.music.play()

        self.current_level = 1
        self.solved_levels = set()
        self.current_puzzle = None

        sm = ScreenManager()
        sm.add_widget(StartScreen(name="start"))
        game_screen = GameScreen(name="game")
        sm.add_widget(game_screen)

        # Load first level when game starts
        sm.current = "start"
        game_screen.load_level(self.current_level)
        return sm


if __name__ == "__main__":
    GameApp().run()
#BugartMadeThisShit(sign)
#Abejuela Z.