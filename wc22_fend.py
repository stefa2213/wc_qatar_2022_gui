import tkinter
import tkinter.font as font
from tkinter import *
import PIL.Image
import customtkinter
from PIL import ImageTk, Image
import wc22_bend

# settings -----------------------------

window = customtkinter.CTk()
window.title('World Cup 2022 - Qatar')
window.geometry('1490x780')
window.iconbitmap('img_icon.ico')
window.attributes("-alpha", 0.9)

# insert bg wallpaper--------------------

fp1 = open("wc22wall_dark.jpg", "rb")
# fp2 = open("wc22_wall_other.jpg", "rb")

fp = fp1
image_wall = PIL.Image.open(fp)
resized_wall = image_wall.resize((2200, 1000))
photoimg = ImageTk.PhotoImage(resized_wall)
image_wall = Label(window, image=photoimg)
image_wall.place(x=-123, y=-5)

# ------------------------------------------

# window.configure(bg=bg_overall_GUI)

bg_overall_GUI = '#F7E0B3'
labfont = 'Helvetica 9 bold'
lab_rank_size = font.Font(size=11)
bg_lab_color = '#FAFAEB'
width_ent_sc = 2

bd_ent_sc = 3

col_lab_gr = '#96E4EF'
fg_color_teams = '#D3EFF3'
bg_ent_sc = '#EBEDEE'
cor_radius_std = 8

def create_lab_group():
    def inner(ro, name, col):
        lab_gr = customtkinter.CTkLabel(window, text=name, width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                        text_font=labfont, fg_color=(col_lab_gr), bg_color='black')

        lab_gr.grid(row=ro, columnspan=3, column=col, pady=10)

    inner(1, 'Group A', 1)
    inner(1, 'Group B', 7)
    inner(1, 'Group C', 13)
    inner(1, 'Group D', 18)

    inner(8, 'Group E', 1)
    inner(8, 'Group F', 7)
    inner(8, 'Group G', 13)
    inner(8, 'Group H', 18)


create_lab_group()

# bar of standings -----------------------------

bg_col_std = 'black'
fg_col_std = '#FEF9E7'

lab_bannerA = customtkinter.CTkLabel(window, text='#             TEAM                           MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerA.grid(row=2, column=0, columnspan=5, sticky=W)

lab_bannerE = customtkinter.CTkLabel(window, text='#             TEAM                           MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerE.grid(row=9, column=0, columnspan=5, sticky=W)

lab_bannerB = customtkinter.CTkLabel(window, text='   #              TEAM                          MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerB.grid(row=2, column=6, columnspan=5, sticky=W)

lab_bannerF = customtkinter.CTkLabel(window, text='   #              TEAM                          MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerF.grid(row=9, column=6, columnspan=5, sticky=W)

lab_bannerC = customtkinter.CTkLabel(window, text='   #             TEAM                               MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerC.grid(row=2, column=12, columnspan=5, sticky=W)

lab_bannerG = customtkinter.CTkLabel(window, text='   #             TEAM                               MP   GD    PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerG.grid(row=9, column=12, columnspan=5, sticky=W)

lab_bannerD = customtkinter.CTkLabel(window,
                                     text='   #             TEAM                                    MP    GD     PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerD.grid(row=2, column=18, columnspan=5, sticky=W)

lab_bannerH = customtkinter.CTkLabel(window,
                                     text='   #             TEAM                                    MP    GD     PTS',
                                     border=2, width=10, height=1, borderwidth=2, corner_radius=cor_radius_std,
                                     text_font=labfont,
                                     bg_color=bg_col_std, fg_color=(fg_col_std))
lab_bannerH.grid(row=9, column=18, columnspan=5, sticky=W)

# rank of teams---------------------
lab_color_place12 = '#23B125'
lab_color_place34 = '#F9DF5C'


def create_place():
    def inner12(txt, ro, col):
        no1 = customtkinter.CTkLabel(window, text=txt, text_font=labfont, bg_color=bg_col_std, width=15,
                                     fg_color=(lab_color_place12),
                                     height=20, corner_radius=cor_radius_std)
        no1.grid(row=ro, column=col, padx=2)
        no1['font'] = lab_rank_size

    def inner34(txt, ro, col):
        no1 = customtkinter.CTkLabel(window, text=txt, text_font=labfont, bg_color=bg_col_std, width=15,
                                     fg_color=(fg_col_std),
                                     height=20, corner_radius=cor_radius_std)
        no1.grid(row=ro, column=col, padx=2)
        no1['font'] = lab_rank_size

    inner12('1', 3, 0)
    inner12('1', 3, 6)
    inner12('1', 3, 12)
    inner12('1', 3, 18)
    inner12('1', 10, 0)
    inner12('1', 10, 6)
    inner12('1', 10, 12)
    inner12('1', 10, 18)
    #
    inner12('2', 4, 0)
    inner12('2', 4, 6)
    inner12('2', 4, 12)
    inner12('2', 4, 18)
    inner12('2', 11, 0)
    inner12('2', 11, 6)
    inner12('2', 11, 12)
    inner12('2', 11, 18)
    #
    inner34('3', 5, 0)
    inner34('3', 5, 6)
    inner34('3', 5, 12)
    inner34('3', 5, 18)
    inner34('3', 12, 0)
    inner34('3', 12, 6)
    inner34('3', 12, 12)
    inner34('3', 12, 18)

    inner34('4', 6, 0)
    inner34('4', 6, 6)
    inner34('4', 6, 12)
    inner34('4', 6, 18)
    inner34('4', 13, 0)
    inner34('4', 13, 6)
    inner34('4', 13, 12)
    inner34('4', 13, 18)


create_place()


def create_teams():
    def inner(name, ro, col):
        lab_team = customtkinter.CTkLabel(window, text=name, width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                          text_font=labfont, fg_color=(fg_color_teams), bg_color='black')
        lab_team.grid(row=ro, column=col, sticky=W, pady=1)
        lab_team['font'] = lab_rank_size

    # A
    inner('Qatar (QAT)', 3, 1)
    inner('Ecuador (ECU)', 4, 1)
    inner('Senegal (SEN)', 5, 1)
    inner('Netherlands (NED)', 6, 1)
    # B
    inner('England (ENG)', 3, 7)
    inner('Iran (IRN)', 4, 7)
    inner('USA (USA)', 5, 7)
    inner('Wales (WAL)', 6, 7)
    # C
    inner('Argentina (ARG)', 3, 13)
    inner('Saudi Arabia (KSA)', 4, 13)
    inner('Mexico (MEX)', 5, 13)
    inner('Poland (POL)', 6, 13)
    # D
    inner('France (FRA)', 3, 19)
    inner('Australia (AUS)', 4, 19)
    inner('Denmark (DEN)', 5, 19)
    inner('Tunisia (TUN)', 6, 19)
    # E
    inner('Spain (ESP)', 10, 1)
    inner('Costa Rica (CRC)', 11, 1)
    inner('Germany (GER)', 12, 1)
    inner('Japan (JPN)', 13, 1)
    # F
    inner('Belgium (BEL)', 10, 7)
    inner('Canada (CAN)', 11, 7)
    inner('Morocco (MAR)', 12, 7)
    inner('Croatia (CRO)', 13, 7)
    # G
    inner('Brazil (BRA)', 10, 13)
    inner('Serbia (SRB)', 11, 13)
    inner('Switzerland (SUI)', 12, 13)
    inner('Cameroon (CMR)', 13, 13)
    # H
    inner('Portugal (POR)', 10, 19)
    inner('Ghana (GHA)', 11, 19)
    inner('Uruguay (URU)', 12, 19)
    inner('Korea Republic (KOR)', 13, 19)


create_teams()


def create_gr_matches():
    def inner(txt, ro, col):
        gr_label = customtkinter.CTkLabel(window, text=txt, width=30, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                          fg_color=(col_lab_gr), bg_color='black')
        gr_label.grid(row=ro, column=col, pady=10)
        gr_label['font'] = lab_rank_size

    inner('A', 15, 4)
    inner('B', 15, 10)
    inner('C', 15, 16)
    inner('D', 15, 22)

    inner('E', 23, 4)
    inner('F', 23, 10)
    inner('G', 23, 16)
    inner('H', 23, 22)


create_gr_matches()


def create_matches():
    def inner(date, date_ro, date_col, country1, country2):
        match_date = customtkinter.CTkLabel(window, text=date, border=1, width=2, height=1, borderwidth=1,
                                            corner_radius=cor_radius_std, text_font='Verdana 9 italic',
                                            bg_color=bg_col_std, fg_color=(fg_col_std))
        match_date.grid(row=date_ro, column=date_col)

        t1 = customtkinter.CTkLabel(window, text=country1, border=1, width=2, height=1, borderwidth=1,
                                    corner_radius=cor_radius_std, text_font=labfont,
                                    bg_color=bg_col_std, fg_color=(fg_color_teams))
        t1.grid(row=date_ro, column=date_col + 1, sticky=E)

        m1 = customtkinter.CTkLabel(window, text='-', border=1, width=2, height=1, borderwidth=1,
                                    corner_radius=cor_radius_std, text_font=labfont,
                                    bg_color=bg_col_std, fg_color=(fg_color_teams))
        m1.grid(row=date_ro, column=date_col + 3)

        t2 = customtkinter.CTkLabel(window, text=country2, border=1, width=2, height=1, borderwidth=1,
                                    corner_radius=cor_radius_std, text_font=labfont,
                                    bg_color=bg_col_std, fg_color=(fg_color_teams))
        t2.grid(row=date_ro, column=date_col + 5, sticky=W)

    # A
    inner('Sun, 20.Nov', 16, 1, 'QAT', 'ECU')
    inner('Mon, 21.Nov', 17, 1, 'SEN', 'NED')
    inner('Fri, 25.Nov', 18, 1, 'NED', 'ECU')
    inner('Fri, 25.Nov', 19, 1, 'QAT', 'SEN')
    inner('Tue, 29.Nov', 20, 1, 'NED', 'QAT')
    inner('Tue, 29.Nov', 21, 1, 'ECU', 'SEN')
    # B
    inner('Mon, 21.Nov', 16, 7, 'ENG', 'IRN')
    inner('Mon, 21.Nov', 17, 7, 'USA', 'WAL')
    inner('Fri, 25.Nov', 18, 7, 'ENG', 'USA')
    inner('Fri, 25.Nov', 19, 7, 'WAL', 'IRN')
    inner('Tue, 29.Nov', 20, 7, 'IRN', 'USA')
    inner('Tue, 29.Nov', 21, 7, 'WAL', 'ENG')
    # C
    inner('Tue, 22.Nov', 16, 13, 'ARG', 'KSA')
    inner('Tue, 22.Nov', 17, 13, 'MEX', 'POL')
    inner('Sat, 26.Nov', 18, 13, 'ARG', 'MEX')
    inner('Sat, 26.Nov', 19, 13, 'POL', 'KSA')
    inner('Wed, 30.Nov', 20, 13, 'KSA', 'MEX')
    inner('Wed, 30.Nov', 21, 13, 'POL', 'ARG')
    # D
    inner('Tue, 22.Nov', 16, 19, 'DEN', 'TUN')
    inner('Tue, 22.Nov', 17, 19, 'FRA', 'AUS')
    inner('Sat, 26.Nov', 18, 19, 'FRA', 'DEN')
    inner('Sat, 26.Nov', 19, 19, 'TUN', 'AUS')
    inner('Wed, 30.Nov', 20, 19, 'TUN', 'FRA')
    inner('Wed, 30.Nov', 21, 19, 'AUS', 'DEN')
    # E
    inner('Wed, 23.Nov', 24, 1, 'GER', 'JPN')
    inner('Wed, 23.Nov', 25, 1, 'ESP', 'CRC')
    inner('Sun, 27.Nov', 26, 1, 'ESP', 'GER')
    inner('Sun, 27.Nov', 27, 1, 'JPN', 'CRC')
    inner('Thu, 1.Dec', 28, 1, 'CRC', 'GER')
    inner('Thu, 1.Dec', 29, 1, 'JPN', 'ESP')
    # F
    inner('Wed, 23.Nov', 24, 7, 'MAR', 'CRO')
    inner('Wed, 23.Nov', 25, 7, 'BEL', 'CAN')
    inner('Sun, 27.Nov', 26, 7, 'CRO', 'CAN')
    inner('Sun, 27.Nov', 27, 7, 'BEL', 'MAR')
    inner('Thu, 1.Dec', 28, 7, 'CAN', 'MAR')
    inner('Thu, 1.Dec', 29, 7, 'CRO', 'BEL')
    # G
    inner('Thu, 24.Nov', 24, 13, 'BRA', 'SRB')
    inner('Thu, 24.Nov', 25, 13, 'SUI', 'CMR')
    inner('Mon, 28.Nov', 26, 13, 'BRA', 'SUI')
    inner('Mon, 28.Nov', 27, 13, 'CMR', 'SRB')
    inner('Fri, 2.Dec', 28, 13, 'CMR', 'BRA')
    inner('Fri, 2.Dec', 29, 13, 'SRB', 'SUI')
    # H
    inner('Thu, 24.Nov', 24, 19, 'POR', 'GHA')
    inner('Thu, 24.Nov', 25, 19, 'URU', 'KOR')
    inner('Mon, 28.Nov', 26, 19, 'POR', 'URU')
    inner('Mon, 28.Nov', 27, 19, 'KOR', 'GHA')
    inner('Fri, 2.Dec', 28, 19, 'KOR', 'POR')
    inner('Fri, 2.Dec', 29, 19, 'GHA', 'URU')


create_matches()

# scores grA --------------------------------------------------

score_m1t1 = StringVar()
ent_m1t1 = Entry(window, textvariable=score_m1t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m1t1.grid(row=16, column=3)

score_m1t2 = StringVar()
ent_m1t2 = Entry(window, textvariable=score_m1t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m1t2.grid(row=16, column=5)

score_m2t1 = StringVar()
ent_m2t1 = Entry(window, textvariable=score_m2t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m2t1.grid(row=17, column=3)

score_m2t2 = StringVar()
ent_m2t2 = Entry(window, textvariable=score_m2t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m2t2.grid(row=17, column=5)

score_m3t1 = StringVar()
ent_m3t1 = Entry(window, textvariable=score_m3t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m3t1.grid(row=18, column=3)

score_m3t2 = StringVar()
ent_m3t2 = Entry(window, textvariable=score_m3t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m3t2.grid(row=18, column=5)

score_m4t1 = StringVar()
ent_m4t1 = Entry(window, textvariable=score_m4t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m4t1.grid(row=19, column=3)

score_m4t2 = StringVar()
ent_m4t2 = Entry(window, textvariable=score_m4t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m4t2.grid(row=19, column=5)

score_m5t1 = StringVar()
ent_m5t1 = Entry(window, textvariable=score_m5t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m5t1.grid(row=20, column=3)

score_m5t2 = StringVar()
ent_m5t2 = Entry(window, textvariable=score_m5t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m5t2.grid(row=20, column=5)

score_m6t1 = StringVar()
ent_m6t1 = Entry(window, textvariable=score_m6t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m6t1.grid(row=21, column=3)

score_m6t2 = StringVar()
ent_m6t2 = Entry(window, textvariable=score_m6t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m6t2.grid(row=21, column=5)

# scores grB --------------------------------------------------

score_m7t1 = StringVar()
ent_m7t1 = Entry(window, textvariable=score_m7t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m7t1.grid(row=16, column=9)

score_m7t2 = StringVar()
ent_m7t2 = Entry(window, textvariable=score_m7t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m7t2.grid(row=16, column=11)

score_m8t1 = StringVar()
ent_m8t1 = Entry(window, textvariable=score_m8t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m8t1.grid(row=17, column=9)

score_m8t2 = StringVar()
ent_m8t2 = Entry(window, textvariable=score_m8t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m8t2.grid(row=17, column=11)

score_m9t1 = StringVar()
ent_m9t1 = Entry(window, textvariable=score_m9t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m9t1.grid(row=18, column=9)

score_m9t2 = StringVar()
ent_m9t2 = Entry(window, textvariable=score_m9t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m9t2.grid(row=18, column=11)

score_m10t1 = StringVar()
ent_m10t1 = Entry(window, textvariable=score_m10t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m10t1.grid(row=19, column=9)

score_m10t2 = StringVar()
ent_m10t2 = Entry(window, textvariable=score_m10t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m10t2.grid(row=19, column=11)

score_m11t1 = StringVar()
ent_m11t1 = Entry(window, textvariable=score_m11t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m11t1.grid(row=20, column=9)

score_m11t2 = StringVar()
ent_m11t2 = Entry(window, textvariable=score_m11t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m11t2.grid(row=20, column=11)

score_m12t1 = StringVar()
ent_m12t1 = Entry(window, textvariable=score_m12t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m12t1.grid(row=21, column=9)

score_m12t2 = StringVar()
ent_m12t2 = Entry(window, textvariable=score_m12t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m12t2.grid(row=21, column=11)

# scores grC --------------------------------------------------

score_m13t1 = StringVar()
ent_m13t1 = Entry(window, textvariable=score_m13t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m13t1.grid(row=16, column=15)

score_m13t2 = StringVar()
ent_m13t2 = Entry(window, textvariable=score_m13t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m13t2.grid(row=16, column=17)

score_m14t1 = StringVar()
ent_m14t1 = Entry(window, textvariable=score_m14t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m14t1.grid(row=17, column=15)

score_m14t2 = StringVar()
ent_m14t2 = Entry(window, textvariable=score_m14t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m14t2.grid(row=17, column=17)

score_m15t1 = StringVar()
ent_m15t1 = Entry(window, textvariable=score_m15t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m15t1.grid(row=18, column=15)

score_m15t2 = StringVar()
ent_m15t2 = Entry(window, textvariable=score_m15t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m15t2.grid(row=18, column=17)

score_m16t1 = StringVar()
ent_m16t1 = Entry(window, textvariable=score_m16t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m16t1.grid(row=19, column=15)

score_m16t2 = StringVar()
ent_m16t2 = Entry(window, textvariable=score_m16t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m16t2.grid(row=19, column=17)

score_m17t1 = StringVar()
ent_m17t1 = Entry(window, textvariable=score_m17t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m17t1.grid(row=20, column=15)

score_m17t2 = StringVar()
ent_m17t2 = Entry(window, textvariable=score_m17t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m17t2.grid(row=20, column=17)

score_m18t1 = StringVar()
ent_m18t1 = Entry(window, textvariable=score_m18t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m18t1.grid(row=21, column=15)

score_m18t2 = StringVar()
ent_m18t2 = Entry(window, textvariable=score_m18t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m18t2.grid(row=21, column=17)

# scores grD --------------------------------------------------

score_m19t1 = StringVar()
ent_m19t1 = Entry(window, textvariable=score_m19t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m19t1.grid(row=16, column=21)

score_m19t2 = StringVar()
ent_m19t2 = Entry(window, textvariable=score_m19t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m19t2.grid(row=16, column=23)

score_m20t1 = StringVar()
ent_m20t1 = Entry(window, textvariable=score_m20t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m20t1.grid(row=17, column=21)

score_m20t2 = StringVar()
ent_m20t2 = Entry(window, textvariable=score_m20t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m20t2.grid(row=17, column=23)

score_m21t1 = StringVar()
ent_m21t1 = Entry(window, textvariable=score_m21t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m21t1.grid(row=18, column=21)

score_m21t2 = StringVar()
ent_m21t2 = Entry(window, textvariable=score_m21t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m21t2.grid(row=18, column=23)

score_m22t1 = StringVar()
ent_m22t1 = Entry(window, textvariable=score_m22t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m22t1.grid(row=19, column=21)

score_m22t2 = StringVar()
ent_m22t2 = Entry(window, textvariable=score_m22t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m22t2.grid(row=19, column=23)

score_m23t1 = StringVar()
ent_m23t1 = Entry(window, textvariable=score_m23t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m23t1.grid(row=20, column=21)

score_m23t2 = StringVar()
ent_m23t2 = Entry(window, textvariable=score_m23t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m23t2.grid(row=20, column=23)

score_m24t1 = StringVar()
ent_m24t1 = Entry(window, textvariable=score_m24t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m24t1.grid(row=21, column=21)

score_m24t2 = StringVar()
ent_m24t2 = Entry(window, textvariable=score_m24t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m24t2.grid(row=21, column=23)

# scores grE --------------------------------------------------

score_m25t1 = StringVar()
ent_m25t1 = Entry(window, textvariable=score_m25t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m25t1.grid(row=24, column=3)

score_m25t2 = StringVar()
ent_m25t2 = Entry(window, textvariable=score_m25t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m25t2.grid(row=24, column=5)

score_m26t1 = StringVar()
ent_m26t1 = Entry(window, textvariable=score_m26t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m26t1.grid(row=25, column=3)

score_m26t2 = StringVar()
ent_m26t2 = Entry(window, textvariable=score_m26t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m26t2.grid(row=25, column=5)

score_m27t1 = StringVar()
ent_m27t1 = Entry(window, textvariable=score_m27t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m27t1.grid(row=26, column=3)

score_m27t2 = StringVar()
ent_m27t2 = Entry(window, textvariable=score_m27t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m27t2.grid(row=26, column=5)

score_m28t1 = StringVar()
ent_m28t1 = Entry(window, textvariable=score_m28t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m28t1.grid(row=27, column=3)

score_m28t2 = StringVar()
ent_m28t2 = Entry(window, textvariable=score_m28t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m28t2.grid(row=27, column=5)

score_m29t1 = StringVar()
ent_m29t1 = Entry(window, textvariable=score_m29t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m29t1.grid(row=28, column=3)

score_m29t2 = StringVar()
ent_m29t2 = Entry(window, textvariable=score_m29t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m29t2.grid(row=28, column=5)

score_m30t1 = StringVar()
ent_m30t1 = Entry(window, textvariable=score_m30t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m30t1.grid(row=29, column=3)

score_m30t2 = StringVar()
ent_m30t2 = Entry(window, textvariable=score_m30t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m30t2.grid(row=29, column=5)

# scores grF --------------------------------------------------

score_m31t1 = StringVar()
ent_m31t1 = Entry(window, textvariable=score_m31t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m31t1.grid(row=24, column=9)

score_m31t2 = StringVar()
ent_m31t2 = Entry(window, textvariable=score_m31t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m31t2.grid(row=24, column=11)

score_m32t1 = StringVar()
ent_m32t1 = Entry(window, textvariable=score_m32t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m32t1.grid(row=25, column=9)

score_m32t2 = StringVar()
ent_m32t2 = Entry(window, textvariable=score_m32t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m32t2.grid(row=25, column=11)

score_m33t1 = StringVar()
ent_m33t1 = Entry(window, textvariable=score_m33t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m33t1.grid(row=26, column=9)

score_m33t2 = StringVar()
ent_m33t2 = Entry(window, textvariable=score_m33t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m33t2.grid(row=26, column=11)

score_m34t1 = StringVar()
ent_m34t1 = Entry(window, textvariable=score_m34t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m34t1.grid(row=27, column=9)

score_m34t2 = StringVar()
ent_m34t2 = Entry(window, textvariable=score_m34t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m34t2.grid(row=27, column=11)

score_m35t1 = StringVar()
ent_m35t1 = Entry(window, textvariable=score_m35t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m35t1.grid(row=28, column=9)

score_m35t2 = StringVar()
ent_m35t2 = Entry(window, textvariable=score_m35t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m35t2.grid(row=28, column=11)

score_m36t1 = StringVar()
ent_m36t1 = Entry(window, textvariable=score_m36t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m36t1.grid(row=29, column=9)

score_m36t2 = StringVar()
ent_m36t2 = Entry(window, textvariable=score_m36t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m36t2.grid(row=29, column=11)

# scores grG --------------------------------------------------

score_m37t1 = StringVar()
ent_m37t1 = Entry(window, textvariable=score_m37t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m37t1.grid(row=24, column=15)

score_m37t2 = StringVar()
ent_m37t2 = Entry(window, textvariable=score_m37t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m37t2.grid(row=24, column=17)

score_m38t1 = StringVar()
ent_m38t1 = Entry(window, textvariable=score_m38t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m38t1.grid(row=25, column=15)

score_m38t2 = StringVar()
ent_m38t2 = Entry(window, textvariable=score_m38t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m38t2.grid(row=25, column=17)

score_m39t1 = StringVar()
ent_m39t1 = Entry(window, textvariable=score_m39t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m39t1.grid(row=26, column=15)

score_m39t2 = StringVar()
ent_m39t2 = Entry(window, textvariable=score_m39t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m39t2.grid(row=26, column=17)

score_m40t1 = StringVar()
ent_m40t1 = Entry(window, textvariable=score_m40t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m40t1.grid(row=27, column=15)

score_m40t2 = StringVar()
ent_m40t2 = Entry(window, textvariable=score_m40t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m40t2.grid(row=27, column=17)

score_m41t1 = StringVar()
ent_m41t1 = Entry(window, textvariable=score_m41t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m41t1.grid(row=28, column=15)

score_m41t2 = StringVar()
ent_m41t2 = Entry(window, textvariable=score_m41t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m41t2.grid(row=28, column=17)

score_m42t1 = StringVar()
ent_m42t1 = Entry(window, textvariable=score_m42t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m42t1.grid(row=29, column=15)

score_m42t2 = StringVar()
ent_m42t2 = Entry(window, textvariable=score_m42t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m42t2.grid(row=29, column=17)

# scores grH --------------------------------------------------

score_m43t1 = StringVar()
ent_m43t1 = Entry(window, textvariable=score_m43t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m43t1.grid(row=24, column=21)

score_m43t2 = StringVar()
ent_m43t2 = Entry(window, textvariable=score_m43t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m43t2.grid(row=24, column=23)

score_m44t1 = StringVar()
ent_m44t1 = Entry(window, textvariable=score_m44t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m44t1.grid(row=25, column=21)

score_m44t2 = StringVar()
ent_m44t2 = Entry(window, textvariable=score_m44t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m44t2.grid(row=25, column=23)

score_m45t1 = StringVar()
ent_m45t1 = Entry(window, textvariable=score_m45t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m45t1.grid(row=26, column=21)

score_m45t2 = StringVar()
ent_m45t2 = Entry(window, textvariable=score_m45t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m45t2.grid(row=26, column=23)

score_m46t1 = StringVar()
ent_m46t1 = Entry(window, textvariable=score_m46t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m46t1.grid(row=27, column=21)

score_m46t2 = StringVar()
ent_m46t2 = Entry(window, textvariable=score_m46t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m46t2.grid(row=27, column=23)

score_m47t1 = StringVar()
ent_m47t1 = Entry(window, textvariable=score_m47t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m47t1.grid(row=28, column=21)

score_m47t2 = StringVar()
ent_m47t2 = Entry(window, textvariable=score_m47t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m47t2.grid(row=28, column=23)

score_m48t1 = StringVar()
ent_m48t1 = Entry(window, textvariable=score_m48t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m48t1.grid(row=29, column=21)

score_m48t2 = StringVar()
ent_m48t2 = Entry(window, textvariable=score_m48t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
ent_m48t2.grid(row=29, column=23)


# add matches---------------------------------------------------------------

def add_match_grA():
    wc22_bend.update_match_a(ent_m1t1.get(), score_m1t2.get(), ent_m2t1.get(), score_m2t2.get(), ent_m3t1.get(),
                             score_m3t2.get(), ent_m4t1.get(), score_m4t2.get(), ent_m5t1.get(), score_m5t2.get(),
                             ent_m6t1.get(), score_m6t2.get())
    wc22_bend.update_group_a()


def add_match_grB():
    wc22_bend.update_match_b(ent_m7t1.get(), score_m7t2.get(), ent_m8t1.get(), score_m8t2.get(), ent_m9t1.get(),
                             score_m9t2.get(), ent_m10t1.get(), score_m10t2.get(), ent_m11t1.get(), score_m11t2.get(),
                             ent_m12t1.get(), score_m12t2.get())
    wc22_bend.update_group_b()


def add_match_grC():
    wc22_bend.update_match_c(ent_m13t1.get(), score_m13t2.get(), ent_m14t1.get(), score_m14t2.get(), ent_m15t1.get(),
                             score_m15t2.get(), ent_m16t1.get(), score_m16t2.get(), ent_m17t1.get(), score_m17t2.get(),
                             ent_m18t1.get(), score_m18t2.get())
    wc22_bend.update_group_c()


def add_match_grD():
    wc22_bend.update_match_d(ent_m19t1.get(), score_m19t2.get(), ent_m20t1.get(), score_m20t2.get(), ent_m21t1.get(),
                             score_m21t2.get(), ent_m22t1.get(), score_m22t2.get(), ent_m23t1.get(), score_m23t2.get(),
                             ent_m24t1.get(), score_m24t2.get())
    wc22_bend.update_group_d()


def add_match_grE():
    wc22_bend.update_match_e(ent_m25t1.get(), score_m25t2.get(), ent_m26t1.get(), score_m26t2.get(), ent_m27t1.get(),
                             score_m27t2.get(), ent_m28t1.get(), score_m28t2.get(), ent_m29t1.get(), score_m29t2.get(),
                             ent_m30t1.get(), score_m30t2.get())
    wc22_bend.update_group_e()


def add_match_grF():
    wc22_bend.update_match_f(ent_m31t1.get(), score_m31t2.get(), ent_m32t1.get(), score_m32t2.get(), ent_m33t1.get(),
                             score_m33t2.get(), ent_m34t1.get(), score_m34t2.get(), ent_m35t1.get(), score_m35t2.get(),
                             ent_m36t1.get(), score_m36t2.get())
    wc22_bend.update_group_f()


def add_match_grG():
    wc22_bend.update_match_g(ent_m37t1.get(), score_m37t2.get(), ent_m38t1.get(), score_m38t2.get(), ent_m39t1.get(),
                             score_m39t2.get(), ent_m40t1.get(), score_m40t2.get(), ent_m41t1.get(), score_m41t2.get(),
                             ent_m42t1.get(), score_m42t2.get())
    wc22_bend.update_group_g()


def add_match_grH():
    wc22_bend.update_match_h(ent_m43t1.get(), score_m43t2.get(), ent_m44t1.get(), score_m44t2.get(), ent_m45t1.get(),
                             score_m45t2.get(), ent_m46t1.get(), score_m46t2.get(), ent_m47t1.get(), score_m47t2.get(),
                             ent_m48t1.get(), score_m48t2.get())
    wc22_bend.update_group_h()


# view groups ------------------------------------
fg_col_view = fg_color_teams


def view_grA():
    cover_grA = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=22,
                        highlightbackground='black')
    cover_grA.grid(row=3, column=1, rowspan=4)

    ro = 3
    for row in wc22_bend.show_teams_a():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=1, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 3
    for row in wc22_bend.show_mp_a():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view),
                                         height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=2)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 3
    for row in wc22_bend.show_gd_a():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view),
                                         height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=3)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 3
    for row in wc22_bend.show_pts_a():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view),
                                          height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=4)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grB():
    cover_grB = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=20,
                        highlightbackground='black')
    cover_grB.grid(row=3, column=7, rowspan=4)

    ro = 3
    for row in wc22_bend.show_teams_b():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=7, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 3
    for row in wc22_bend.show_mp_b():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=8)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 3
    for row in wc22_bend.show_gd_b():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=9)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 3
    for row in wc22_bend.show_pts_b():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=10)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grC():
    cover_grC = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=22,
                        highlightbackground='black')
    cover_grC.grid(row=3, column=13, rowspan=4)

    ro = 3
    for row in wc22_bend.show_teams_c():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=13, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 3
    for row in wc22_bend.show_mp_c():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=14)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 3
    for row in wc22_bend.show_gd_c():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=15)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 3
    for row in wc22_bend.show_pts_c():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=16)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grD():
    cover_grD = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=20,
                        highlightbackground='black')
    cover_grD.grid(row=3, column=19, rowspan=4)

    ro = 3
    for row in wc22_bend.show_teams_d():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=19, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 3
    for row in wc22_bend.show_mp_d():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=20)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 3
    for row in wc22_bend.show_gd_d():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=21)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 3
    for row in wc22_bend.show_pts_d():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=22)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grE():
    cover_grE = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=20,
                        highlightbackground='black')
    cover_grE.grid(row=10, column=1, rowspan=4)

    ro = 10
    for row in wc22_bend.show_teams_e():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=1, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 10
    for row in wc22_bend.show_mp_e():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=2)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 10
    for row in wc22_bend.show_gd_e():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=3)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 10
    for row in wc22_bend.show_pts_e():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=4)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grF():
    cover_grF = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=20,
                        highlightbackground='black')
    cover_grF.grid(row=10, column=7, rowspan=4)

    ro = 10
    for row in wc22_bend.show_teams_f():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=7, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 10
    for row in wc22_bend.show_mp_f():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=8)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 10
    for row in wc22_bend.show_gd_f():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=9)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 10
    for row in wc22_bend.show_pts_f():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=10)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grG():
    cover_grG = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=20,
                        highlightbackground='black')
    cover_grG.grid(row=10, column=13, rowspan=4)

    ro = 10
    for row in wc22_bend.show_teams_g():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=13, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 10
    for row in wc22_bend.show_mp_g():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=14)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 10
    for row in wc22_bend.show_gd_g():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=15)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 10
    for row in wc22_bend.show_pts_g():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=16)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


def view_grH():
    cover_grH = Listbox(window, bg='black', fg='black', bd=0, borderwidth=0, height=6, width=25,
                        highlightbackground='black')
    cover_grH.grid(row=10, column=19, rowspan=4)

    ro = 10
    for row in wc22_bend.show_teams_h():
        team = customtkinter.CTkLabel(window, text=row[1], width=80, height=23, bg=bg_overall_GUI, corner_radius=cor_radius_std,
                                      text_font=labfont, fg_color=(fg_col_view), bg_color='black')
        team.grid(row=ro, column=19, sticky=W)
        team['font'] = lab_rank_size
        ro += 1

    ro_mp = 10
    for row in wc22_bend.show_mp_h():
        team_mp = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_mp.grid(row=ro_mp, column=20)
        team_mp['font'] = lab_rank_size
        ro_mp += 1

    ro_gd = 10
    for row in wc22_bend.show_gd_h():
        team_gd = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                         fg_color=(fg_col_view), height=20, corner_radius=cor_radius_std)
        team_gd.grid(row=ro_gd, column=21)
        team_gd['font'] = lab_rank_size
        ro_gd += 1

    ro_pts = 10
    for row in wc22_bend.show_pts_h():
        team_pts = customtkinter.CTkLabel(window, text=row, text_font=labfont, bg_color=bg_col_std, width=15,
                                          fg_color=(fg_col_view), height=22, corner_radius=cor_radius_std)
        team_pts.grid(row=ro_pts, column=22)
        team_pts['font'] = lab_rank_size
        ro_pts += 1


# command functions -------------------

# f1_a = add_match_grA
# f2_a = view_grA
# f1_b = add_match_grB
# f2_b = view_grB
# f1_c = add_match_grC
# f2_c = view_grC
# f1_d = add_match_grD
# f2_d = view_grD
# f1_e = add_match_grE
# f2_e = view_grE
# f1_f = add_match_grF
# f2_f = view_grF
# f1_g = add_match_grG
# f2_g = view_grG
# f1_h = add_match_grH
# f2_h = view_grH


def confirm_update():
    window_confirm_update = Tk()
    window_confirm_update.title('Confirm Update Groups')
    window_confirm_update.geometry('400x150')
    window_confirm_update.iconbitmap('img_icon.ico')
    window_confirm_update.configure(bg='black')
    f_destroy = window_confirm_update.destroy
    lavert = Label(window_confirm_update, text='Before updating any match, you have to be sure that you have pressed'
                                          '"SHOW DATA" button, otherwise all previous saved matches will be lost.',
                   font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
    lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
    btn_update_yes = Button(window_confirm_update, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold',
                            command=lambda: [add_match_grA(), add_match_grB(), add_match_grC(),
                                             add_match_grD(), add_match_grE(), add_match_grF(), add_match_grG(),
                                             add_match_grH(), view_grA(), view_grB(), view_grC(), view_grD(),
                                             view_grE(), view_grF(), view_grG(), view_grH(), f_destroy()])
    btn_update_yes.grid(row=4, column=1, sticky=E, padx=10, pady=10)

    btn_update_no = Button(window_confirm_update, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_confirm_update.destroy)
    btn_update_no.grid(row=4, column=2, sticky=W, padx=10, pady=10)

    window_confirm_update.mainloop()


def confirm_reset():
    window_confirm_reset = Tk()
    window_confirm_reset.title('Confirm Reset Data')
    window_confirm_reset.geometry('365x120')
    window_confirm_reset.iconbitmap('img_icon.ico')
    window_confirm_reset.configure(bg='black')
    f_destroy = window_confirm_reset.destroy
    lavert = Label(window_confirm_reset, text='Are you sure you want to erase all data?',
                   font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
    lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=35, pady=15)
    btn_update_yes = Button(window_confirm_reset, text='YES', bg='red', fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=lambda: [wc22_bend.reset_tables(), f_destroy()])
    btn_update_yes.grid(row=4, column=1, sticky=E, padx=12, pady=10)
    btn_update_no = Button(window_confirm_reset, text='NO', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_confirm_reset.destroy)
    btn_update_no.grid(row=4, column=2, sticky=W, padx=5, pady=10)

    window_confirm_reset.mainloop()


# show all data ----------------------

def show_data():
    view_grA()
    view_grB()
    view_grC()
    view_grD()
    view_grE()
    view_grF()
    view_grG()
    view_grH()

    lab_all_updated = Label(window, text='Data updated', fg='#65C252', bg='black', font='Verdana 7 bold')
    lab_all_updated.grid(row=21, column=46, sticky=N)

    # if len(ent_m1t1.get()) < 1:
    if ent_m1t1.get() == '':
        # A
        ent_m1t1.insert(END, wc22_bend.show_data_a()[0][0])
        ent_m1t2.insert(END, wc22_bend.show_data_a()[0][1])
        ent_m2t1.insert(END, wc22_bend.show_data_a()[1][0])
        ent_m2t2.insert(END, wc22_bend.show_data_a()[1][1])
        ent_m3t1.insert(END, wc22_bend.show_data_a()[2][0])
        ent_m3t2.insert(END, wc22_bend.show_data_a()[2][1])
        ent_m4t1.insert(END, wc22_bend.show_data_a()[3][0])
        ent_m4t2.insert(END, wc22_bend.show_data_a()[3][1])
        ent_m5t1.insert(END, wc22_bend.show_data_a()[4][0])
        ent_m5t2.insert(END, wc22_bend.show_data_a()[4][1])
        ent_m6t1.insert(END, wc22_bend.show_data_a()[5][0])
        ent_m6t2.insert(END, wc22_bend.show_data_a()[5][1])
        # B
        ent_m7t1.insert(END, wc22_bend.show_data_b()[0][0])
        ent_m7t2.insert(END, wc22_bend.show_data_b()[0][1])
        ent_m8t1.insert(END, wc22_bend.show_data_b()[1][0])
        ent_m8t2.insert(END, wc22_bend.show_data_b()[1][1])
        ent_m9t1.insert(END, wc22_bend.show_data_b()[2][0])
        ent_m9t2.insert(END, wc22_bend.show_data_b()[2][1])
        ent_m10t1.insert(END, wc22_bend.show_data_b()[3][0])
        ent_m10t2.insert(END, wc22_bend.show_data_b()[3][1])
        ent_m11t1.insert(END, wc22_bend.show_data_b()[4][0])
        ent_m11t2.insert(END, wc22_bend.show_data_b()[4][1])
        ent_m12t1.insert(END, wc22_bend.show_data_b()[5][0])
        ent_m12t2.insert(END, wc22_bend.show_data_b()[5][1])
        # C
        ent_m13t1.insert(END, wc22_bend.show_data_c()[0][0])
        ent_m13t2.insert(END, wc22_bend.show_data_c()[0][1])
        ent_m14t1.insert(END, wc22_bend.show_data_c()[1][0])
        ent_m14t2.insert(END, wc22_bend.show_data_c()[1][1])
        ent_m15t1.insert(END, wc22_bend.show_data_c()[2][0])
        ent_m15t2.insert(END, wc22_bend.show_data_c()[2][1])
        ent_m16t1.insert(END, wc22_bend.show_data_c()[3][0])
        ent_m16t2.insert(END, wc22_bend.show_data_c()[3][1])
        ent_m17t1.insert(END, wc22_bend.show_data_c()[4][0])
        ent_m17t2.insert(END, wc22_bend.show_data_c()[4][1])
        ent_m18t1.insert(END, wc22_bend.show_data_c()[5][0])
        ent_m18t2.insert(END, wc22_bend.show_data_c()[5][1])
        # D
        ent_m19t1.insert(END, wc22_bend.show_data_d()[0][0])
        ent_m19t2.insert(END, wc22_bend.show_data_d()[0][1])
        ent_m20t1.insert(END, wc22_bend.show_data_d()[1][0])
        ent_m20t2.insert(END, wc22_bend.show_data_d()[1][1])
        ent_m21t1.insert(END, wc22_bend.show_data_d()[2][0])
        ent_m21t2.insert(END, wc22_bend.show_data_d()[2][1])
        ent_m22t1.insert(END, wc22_bend.show_data_d()[3][0])
        ent_m22t2.insert(END, wc22_bend.show_data_d()[3][1])
        ent_m23t1.insert(END, wc22_bend.show_data_d()[4][0])
        ent_m23t2.insert(END, wc22_bend.show_data_d()[4][1])
        ent_m24t1.insert(END, wc22_bend.show_data_d()[5][0])
        ent_m24t2.insert(END, wc22_bend.show_data_d()[5][1])
        # E
        ent_m25t1.insert(END, wc22_bend.show_data_e()[0][0])
        ent_m25t2.insert(END, wc22_bend.show_data_e()[0][1])
        ent_m26t1.insert(END, wc22_bend.show_data_e()[1][0])
        ent_m26t2.insert(END, wc22_bend.show_data_e()[1][1])
        ent_m27t1.insert(END, wc22_bend.show_data_e()[2][0])
        ent_m27t2.insert(END, wc22_bend.show_data_e()[2][1])
        ent_m28t1.insert(END, wc22_bend.show_data_e()[3][0])
        ent_m28t2.insert(END, wc22_bend.show_data_e()[3][1])
        ent_m29t1.insert(END, wc22_bend.show_data_e()[4][0])
        ent_m29t2.insert(END, wc22_bend.show_data_e()[4][1])
        ent_m30t1.insert(END, wc22_bend.show_data_e()[5][0])
        ent_m30t2.insert(END, wc22_bend.show_data_e()[5][1])
        # F
        ent_m31t1.insert(END, wc22_bend.show_data_f()[0][0])
        ent_m31t2.insert(END, wc22_bend.show_data_f()[0][1])
        ent_m32t1.insert(END, wc22_bend.show_data_f()[1][0])
        ent_m32t2.insert(END, wc22_bend.show_data_f()[1][1])
        ent_m33t1.insert(END, wc22_bend.show_data_f()[2][0])
        ent_m33t2.insert(END, wc22_bend.show_data_f()[2][1])
        ent_m34t1.insert(END, wc22_bend.show_data_f()[3][0])
        ent_m34t2.insert(END, wc22_bend.show_data_f()[3][1])
        ent_m35t1.insert(END, wc22_bend.show_data_f()[4][0])
        ent_m35t2.insert(END, wc22_bend.show_data_f()[4][1])
        ent_m36t1.insert(END, wc22_bend.show_data_f()[5][0])
        ent_m36t2.insert(END, wc22_bend.show_data_f()[5][1])
        # G
        ent_m37t1.insert(END, wc22_bend.show_data_g()[0][0])
        ent_m37t2.insert(END, wc22_bend.show_data_g()[0][1])
        ent_m38t1.insert(END, wc22_bend.show_data_g()[1][0])
        ent_m38t2.insert(END, wc22_bend.show_data_g()[1][1])
        ent_m39t1.insert(END, wc22_bend.show_data_g()[2][0])
        ent_m39t2.insert(END, wc22_bend.show_data_g()[2][1])
        ent_m40t1.insert(END, wc22_bend.show_data_g()[3][0])
        ent_m40t2.insert(END, wc22_bend.show_data_g()[3][1])
        ent_m41t1.insert(END, wc22_bend.show_data_g()[4][0])
        ent_m41t2.insert(END, wc22_bend.show_data_g()[4][1])
        ent_m42t1.insert(END, wc22_bend.show_data_g()[5][0])
        ent_m42t2.insert(END, wc22_bend.show_data_g()[5][1])
        # H
        ent_m43t1.insert(END, wc22_bend.show_data_h()[0][0])
        ent_m43t2.insert(END, wc22_bend.show_data_h()[0][1])
        ent_m44t1.insert(END, wc22_bend.show_data_h()[1][0])
        ent_m44t2.insert(END, wc22_bend.show_data_h()[1][1])
        ent_m45t1.insert(END, wc22_bend.show_data_h()[2][0])
        ent_m45t2.insert(END, wc22_bend.show_data_h()[2][1])
        ent_m46t1.insert(END, wc22_bend.show_data_h()[3][0])
        ent_m46t2.insert(END, wc22_bend.show_data_h()[3][1])
        ent_m47t1.insert(END, wc22_bend.show_data_h()[4][0])
        ent_m47t2.insert(END, wc22_bend.show_data_h()[4][1])
        ent_m48t1.insert(END, wc22_bend.show_data_h()[5][0])
        ent_m48t2.insert(END, wc22_bend.show_data_h()[5][1])

    else:
        all_updated()


def all_updated():
    window_updated = Tk()
    window_updated.title('ALL UP TO DATE')
    window_updated.iconbitmap('img_icon.ico')
    window_updated.geometry('200x100')
    window_updated.configure(bg='#6B6E6E')
    lavert = Label(window_updated, text='All data is updated!',
                   font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
    lavert.grid(row=0, column=0, padx=30, pady=10)
    btn_update_ok = Button(window_updated, text='OK', command=window_updated.destroy, anchor=CENTER, bd=3, fg='white',
                           bg='#6B6E6E')
    btn_update_ok.grid(row=4, column=0, padx=30, pady=10)


blank_lab = Label(window, text='', bg='black', width=2)
blank_lab.grid(rowspan=22, column=45)

b_show_data = Button(window, text='UPDATE', command=confirm_update, width=13, bd=5, bg=fg_color_teams, fg='darkblue',
                     font='Verdana 9 bold')
b_show_data.grid(row=15, column=46, sticky=N)

b_show_data = Button(window, text='SHOW DATA', command=show_data, width=12, bg='#65C252', bd=5, font='Verdana 9 bold')
b_show_data.grid(row=22, column=46, sticky=N)


def func_final_stages():
    window_ko = tkinter.Toplevel()
    window_ko.title('WORLD CUP 2022 - FINAL STAGES')
    window_ko.geometry('1580x760')
    window_ko.iconbitmap('img_icon.ico')
    # window_ko.attributes("-alpha", 0.9)
    # window_ko.configure(bg='black')

    fp1 = open("wc22wall_dark_final.jpg", "rb")

    fp = fp1
    image_wall_final = PIL.Image.open(fp)
    resized_wall = image_wall_final.resize((1800, 1400))
    photoimg_final = ImageTk.PhotoImage(resized_wall)
    image_wall_final = Label(window_ko, image=photoimg_final)
    image_wall_final.place(x=-33, y=-500)

    blank_lab1 = Label(window_ko, text='', bg='black', width=2, height=1)
    blank_lab1.grid(row=0, column=0)

    def stages_lab():
        def inner(phase, col):
            st_lab = customtkinter.CTkLabel(window_ko, text=phase, width=80, height=23, bg=bg_overall_GUI,
                                            corner_radius=cor_radius_std, text_font=labfont, fg_color=(col_lab_gr),
                                            bg_color='black')
            st_lab.grid(row=1, column=col, columnspan=5, pady=8)

        inner('Rounf of 16', 2)
        inner('Quater Finals', 8)
        inner('Semi Finals', 14)

    stages_lab()

    def matches_finals():
        def inner_matches(date, info, date_ro, date_col, country1, country2):
            match_date = customtkinter.CTkLabel(window_ko, text=date, border=1, width=2, height=1, borderwidth=1,
                                                corner_radius=cor_radius_std, text_font='Verdana 9 italic',
                                                bg_color=bg_col_std, fg_color=(fg_col_std))
            match_date.grid(row=date_ro, column=date_col, pady=2)
            info_lab = customtkinter.CTkLabel(window_ko, text=info, border=1, width=2, height=1, borderwidth=1,
                                              corner_radius=cor_radius_std, text_font='Verdana 6 italic',
                                              bg_color=bg_col_std, fg_color=(fg_col_std))
            info_lab.grid(row=date_ro + 1, column=date_col)

            t1 = customtkinter.CTkLabel(window_ko, text=country1, border=1, width=2, height=1, borderwidth=1,
                                        corner_radius=cor_radius_std, text_font=labfont,
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            t1.grid(row=date_ro, column=date_col + 1, sticky=E)

            m1 = customtkinter.CTkLabel(window_ko, text='-', border=1, width=2, height=1, borderwidth=1,
                                        corner_radius=cor_radius_std, text_font=labfont,
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            m1.grid(row=date_ro, column=date_col + 3)

            t2 = customtkinter.CTkLabel(window_ko, text=country2, border=1, width=2, height=1, borderwidth=1,
                                        corner_radius=cor_radius_std, text_font=labfont,
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            t2.grid(row=date_ro, column=date_col + 5, sticky=W)

        # Round of 16
        inner_matches('Sat,3.Dec', '49.1A-2B', 2, 1, wc22_bend.final_stages('gra')[0], wc22_bend.final_stages('grb')[1])
        inner_matches('Sat,3.Dec', '50.1C-2D', 4, 1, wc22_bend.final_stages('grc')[0], wc22_bend.final_stages('grd')[1])
        inner_matches('Sun,4.Dec', '51.1B-2A', 6, 1, wc22_bend.final_stages('grb')[0], wc22_bend.final_stages('gra')[1])
        inner_matches('Sun,4.Dec', '52.1D-2C', 8, 1, wc22_bend.final_stages('grd')[0], wc22_bend.final_stages('grc')[1])
        blank_lab = Label(window_ko, text='', bg='black', width=2, height=1)
        blank_lab.grid(row=10, column=1)
        inner_matches('Mon,5.Dec', '54.1G-2H', 11, 1, wc22_bend.final_stages('grg')[0],
                      wc22_bend.final_stages('grh')[1])
        inner_matches('Mon,5.Dec', '53.1E-2F', 13, 1, wc22_bend.final_stages('gre')[0],
                      wc22_bend.final_stages('grf')[1])
        inner_matches('Tue,6.Dec', '56.1H-2G', 15, 1, wc22_bend.final_stages('grh')[0],
                      wc22_bend.final_stages('grg')[1])
        inner_matches('Tue,6.Dec', '55.1F-2E', 17, 1, wc22_bend.final_stages('grf')[0],
                      wc22_bend.final_stages('gre')[1])

        # Quater finals
        inner_matches('Fri,9.Dec', '57.W49-W50', 3, 7, '...', '...')
        inner_matches('Fri,9.Dec', '58.W53-W54', 7, 7, '...', '...')
        inner_matches('Sat,10.Dec', '59.W51-W52', 12, 7, '...', '...')
        inner_matches('Sat,10.Dec', '60.W55-W56', 16, 7, '...', '...')

        # Semi finals
        inner_matches('Tue,13.Dec', '61.W57-W58', 5, 13, '...', '...')
        inner_matches('Wed,14.Dec', '62.W59-W60', 14, 13, '...', '...')

        # Finals
        blank_lab = Label(window_ko, text='', bg='black', width=2, height=4)
        blank_lab.grid(row=10, column=19)

        st_lab_tp = customtkinter.CTkLabel(window_ko, text='THIRD PLACE', width=80, height=23, bg='#2C3E50',
                                           corner_radius=cor_radius_std, text_font='Verdana 11 bold', fg_color=('#E74C3C'),
                                           bg_color='black')
        st_lab_tp.grid(row=12, column=20, columnspan=5, pady=1)

        st_lab_final = customtkinter.CTkLabel(window_ko, text='GRAND FINAL', width=80, height=23, bg='#2C3E50',
                                              corner_radius=cor_radius_std, text_font='Verdana 13 bold', fg_color=('#E74C3C'),
                                              bg_color='black')
        st_lab_final.grid(row=7, column=20, columnspan=5, pady=1)

        match_date_tp = customtkinter.CTkLabel(window_ko, text='Sat, 17.Dec', border=1, width=2, height=1,
                                               borderwidth=1, corner_radius=cor_radius_std,
                                               text_font='Verdana 9 italic',
                                               bg_color=bg_col_std, fg_color=(fg_col_std))
        match_date_tp.grid(row=13, column=20, columnspan=5, pady=1)

        match_date_final = customtkinter.CTkLabel(window_ko, text='Sun, 18.Dec', border=1, width=2, height=1,
                                                  borderwidth=1, corner_radius=cor_radius_std,
                                                  text_font='Verdana 9 italic',
                                                  bg_color=bg_col_std, fg_color=(fg_col_std))
        match_date_final.grid(row=8, column=20, columnspan=5)

        t1_tp = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                       borderwidth=1,
                                       corner_radius=cor_radius_std, text_font=labfont,
                                       bg_color=bg_col_std, fg_color=(fg_color_teams))
        t1_tp.grid(row=14, column=20, sticky=E)

        m1 = customtkinter.CTkLabel(window_ko, text='-', border=1, width=2, height=1, borderwidth=1,
                                    corner_radius=cor_radius_std, text_font=labfont,
                                    bg_color=bg_col_std, fg_color=(fg_color_teams))
        m1.grid(row=14, column=22)

        t2_tp = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                       borderwidth=1,
                                       corner_radius=cor_radius_std, text_font=labfont,
                                       bg_color=bg_col_std, fg_color=(fg_color_teams))
        t2_tp.grid(row=14, column=24, sticky=W)

        t1_final = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                          borderwidth=1,
                                          corner_radius=cor_radius_std, text_font='Verdana 10 bold',
                                          bg_color=bg_col_std, fg_color=(fg_color_teams))
        t1_final.grid(row=9, column=20, sticky=E)

        m1_final = customtkinter.CTkLabel(window_ko, text='-', border=1, width=2, height=1, borderwidth=1,
                                          corner_radius=cor_radius_std, text_font=labfont,
                                          bg_color=bg_col_std, fg_color=(fg_color_teams))
        m1_final.grid(row=9, column=22)

        t2_final = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                          borderwidth=1,
                                          corner_radius=cor_radius_std, text_font='Verdana 10 bold',
                                          bg_color=bg_col_std, fg_color=(fg_color_teams))
        t2_final.grid(row=9, column=24, sticky=W)

        # winners ----------------------------------------------------

        sec_ = customtkinter.CTkLabel(window_ko, text='2ND', border=1, width=2, height=1,
                                      borderwidth=1,
                                      corner_radius=cor_radius_std, text_font='Verdana 10 bold',
                                      bg_color=bg_col_std, fg_color=(fg_color_teams))
        sec_.grid(row=14, column=26, padx=1, pady=2)

        sec_team = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                          borderwidth=1,
                                          corner_radius=cor_radius_std, text_font='Verdana 11 bold',
                                          bg_color=bg_col_std, fg_color=('#D5DBDB'))  # silver
        sec_team.grid(row=14, column=27, padx=1, pady=2)

        thi_ = customtkinter.CTkLabel(window_ko, text='3RD', border=1, width=2, height=1,
                                      borderwidth=1,
                                      corner_radius=cor_radius_std, text_font='Verdana 10 bold',
                                      bg_color=bg_col_std, fg_color=(fg_color_teams))
        thi_.grid(row=15, column=26, padx=1)

        thi_team = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2, height=1,
                                          borderwidth=1,
                                          corner_radius=cor_radius_std, text_font='Verdana 11 bold',
                                          bg_color=bg_col_std, fg_color=('#Cd7f32'))  # bronze
        thi_team.grid(row=15, column=27, padx=1)

        winner_team = customtkinter.CTkLabel(window_ko, text='...', border=1, width=2,
                                             height=1,
                                             borderwidth=1,
                                             corner_radius=cor_radius_std, text_font='Verdana 14 bold',
                                             bg_color=bg_col_std, fg_color=('#FFD700'))  # gold
        winner_team.grid(row=10, column=27, padx=5, pady=10)

    matches_finals()

    # entries R 16

    score_m49t1 = StringVar()
    ent_m49t1 = Entry(window_ko, textvariable=score_m49t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m49t1.grid(row=2, column=3)

    score_m49t2 = StringVar()
    ent_m49t2 = Entry(window_ko, textvariable=score_m49t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m49t2.grid(row=2, column=5)

    score_m50t1 = StringVar()
    ent_m50t1 = Entry(window_ko, textvariable=score_m50t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m50t1.grid(row=4, column=3)

    score_m50t2 = StringVar()
    ent_m50t2 = Entry(window_ko, textvariable=score_m50t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m50t2.grid(row=4, column=5)

    score_m51t1 = StringVar()
    ent_m51t1 = Entry(window_ko, textvariable=score_m51t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m51t1.grid(row=6, column=3)

    score_m51t2 = StringVar()
    ent_m51t2 = Entry(window_ko, textvariable=score_m51t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m51t2.grid(row=6, column=5)

    score_m52t1 = StringVar()
    ent_m52t1 = Entry(window_ko, textvariable=score_m52t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m52t1.grid(row=8, column=3)

    score_m52t2 = StringVar()
    ent_m52t2 = Entry(window_ko, textvariable=score_m52t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m52t2.grid(row=8, column=5)

    score_m53t1 = StringVar()
    ent_m53t1 = Entry(window_ko, textvariable=score_m53t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m53t1.grid(row=11, column=3)

    score_m53t2 = StringVar()
    ent_m53t2 = Entry(window_ko, textvariable=score_m53t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m53t2.grid(row=11, column=5)

    score_m54t1 = StringVar()
    ent_m54t1 = Entry(window_ko, textvariable=score_m54t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m54t1.grid(row=13, column=3)

    score_m54t2 = StringVar()
    ent_m54t2 = Entry(window_ko, textvariable=score_m54t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m54t2.grid(row=13, column=5)

    score_m55t1 = StringVar()
    ent_m55t1 = Entry(window_ko, textvariable=score_m55t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m55t1.grid(row=15, column=3)

    score_m55t2 = StringVar()
    ent_m55t2 = Entry(window_ko, textvariable=score_m55t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m55t2.grid(row=15, column=5)

    score_m56t1 = StringVar()
    ent_m56t1 = Entry(window_ko, textvariable=score_m56t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m56t1.grid(row=17, column=3)

    score_m56t2 = StringVar()
    ent_m56t2 = Entry(window_ko, textvariable=score_m56t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m56t2.grid(row=17, column=5)

    # entries QF

    score_m57t1 = StringVar()
    ent_m57t1 = Entry(window_ko, textvariable=score_m57t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m57t1.grid(row=3, column=9)

    score_m57t2 = StringVar()
    ent_m57t2 = Entry(window_ko, textvariable=score_m57t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m57t2.grid(row=3, column=11)

    score_m58t1 = StringVar()
    ent_m58t1 = Entry(window_ko, textvariable=score_m58t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m58t1.grid(row=7, column=9)

    score_m58t2 = StringVar()
    ent_m58t2 = Entry(window_ko, textvariable=score_m58t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m58t2.grid(row=7, column=11)

    score_m59t1 = StringVar()
    ent_m59t1 = Entry(window_ko, textvariable=score_m59t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m59t1.grid(row=12, column=9)

    score_m59t2 = StringVar()
    ent_m59t2 = Entry(window_ko, textvariable=score_m59t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m59t2.grid(row=12, column=11)

    score_m60t1 = StringVar()
    ent_m60t1 = Entry(window_ko, textvariable=score_m60t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m60t1.grid(row=16, column=9)

    score_m60t2 = StringVar()
    ent_m60t2 = Entry(window_ko, textvariable=score_m60t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m60t2.grid(row=16, column=11)

    # entries SF

    score_m61t1 = StringVar()
    ent_m61t1 = Entry(window_ko, textvariable=score_m61t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m61t1.grid(row=5, column=15)

    score_m61t2 = StringVar()
    ent_m61t2 = Entry(window_ko, textvariable=score_m61t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m61t2.grid(row=5, column=17)

    score_m62t1 = StringVar()
    ent_m62t1 = Entry(window_ko, textvariable=score_m62t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m62t1.grid(row=14, column=15)

    score_m62t2 = StringVar()
    ent_m62t2 = Entry(window_ko, textvariable=score_m62t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m62t2.grid(row=14, column=17)

    # entries FINALS

    score_m63t1 = StringVar()
    ent_m63t1 = Entry(window_ko, textvariable=score_m63t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m63t1.grid(row=14, column=21)

    score_m63t2 = StringVar()
    ent_m63t2 = Entry(window_ko, textvariable=score_m63t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m63t2.grid(row=14, column=23)

    score_m64t1 = StringVar()
    ent_m64t1 = Entry(window_ko, textvariable=score_m64t1, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m64t1.grid(row=9, column=21)

    score_m64t2 = StringVar()
    ent_m64t2 = Entry(window_ko, textvariable=score_m64t2, font=labfont, width=width_ent_sc, bg=bg_ent_sc, bd=bd_ent_sc)
    ent_m64t2.grid(row=9, column=23)

    # -------------------------------------------------------------------

    def r16_to_qf():
        wc22_bend.update_round16('gra', 'grb', 49)
        wc22_bend.update_round16('grc', 'grd', 50)
        wc22_bend.update_round16('grb', 'gra', 51)
        wc22_bend.update_round16('grd', 'grc', 52)
        wc22_bend.update_round16('gre', 'grf', 53)
        wc22_bend.update_round16('grg', 'grh', 54)
        wc22_bend.update_round16('grf', 'gre', 55)
        wc22_bend.update_round16('grh', 'grg', 56)
        # try:
        wc22_bend.update_qf(ent_m49t1.get(), ent_m49t2.get(), ent_m50t1.get(), ent_m50t2.get(), ent_m51t1.get(),
                            ent_m51t2.get(), ent_m52t1.get(), ent_m52t2.get(), ent_m54t1.get(), ent_m54t2.get(),
                            ent_m53t1.get(), ent_m53t2.get(), ent_m56t1.get(), ent_m56t2.get(), ent_m55t1.get(),
                            ent_m55t2.get(), 49, 50, 57)
        wc22_bend.update_qf(ent_m49t1.get(), ent_m49t2.get(), ent_m50t1.get(), ent_m50t2.get(), ent_m51t1.get(),
                            ent_m51t2.get(), ent_m52t1.get(), ent_m52t2.get(), ent_m54t1.get(), ent_m54t2.get(),
                            ent_m53t1.get(), ent_m53t2.get(), ent_m56t1.get(), ent_m56t2.get(), ent_m55t1.get(),
                            ent_m55t2.get(), 53, 54, 58)
        wc22_bend.update_qf(ent_m49t1.get(), ent_m49t2.get(), ent_m50t1.get(), ent_m50t2.get(), ent_m51t1.get(),
                            ent_m51t2.get(), ent_m52t1.get(), ent_m52t2.get(), ent_m54t1.get(), ent_m54t2.get(),
                            ent_m53t1.get(), ent_m53t2.get(), ent_m56t1.get(), ent_m56t2.get(), ent_m55t1.get(),
                            ent_m55t2.get(), 51, 52, 59)
        wc22_bend.update_qf(ent_m49t1.get(), ent_m49t2.get(), ent_m50t1.get(), ent_m50t2.get(), ent_m51t1.get(),
                            ent_m51t2.get(), ent_m52t1.get(), ent_m52t2.get(), ent_m54t1.get(), ent_m54t2.get(),
                            ent_m53t1.get(), ent_m53t2.get(), ent_m56t1.get(), ent_m56t2.get(), ent_m55t1.get(),
                            ent_m55t2.get(), 55, 56, 60)

    def qf_to_sf():
        wc22_bend.update_sf(ent_m57t1.get(), ent_m57t2.get(), ent_m58t1.get(), ent_m58t2.get(), ent_m59t1.get(),
                            ent_m59t2.get(), ent_m60t1.get(), ent_m60t2.get(), 57, 58, 61)
        wc22_bend.update_sf(ent_m57t1.get(), ent_m57t2.get(), ent_m58t1.get(), ent_m58t2.get(), ent_m59t1.get(),
                            ent_m59t2.get(), ent_m60t1.get(), ent_m60t2.get(), 59, 60, 62)

    def sf_to_f():
        wc22_bend.update_fin(ent_m61t1.get(), ent_m61t2.get(), ent_m62t1.get(), ent_m62t2.get())

    def f_to_winners():
        wc22_bend.decide_winners(ent_m63t1.get(), ent_m63t2.get(), ent_m64t1.get(), ent_m64t2.get())

    def view_qf():
        def inner(ro, col, txt):
            t1 = customtkinter.CTkLabel(window_ko, text=txt, border=1, width=2, height=1,
                                        borderwidth=1,
                                        corner_radius=cor_radius_std, text_font=labfont,
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            t1.grid(row=ro, column=col)

        if wc22_bend.show_qf_abbr()[0] != None:
            inner(3, 8, wc22_bend.show_qf_abbr()[0])
        if wc22_bend.show_qf_abbr()[1] != None:
            inner(3, 12, wc22_bend.show_qf_abbr()[1])
        if wc22_bend.show_qf_abbr()[2] != None:
            inner(7, 8, wc22_bend.show_qf_abbr()[2])
        if wc22_bend.show_qf_abbr()[3] != None:
            inner(7, 12, wc22_bend.show_qf_abbr()[3])

        if wc22_bend.show_qf_abbr()[4] != None:
            inner(12, 8, wc22_bend.show_qf_abbr()[4])
        if wc22_bend.show_qf_abbr()[5] != None:
            inner(12, 12, wc22_bend.show_qf_abbr()[5])
        if wc22_bend.show_qf_abbr()[6] != None:
            inner(16, 8, wc22_bend.show_qf_abbr()[6])
        if wc22_bend.show_qf_abbr()[7] != None:
            inner(16, 12, wc22_bend.show_qf_abbr()[7])

    def view_sf():
        def inner(ro, col, txt):
            t1 = customtkinter.CTkLabel(window_ko, text=txt, border=1, width=2, height=1,
                                        borderwidth=1,
                                        corner_radius=cor_radius_std, text_font=labfont,
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            t1.grid(row=ro, column=col)

        if wc22_bend.show_sf_abbr()[0] != None:
            inner(5, 14, wc22_bend.show_sf_abbr()[0])
        if wc22_bend.show_sf_abbr()[1] != None:
            inner(5, 18, wc22_bend.show_sf_abbr()[1])

        if wc22_bend.show_sf_abbr()[2] != None:
            inner(14, 14, wc22_bend.show_sf_abbr()[2])
        if wc22_bend.show_sf_abbr()[3] != None:
            inner(14, 18, wc22_bend.show_sf_abbr()[3])

    def view_f():
        def inner(ro, col, txt):
            t1 = customtkinter.CTkLabel(window_ko, text=txt, border=1, width=2, height=1,
                                        borderwidth=1,
                                        corner_radius=cor_radius_std, text_font='Verdana 10 bold',
                                        bg_color=bg_col_std, fg_color=(fg_color_teams))
            t1.grid(row=ro, column=col)

        if wc22_bend.show_fin_abbr()[2] != None:
            inner(9, 20, wc22_bend.show_fin_abbr()[2])
        if wc22_bend.show_fin_abbr()[3] != None:
            inner(9, 24, wc22_bend.show_fin_abbr()[3])

        if wc22_bend.show_fin_abbr()[0] != None:
            inner(14, 20, wc22_bend.show_fin_abbr()[0])
        if wc22_bend.show_fin_abbr()[1] != None:
            inner(14, 24, wc22_bend.show_fin_abbr()[1])

    def view_winners():

        if wc22_bend.show_winners()[2] != None:
            thi_team = customtkinter.CTkLabel(window_ko, text=wc22_bend.show_winners()[2], border=1, width=2, height=1,
                                              borderwidth=1,
                                              corner_radius=cor_radius_std, text_font='Verdana 11 bold',
                                              bg_color=bg_col_std, fg_color=('#Cd7f32'))  # bronze
            thi_team.grid(row=15, column=27, padx=4)

        if wc22_bend.show_winners()[1] != None:
            sec_team = customtkinter.CTkLabel(window_ko, text=wc22_bend.show_winners()[1], border=1, width=2, height=1,
                                              borderwidth=1,
                                              corner_radius=cor_radius_std, text_font='Verdana 11 bold',
                                              bg_color=bg_col_std, fg_color=('#D5DBDB'))  # silver
            sec_team.grid(row=14, column=27, padx=4, pady=2)

        if wc22_bend.show_winners()[0] != None:
            winner_team = customtkinter.CTkLabel(window_ko, text=wc22_bend.show_winners()[0], border=1, width=2,
                                                 height=1,
                                                 borderwidth=1,
                                                 corner_radius=cor_radius_std, text_font='Verdana 14 bold',
                                                 bg_color=bg_col_std, fg_color=('#FFD700'))  # gold
            winner_team.grid(row=10, column=27, padx=0, pady=10, sticky=W)

    # update and info buttons

    def confirm_update_r16():
        window_confirm_r16 = Tk()
        window_confirm_r16.title('Confirm Update Round of 16')
        window_confirm_r16.geometry('400x150')
        window_confirm_r16.iconbitmap('img_icon.ico')
        window_confirm_r16.configure(bg='black')
        f_destroy = window_confirm_r16.destroy
        lavert = Label(window_confirm_r16, text='Before updating any match, you have to be sure that you have pressed'
                                                '"SHOW DATA" button, otherwise all previous saved matches will be lost.',
                       font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        btn_update_yes = Button(window_confirm_r16, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                                font='Verdana 7 bold', command=lambda: [r16_to_qf(), view_qf(), f_destroy()])
        btn_update_yes.grid(row=4, column=1, sticky=E, padx=10, pady=10)

        btn_update_no = Button(window_confirm_r16, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                               command=window_confirm_r16.destroy)
        btn_update_no.grid(row=4, column=2, sticky=W, padx=10, pady=10)

        window_confirm_r16.mainloop()

    def confirm_update_qf():
        window_confirm_qf = Tk()
        window_confirm_qf.title('Confirm Update Qater Finals')
        window_confirm_qf.geometry('400x150')
        window_confirm_qf.iconbitmap('img_icon.ico')
        window_confirm_qf.configure(bg='black')
        f_destroy = window_confirm_qf.destroy
        lavert = Label(window_confirm_qf, text='Before updating any match, you have to be sure that you have pressed'
                                               '"SHOW DATA" button, otherwise all previous saved matches will be lost.',
                       font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        btn_update_yes = Button(window_confirm_qf, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                                font='Verdana 7 bold', command=lambda: [qf_to_sf(), view_sf(), f_destroy()])
        btn_update_yes.grid(row=4, column=1, sticky=E, padx=10, pady=10)

        btn_update_no = Button(window_confirm_qf, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                               command=window_confirm_qf.destroy)
        btn_update_no.grid(row=4, column=2, sticky=W, padx=10, pady=10)

        window_confirm_qf.mainloop()

    def confirm_update_sf():
        window_confirm_sf = Tk()
        window_confirm_sf.title('Confirm Update Semi Finals')
        window_confirm_sf.geometry('400x150')
        window_confirm_sf.iconbitmap('img_icon.ico')
        window_confirm_sf.configure(bg='black')
        f_destroy = window_confirm_sf.destroy
        lavert = Label(window_confirm_sf, text='Before updating any match, you have to be sure that you have pressed'
                                               '"SHOW DATA" button, otherwise all previous saved matches will be lost.',
                       font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        btn_update_yes = Button(window_confirm_sf, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                                font='Verdana 7 bold', command=lambda: [sf_to_f(), view_f(), f_destroy()])
        btn_update_yes.grid(row=4, column=1, sticky=E, padx=10, pady=10)

        btn_update_no = Button(window_confirm_sf, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                               command=window_confirm_sf.destroy)
        btn_update_no.grid(row=4, column=2, sticky=W, padx=10, pady=10)

        window_confirm_sf.mainloop()

    def confirm_update_f():
        window_confirm_f = Tk()
        window_confirm_f.title('Confirm Update Finals')
        window_confirm_f.geometry('400x150')
        window_confirm_f.iconbitmap('img_icon.ico')
        window_confirm_f.configure(bg='black')
        f_destroy = window_confirm_f.destroy
        lavert = Label(window_confirm_f, text='Before updating any match, you have to be sure that you have pressed'
                                              '"SHOW DATA" button, otherwise all previous saved matches will be lost.',
                       font=labfont, bg='black', fg='white', anchor=CENTER, wraplength=360)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        btn_update_yes = Button(window_confirm_f, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                                font='Verdana 7 bold', command=lambda: [f_to_winners(), view_winners(), f_destroy()])
        btn_update_yes.grid(row=4, column=1, sticky=E, padx=10, pady=10)

        btn_update_no = Button(window_confirm_f, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                               command=window_confirm_f.destroy)
        btn_update_no.grid(row=4, column=2, sticky=W, padx=10, pady=10)

        window_confirm_f.mainloop()

    # ----------------------------------

    def update_button_fin():
        def inner(col, cmd):
            btn_update = Button(window_ko, text='UPDATE', command=cmd, bg=fg_color_teams, fg='darkblue', bd=3,
                                font='Verdana 7 bold')
            btn_update.grid(row=19, column=col, pady=15)

        inner(4, cmd=confirm_update_r16)
        inner(10, cmd=confirm_update_qf)
        inner(16, cmd=confirm_update_sf)
        inner(22, cmd=confirm_update_f)

    update_button_fin()

    def show_data_finals():
        view_qf()
        view_sf()
        view_f()
        view_winners()

        if len(ent_m49t1.get()) < 1:
            # r16
            ent_m49t1.insert(END, wc22_bend.show_data_r16()[0][0])
            ent_m49t2.insert(END, wc22_bend.show_data_r16()[0][1])
            ent_m50t1.insert(END, wc22_bend.show_data_r16()[1][0])
            ent_m50t2.insert(END, wc22_bend.show_data_r16()[1][1])
            ent_m51t1.insert(END, wc22_bend.show_data_r16()[2][0])
            ent_m51t2.insert(END, wc22_bend.show_data_r16()[2][1])
            ent_m52t1.insert(END, wc22_bend.show_data_r16()[3][0])
            ent_m52t2.insert(END, wc22_bend.show_data_r16()[3][1])

            ent_m53t1.insert(END, wc22_bend.show_data_r16()[4][0])
            ent_m53t2.insert(END, wc22_bend.show_data_r16()[4][1])
            ent_m54t1.insert(END, wc22_bend.show_data_r16()[5][0])
            ent_m54t2.insert(END, wc22_bend.show_data_r16()[5][1])
            ent_m55t1.insert(END, wc22_bend.show_data_r16()[6][0])
            ent_m55t2.insert(END, wc22_bend.show_data_r16()[6][1])
            ent_m56t1.insert(END, wc22_bend.show_data_r16()[7][0])
            ent_m56t2.insert(END, wc22_bend.show_data_r16()[7][1])

            # qf
            ent_m57t1.insert(END, wc22_bend.show_data_qf()[0][0])
            ent_m57t2.insert(END, wc22_bend.show_data_qf()[0][1])
            ent_m58t1.insert(END, wc22_bend.show_data_qf()[1][0])
            ent_m58t2.insert(END, wc22_bend.show_data_qf()[1][1])

            ent_m59t1.insert(END, wc22_bend.show_data_qf()[2][0])
            ent_m59t2.insert(END, wc22_bend.show_data_qf()[2][1])
            ent_m60t1.insert(END, wc22_bend.show_data_qf()[3][0])
            ent_m60t2.insert(END, wc22_bend.show_data_qf()[3][1])

            # sf
            ent_m61t1.insert(END, wc22_bend.show_data_sf()[0][0])
            ent_m61t2.insert(END, wc22_bend.show_data_sf()[0][1])

            ent_m62t1.insert(END, wc22_bend.show_data_sf()[1][0])
            ent_m62t2.insert(END, wc22_bend.show_data_sf()[1][1])

            # fin
            ent_m63t1.insert(END, wc22_bend.show_data_fin()[0][0])
            ent_m63t2.insert(END, wc22_bend.show_data_fin()[0][1])

            ent_m64t1.insert(END, wc22_bend.show_data_fin()[1][0])
            ent_m64t2.insert(END, wc22_bend.show_data_fin()[1][1])

        else:
            all_updated()

    b_show_data_fin = Button(window_ko, text='SHOW DATA', command=show_data_finals, bg='#65C252', width=13, bd=5,
                             font='Verdana 8 bold')
    b_show_data_fin.grid(row=20, column=26)

    def info_49():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 49)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        info_ent.insert(END, wc22_bend.get_info('matches_r16', 49)[0])  # ------------

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_50():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 50)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        info_ent.insert(END, wc22_bend.get_info('matches_r16', 50)[0])  # ------------

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_51():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 51)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 51)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_52():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 52)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 52)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_53():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 53)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 53)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_54():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 54)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 54)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_55():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 55)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 55)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_56():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_r16", 56)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_r16(info_ent.get(), 56)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_57():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_qf", 57)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_qf(info_ent.get(), 57)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_58():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_qf", 58)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_qf(info_ent.get(), 58)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_59():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_qf", 59)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_qf(info_ent.get(), 59)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_60():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_qf", 60)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_qf(info_ent.get(), 60)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_61():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_sf", 61)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_sf(info_ent.get(), 61)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_62():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_sf", 62)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_sf(info_ent.get(), 62)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_63():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_fin", 63)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_fin(info_ent.get(), 63)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_64():
        window_info = Tk()
        window_info.title('Information match')
        window_info.geometry('450x200')
        window_info.iconbitmap('img_icon.ico')
        window_info.configure(bg='#6B6E6E')
        lavert = Label(window_info,
                       text='Update information about the match! (ex: extra-time win, penalty shootout win, red cards)...',
                       font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER, wraplength=400)
        lavert.grid(row=0, column=1, rowspan=2, columnspan=2, padx=15, pady=15)
        info_E = StringVar()
        info_ent = Entry(window_info, textvariable=info_E, font=labfont, width=40, bg=bg_ent_sc,
                         bd=bd_ent_sc)
        info_ent.grid(row=3, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

        info_ent.insert(END, wc22_bend.get_info("matches_fin", 64)[0])  # ------------------

        def f_update():
            wc22_bend.update_info_fin(info_ent.get(), 64)  # ------------
            window_updated = Tk()
            window_updated.title('Updated')
            window_updated.configure(bg='#6B6E6E')
            window_updated.geometry('200x70')
            lavert = Label(window_updated,
                           text='UPDATED!', font=labfont, bg='#6B6E6E', fg='white', anchor=CENTER)
            lavert.grid(row=0, column=1, rowspan=2, columnspan=3, padx=60, pady=15)
            window_updated.iconbitmap('img_icon.ico')
            window_updated.mainloop()

        btn_update = Button(window_info, text='UPDATE', bg=fg_color_teams, fg='darkblue', bd=3,
                            font='Verdana 7 bold', command=f_update)
        btn_update.grid(row=5, column=1, sticky=E, padx=10, pady=10)

        btn_close = Button(window_info, text='CLOSE', bg='#65C252', bd=3, font='Verdana 7 bold',
                           command=window_info.destroy)
        btn_close.grid(row=5, column=2, sticky=W, padx=10, pady=10)

        window_info.mainloop()

    def info_button():
        def inner(ro, col, cmd):
            btn_update = Button(window_ko, text='i', command=cmd, bg='#2B2B2B', fg='aliceblue', font='Courier 7')
            btn_update.grid(row=ro, column=col, pady=2, sticky=N)

        inner(3, 4, cmd=info_49)
        inner(5, 4, cmd=info_50)
        inner(7, 4, cmd=info_51)
        inner(9, 4, cmd=info_52)
        inner(12, 4, cmd=info_53)
        inner(14, 4, cmd=info_54)
        inner(16, 4, cmd=info_55)
        inner(18, 4, cmd=info_56)

        inner(4, 10, cmd=info_57)
        inner(8, 10, cmd=info_58)
        inner(13, 10, cmd=info_59)
        inner(17, 10, cmd=info_60)

        inner(6, 16, cmd=info_61)
        inner(15, 16, cmd=info_62)

        inner(10, 22, cmd=info_63)
        inner(15, 22, cmd=info_64)

    info_button()

    window_ko.mainloop()


def update_round_16():
    wc22_bend.update_round16('gra', 'grb', 49)
    wc22_bend.update_round16('grc', 'grd', 50)
    wc22_bend.update_round16('grb', 'gra', 51)
    wc22_bend.update_round16('grd', 'grc', 52)
    wc22_bend.update_round16('gre', 'grf', 53)
    wc22_bend.update_round16('grg', 'grh', 54)
    wc22_bend.update_round16('grf', 'gre', 55)
    wc22_bend.update_round16('grh', 'grg', 56)


b_finals = Button(window, text='FINAL STAGES', command=lambda: [func_final_stages(), update_round_16()],
                  bg='#FFD700', fg='darkblue',  width=13, bd=5, font='Verdana 9 bold')
b_finals.grid(row=30, column=46, sticky=N)

b_reset = Button(window, text='RESET DATA', command=confirm_reset,
                 bg='#D5333A', fg='darkblue', width=10, bd=4, font='Verdana 6 bold')
b_reset.grid(row=31, column=1, sticky=S, pady=10)

window.mainloop()
