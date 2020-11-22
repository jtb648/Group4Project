import gi
from Player import Player
from PlayerType import PlayerType
from Game import Game
from PieceSet import PieceSet
from Timer import Timer
from Colours import ColourCodes, ColourBoardCodes, ColourOffset, COLOUR_STRING_LOOK_UP_TABLE, COLOUR_BOARD_STRING_LOOK_UP_TABLE
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
from GameType import GameType

resume = True

class TheWindow(Gtk.Window):
        def __init__(self):
                Gtk.Window.__init__(self, title="Main Menu")
                self.set_border_width(70)
                self.set_position(Gtk.WindowPosition.CENTER)
                col = Gdk.Color(2000, 6000, 200)  # dark green
                self.modify_bg(Gtk.StateType.NORMAL, col)

                self.main_box = MainMenuBox()#Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
                self.main_box.play_button.connect("clicked", self.main_play_clicked)
                if resume:
                        self.main_box.resume_button.connect("clicked", self.main_resume_clicked)


                self.game_choice_box = GameChoiceBox()
                self.game_choice_box.chess_button.connect("clicked", self.game_choice_chess_clicked)
                self.game_choice_box.checkers_button.connect("clicked", self.game_choice_checkers_clicked)
                self.game_choice_box.back_button.connect("clicked", self.game_choice_back_clicked)


                self.player_type = PlayerTypeBox()
                self.player_type.single_button.connect("clicked", self.player_type_single_clicked)
                self.player_type.multiplayer_button.connect("clicked", self.player_type_multi_clicked)
                self.player_type.back_button.connect("clicked", self.player_type_back_clicked)


                self.customization = CustomizationGrid()
                self.customization.back_button.connect("clicked", self.customization_back_clicked)
                self.customization.start_button.connect("clicked", self.customization_start_clicked)


                self.grid = Gtk.Grid()
                self.grid.attach(self.main_box,0,0,1,1)
                self.grid.attach(self.game_choice_box,0,0,1,1)
                self.grid.attach(self.player_type,0,0,1,1)
                self.grid.attach(self.customization,0,0,1,1)

                self.game_choice_box.hide()
                self.player_type.hide()
                self.customization.hide()
                self.add(self.grid)
                self.main_box.show()

        
                self.connect("destroy", Gtk.main_quit)  # fixed the exit stalling problem

        def main_play_clicked(self, button):
                print('Play was chosen')
                self.main_box.hide()
                self.game_choice_box.show()

        def main_resume_clicked(self, button):
                print('This should go to resumed game') 
                return

        def game_choice_chess_clicked(self, button):
                print('Chess was chosen')  # put next window here
                self.game_type = GameType.CHESS
                self.game_choice_box.hide()
                self.player_type.show()

        def game_choice_checkers_clicked(self, button):
                print('Checkers was chosen')  # put next window here
                self.game_type = GameType.CHECKERS
                self.game_choice_box.hide()
                self.player_type.show()

        def game_choice_back_clicked(self, button):
                print("This should go back to Main Menu Window")
                self.game_choice_box.hide()
                self.main_box.show()

        def player_type_single_clicked(self, button):
                print('Single Player was chosen')  # put next window here
                self.player_type.hide()
                self.customization.show()


        def player_type_multi_clicked(self, button):
                print('Multi Player was chosen')  # put next window here
                self.player_type.hide()
                self.customization.show()


        def player_type_back_clicked(self, button):
                print("This should go back to Game Choice Window")
                self.player_type.hide()
                self.game_type.show()

        def customization_back_clicked(self, button):
                print("This should go back to Game Choice Window")
                self.customization.hide()
                self.player_type.show()

        def customization_start_clicked(self, button):
                print("This should go to Board Window")
                #board = BoardWindow(self.__game, self.__game_type)
                board = BoardWindow("Test", "multiplayer")
                board.show_all()







class MainMenuBox(Gtk.Box):
        def __init__(self):
                Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL, spacing=10)
                # self.add(b)
                self.play_button = Gtk.Button.new_with_label("Play")
                #chess_button.connect("clicked", self.play_clicked)
                self.play_button.set_property("width-request", 300)
                self.play_button.set_property("height-request", 100)
                self.pack_start(self.play_button, True, True, 0)
                
                if resume:
                        self.resume_button = Gtk.Button.new_with_label("Resume")
                        #checkers_button.connect("clicked", self.resume_clicked)
                        self.resume_button.set_property("width-request", 300)
                        self.resume_button.set_property("height-request", 100)
                        self.pack_start(self.resume_button, True, True, 0)
                
                back_button = Gtk.Button.new_with_mnemonic("_Exit")
                back_button.connect("clicked", self.exit_clicked)
                self.pack_start(back_button, True, True, 0)


                
        def exit_clicked(self, button):
                print("This should exit")
                Gtk.main_quit()


class GameChoiceBox(Gtk.Box):
        def __init__(self):
                Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL, spacing=10)

                self.chess_button = Gtk.Button.new_with_label("Chess")
                self.chess_button.set_property("width-request", 300)
                self.chess_button.set_property("height-request", 100)
                self.pack_start(self.chess_button, True, True, 0)

                self.checkers_button = Gtk.Button.new_with_label("Checkers")
                self.checkers_button.set_property("width-request", 300)
                self.checkers_button.set_property("height-request", 100)
                self.pack_start(self.checkers_button, True, True, 0)

                self.back_button = Gtk.Button.new_with_label("Back")
                self.pack_start(self.back_button, True, True, 0)

                self.connect("destroy", Gtk.main_quit)  # fixed the exit stalling problem







class PlayerTypeBox(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.single_button = Gtk.Button.new_with_label("Single-Player")
        # single_button.get_style_context().add_class("suggested-action") changes button to blue
        self.single_button.set_property("width-request", 300)
        self.single_button.set_property("height-request", 100)
        self.pack_start(self.single_button, True, True, 0)

        self.multiplayer_button = Gtk.Button.new_with_label("Multi-Player")
        self.multiplayer_button.set_property("width-request", 300)
        self.multiplayer_button.set_property("height-request", 100)
        self.pack_start(self.multiplayer_button, True, True, 0)

        self.back_button = Gtk.Button.new_with_mnemonic("_Back")
        
        self.pack_start(self.back_button, True, True, 0)









class CustomizationGrid(Gtk.Grid):
    def __init__(self):#, game, game_type):
        #self.__game = game
        #self.__game_type = game_type

        Gtk.Grid.__init__(self)
        self.set_column_spacing(10)
        self.set_row_spacing(20)
        title = Gtk.Label()
        title.set_markup("<big>Customize your pieces and board!</big>")
        title.set_justify(Gtk.Justification.RIGHT)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 1.0, 1.0, 1.0))
        self.attach(title, 3, 0, 1, 1)

        label_piece = Gtk.Label()
        label_piece.set_markup("<b>Pieces</b>")
        # label_piece.set_justify(Gtk.Justification.CENTER)
        label_piece.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 1.0, 1.0, 1.0))
        self.attach(label_piece, 1, 1, 1, 1)

        label_board = Gtk.Label()
        label_board.set_markup("<b>Board</b>")
        label_board.set_justify(Gtk.Justification.CENTER)
        label_board.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 1.0, 1.0, 1.0))
        self.attach(label_board, 4, 1, 1, 1)

        x=0
        self.piece_radio_buttons = []
        self.piece_radio_buttons.append(Gtk.RadioButton.new_with_label(None, COLOUR_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_LIGHT] + " " + COLOUR_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_DARK]))
        x+=1
        while (x!=len(COLOUR_STRING_LOOK_UP_TABLE)):
                self.piece_radio_buttons.append(Gtk.RadioButton.new_with_label_from_widget(self.piece_radio_buttons[0], COLOUR_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_LIGHT] + " " + COLOUR_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_DARK]))
                x+=1
        x=0
        while (x!=len(COLOUR_STRING_LOOK_UP_TABLE)):
                self.attach(self.piece_radio_buttons[x],0,2+x,1,1)
                x+=1

        x=0
        self.board_radio_buttons = []
        self.board_radio_buttons.append(Gtk.RadioButton.new_with_label(None, COLOUR_BOARD_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_LIGHT] + " " + COLOUR_BOARD_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_DARK]))
        x+=1
        while (x!=len(COLOUR_BOARD_STRING_LOOK_UP_TABLE)):
                self.board_radio_buttons.append(Gtk.RadioButton.new_with_label_from_widget(self.board_radio_buttons[0], COLOUR_BOARD_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_LIGHT] + " " + COLOUR_BOARD_STRING_LOOK_UP_TABLE[x][ColourOffset.OFFSET_DARK]))
                x+=1
        x=0
        while (x!=len(COLOUR_BOARD_STRING_LOOK_UP_TABLE)):
                self.attach(self.board_radio_buttons[x],3,2+x,1,1)
                x+=1

        

        self.back_button = Gtk.Button.new_with_label("Back")
        self.attach(self.back_button, 0, 8, 1, 1)

        self.start_button = Gtk.Button.new_with_label("Start")
        self.attach(self.start_button, 4, 8, 1, 1)


    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print(name, "was turned", state)



class BoardGrid(Gtk.Grid):
    def __init__(self, game, game_type):
        Gtk.Window.__init__(self, title=game + " " + game_type)
        self.__game = game
        self.set_border_width(200)
        self.set_position(Gtk.WindowPosition.CENTER)
        col = Gdk.Color(2000, 6000, 200)  # dark green
        self.modify_bg(Gtk.StateType.NORMAL, col)
        grid = Gtk.Grid()
        self.add(grid)

        row_1_0 = Gtk.Button(label=" ")
        row_1_0 = Gtk.Button(label=" ")

        single_button = Gtk.Button.new_with_label("Single-Player")
        single_button.connect("clicked", self.single_clicked)
        single_button.set_property("width-request", 300)
        single_button.set_property("height-request", 100)
        # flowbox.pack_start(single_button, True, True, 0)

        # look at EventBox() to see if that works for this

        self.connect("destroy", Gtk.main_quit)

    def single_clicked(self, button):
        print('Single Player was chosen')  # put next window here
        customization = CustomizationWindow(self.__game, "Single-Player")
        customization.show_all()
        self.hide()

    def multi_clicked(self, button):
        print('Multi Player was chosen')  # put next window here
        customization = CustomizationWindow(self.__game, "Multi-Player")
        customization.show_all()
        self.hide()

    def back_clicked(self, button):
        print("This should go back to Game Choice Window")
        game_type = GameChoiceWindow()
        game_type.show_all()
        self.hide()


class HowToPlayMenu(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="How to Play ")
        self.set_border_width(50)
        self.set_position(Gtk.WindowPosition.CENTER)
        col = Gdk.Color(2000, 6000, 200)  # dark green
        self.modify_bg(Gtk.StateType.NORMAL, col)
        player_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.add(player_box)
        # if we want there to be text in the window

        # scrolled = Gtk.ScrolledWindow()
        # scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        label = Gtk.Label()
        label.set_markup("<a href='https://www.chess.com/learn-how-to-play-chess'"
                         "title='Click to find out more'>Chess Rules</a>")

        label1 = Gtk.Label()
        label1.set_markup("<a href='https://www.fgbradleys.com/rules/Checkers.pdf'"
                          "title='Click to find out more'>Checkers Rules</a>")
        player_box.add(label)
        player_box.add(label1)

        self.connect("destroy", Gtk.main_quit)  # fixed the exit stalling problem


class PlayAgainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Play Again?")
        self.set_border_width(70)
        self.set_position(Gtk.WindowPosition.CENTER)
        col = Gdk.Color(2000, 6000, 200)  # dark green
        self.modify_bg(Gtk.StateType.NORMAL, col)
        # b = Button()
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)
        # self.add(b)
        chess_button = Gtk.Button.new_with_label("Play Again")
        chess_button.connect("clicked", self.play_clicked)
        chess_button.set_property("width-request", 300)
        chess_button.set_property("height-request", 100)
        main_box.pack_start(chess_button, True, True, 0)

        chess_button = Gtk.Button.new_with_label("Main Menu")
        chess_button.connect("clicked", self.main_menu_clicked)
        chess_button.set_property("width-request", 300)
        chess_button.set_property("height-request", 100)
        main_box.pack_start(chess_button, True, True, 0)

        back_button = Gtk.Button.new_with_mnemonic("_Exit")
        back_button.connect("clicked", self.exit_clicked)
        main_box.pack_start(back_button, True, True, 0)

        self.connect("destroy", Gtk.main_quit)  # fixed the exit stalling problem

    def play_clicked(self, button):
        print('Play was chosen')
        game_type = GameChoiceWindow()  # do we want it to go back to the board or back through menus?
        game_type.show_all()
        self.hide()

    def main_menu_clicked(self, button):
        print('This should go to resumed game')
        main_menu = MainMenuWindow()
        main_menu.show_all()
        self.hide()

    def exit_clicked(self, button):
        print("This should exit")
        Gtk.main_quit()


"""class Button(Gtk.Button):
    def __init__(self):
        super().Gtk.Button.new_with_label("Play")
        print("b")"""

if __name__ == "__main__":
    win = TheWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
