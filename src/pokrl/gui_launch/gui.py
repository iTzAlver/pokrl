# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
from tkinter import Tk, LabelFrame, Label, Entry, ttk, END, scrolledtext, filedialog, Button
import numpy as np
from PIL import Image, ImageTk
from pokrl import CoreGame
from ..__special__ import __gui_cards_img__
C2IN_P = {0: 'spades', 1: 'clubs', 2: 'diamonds', 3: 'hearts'}
C2IN_N = {2: 2, 3: 3, 4: 4, 5: 5, 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'jack', 12: 'queen', 13: 'king',
          14: 'ace'}


def gui() -> None:
    root_node = Tk()
    MainWindow(root_node)
    root_node.configure()
    root_node.mainloop()
    return


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("PokRL - GUI")
        self.master.geometry('715x810')
        self.master.minsize(620, 810)
        self.master.maxsize(1290, 810)
        self.windowsize = '620x810'
        # -------------------------------------------------------------------------------------------------------------
        #                       VARIABLES
        # -------------------------------------------------------------------------------------------------------------
        self.core_game = CoreGame()
        self.player_hands = None
        # -------------------------------------------------------------------------------------------------------------
        #                       Interface (IF)
        # -------------------------------------------------------------------------------------------------------------
        self.action_lf = LabelFrame(self.master, width=190, height=135)
        self.action_lf.place(x=5, y=5)

        action_label = Label(self.action_lf, text='TAKE ACTIONS')
        action_label.place(x=42, y=8)

        action_shuffle = Button(self.action_lf, text='Shuffle', command=self.shuffle)
        action_shuffle.place(x=5, y=35)

        get_hands = Button(self.action_lf, text='Give cards', command=self.hands)
        get_hands.place(x=80, y=35)

        get_flop = Button(self.action_lf, text='Flop', command=self.flop, width=3)
        get_flop.place(x=5, y=65)

        get_turn = Button(self.action_lf, text='Turn', command=self.turn, width=3)
        get_turn.place(x=65, y=65)

        get_river = Button(self.action_lf, text='River', command=self.river, width=3)
        get_river.place(x=125, y=65)

        get_winner = Button(self.action_lf, text='Get the winner', command=self.winner, width=18)
        get_winner.place(x=5, y=95)

        self.if_lf = LabelFrame(self.master, width=705, height=660)
        self.if_lf.place(x=5, y=145)

        self.p0_c0 = None
        self.p0_c1 = None
        self.p1_c0 = None
        self.p1_c1 = None
        self.p2_c0 = None
        self.p2_c1 = None
        self.p3_c0 = None
        self.p3_c1 = None
        self.p4_c0 = None
        self.p4_c1 = None
        self.p5_c0 = None
        self.p5_c1 = None
        self.p6_c0 = None
        self.p6_c1 = None
        self.p7_c0 = None
        self.p7_c1 = None
        self.p8_c0 = None
        self.p8_c1 = None
        self.c_flop0 = None
        self.c_flop1 = None
        self.c_flop2 = None
        self.c_turn = None
        self.c_river = None
        self.p0_c0_img = None
        self.p0_c1_img = None
        self.p1_c0_img = None
        self.p1_c1_img = None
        self.p2_c0_img = None
        self.p2_c1_img = None
        self.p3_c0_img = None
        self.p3_c1_img = None
        self.p4_c0_img = None
        self.p4_c1_img = None
        self.p5_c0_img = None
        self.p5_c1_img = None
        self.p6_c0_img = None
        self.p6_c1_img = None
        self.p7_c0_img = None
        self.p7_c1_img = None
        self.p8_c0_img = None
        self.p8_c1_img = None
        self.c_flop0_img = None
        self.c_flop1_img = None
        self.c_flop2_img = None
        self.c_turn_img = None
        self.c_river_img = None
        self.c_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.c_c0.place(x=35, y=520)
        self.c_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.c_c1.place(x=45, y=530)
        self.ph = list()
        self.th = list()
        self.pi = list()
        self.shuffle()

    def shuffle(self):
        self.p0_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p0_c0.place(x=5, y=175)
        self.p0_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p0_c1.place(x=5 + 72, y=175)

        self.p1_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p1_c0.place(x=5, y=5)
        self.p1_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p1_c1.place(x=5 + 72, y=5)

        self.p2_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p2_c0.place(x=230 + 90 / 2, y=5)
        self.p2_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p2_c1.place(x=230 + 72 + 90 / 2, y=5)

        self.p3_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p3_c0.place(x=460 + 90, y=5)
        self.p3_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p3_c1.place(x=460 + 90 + 72, y=5)

        self.p4_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p4_c0.place(x=460 + 90, y=175)
        self.p4_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p4_c1.place(x=460 + 72 + 90, y=175)

        self.p5_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p5_c0.place(x=460 + 90, y=345)
        self.p5_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p5_c1.place(x=460 + 72 + 90, y=345)

        self.p6_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p6_c0.place(x=460 + 90, y=550)
        self.p6_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p6_c1.place(x=460 + 72 + 90, y=550)

        self.p7_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p7_c0.place(x=230 + 90 / 2, y=550)
        self.p7_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p7_c1.place(x=230 + 72 + 90 / 2, y=550)

        self.p8_c0 = LabelFrame(self.if_lf, width=70, height=100)
        self.p8_c0.place(x=5, y=345)
        self.p8_c1 = LabelFrame(self.if_lf, width=70, height=100)
        self.p8_c1.place(x=5 + 72, y=345)

        self.c_flop0 = LabelFrame(self.if_lf, width=70, height=100)
        self.c_flop0.place(x=175, y=320)
        self.c_flop1 = LabelFrame(self.if_lf, width=70, height=100)
        self.c_flop1.place(x=175 + 72, y=320)
        self.c_flop2 = LabelFrame(self.if_lf, width=70, height=100)
        self.c_flop2.place(x=175 + 144, y=320)
        self.c_turn = LabelFrame(self.if_lf, width=70, height=100)
        self.c_turn.place(x=175 + 216, y=320)
        self.c_river = LabelFrame(self.if_lf, width=70, height=100)
        self.c_river.place(x=175 + 288, y=320)

        self.ph = [(self.p0_c0, self.p0_c1),
                   (self.p1_c0, self.p1_c1),
                   (self.p2_c0, self.p2_c1),
                   (self.p3_c0, self.p3_c1),
                   (self.p4_c0, self.p4_c1),
                   (self.p5_c0, self.p5_c1),
                   (self.p6_c0, self.p6_c1),
                   (self.p7_c0, self.p7_c1),
                   (self.p8_c0, self.p8_c1)]

        self.pi = [[self.p0_c0_img, self.p0_c1_img],
                   [self.p1_c0_img, self.p1_c1_img],
                   [self.p2_c0_img, self.p2_c1_img],
                   [self.p3_c0_img, self.p3_c1_img],
                   [self.p4_c0_img, self.p4_c1_img],
                   [self.p5_c0_img, self.p5_c1_img],
                   [self.p6_c0_img, self.p6_c1_img],
                   [self.p7_c0_img, self.p7_c1_img],
                   [self.p8_c0_img, self.p8_c1_img]]

        self.th = [self.c_flop0, self.c_flop1, self.c_flop2, self.c_turn, self.c_river]

        self.core_game.shuffle_deck()

    def hands(self):
        self.player_hands = self.core_game.get_cards()
        for hand, p_label, pi in zip(self.player_hands, self.ph, self.pi):
            pi[0] = self.__get_img(hand[0])
            pi[1] = self.__get_img(hand[1])
            self.label_img0 = Label(p_label[0], image=pi[1])
            self.label_img0.image = pi[0]
            self.label_img1 = Label(p_label[1], image=pi[1])
            self.label_img1 = pi[1]
            self.label_img0.pack()
            self.label_img1.pack()


    def flop(self):
        self.core_game.flop()

    def turn(self):
        self.core_game.turn()

    def river(self):
        self.core_game.river()

    def winner(self):
        self.core_game.get_winner(self.player_hands)

    @staticmethod
    def __get_img(card: np.ndarray):
        number = C2IN_N[int(card[1])]
        color = C2IN_P[int(card[0])]
        card_name = f'{number}_of_{color}'
        if 'jack' in card_name or 'queen' in card_name or 'king' in card_name:
            card_name += '2'
        card_path = f"{__gui_cards_img__}{card_name}.png"
        img = Image.open(card_path)
        img1 = img.resize((70, 100))
        return img1
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
