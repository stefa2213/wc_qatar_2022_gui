import sqlite3
from pprint import pprint


# general ----------------------
def connect_db():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # create groups
    cur.execute('CREATE TABLE IF NOT EXISTS grA (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grB (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grC (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grD (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grE (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grF (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grG (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')
    cur.execute('CREATE TABLE IF NOT EXISTS grH (team_id int primary key,team varchar(50), abbr varchar(3), '
                'name varchar(15), mp int,gd int,pts int)')

    # create matches tables
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_a (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES gra(team_id),FOREIGN KEY (team_id2) REFERENCES gra(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_b (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grb(team_id),FOREIGN KEY (team_id2) REFERENCES grb(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_c (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grc(team_id),FOREIGN KEY (team_id2) REFERENCES grc(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_d (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grd(team_id),FOREIGN KEY (team_id2) REFERENCES grd(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_e (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES gre(team_id),FOREIGN KEY (team_id2) REFERENCES gre(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_f (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grf(team_id),FOREIGN KEY (team_id2) REFERENCES grf(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_g (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grg(team_id),FOREIGN KEY (team_id2) REFERENCES grg(team_id))')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS matches_h (match_id int primary key,team_id int,score1 int,score2 int,'
        'team_id2 int,FOREIGN KEY (team_id) REFERENCES grh(team_id),FOREIGN KEY (team_id2) REFERENCES grh(team_id))')

    # create tables final stages
    cur.execute('CREATE TABLE IF NOT EXISTS matches_r16 ('
                'match_id int primary key,'
                'team_id int,'
                'team1_name varchar(20),'
                'team1_abbr varchar(3),'
                'score1 int,'
                'score2 int,'
                'team2_abbr varchar(3),'
                'team2_name varchar(20),'
                'info varchar(120),'
                'FOREIGN KEY (team_id) REFERENCES gra(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grb(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grc(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grd(team_id),'
                'FOREIGN KEY (team_id) REFERENCES gre(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grf(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grg(team_id),'
                'FOREIGN KEY (team_id) REFERENCES grh(team_id))')

    cur.execute('CREATE TABLE IF NOT EXISTS matches_qf ('
                'match_id int primary key,'
                'team_id int,'
                'team1_name varchar(20),'
                'team1_abbr varchar(3),'
                'score1 int,'
                'score2 int,'
                'team2_abbr varchar(3),'
                'team2_name varchar(20),'
                'info varchar(120),'
                'FOREIGN KEY (team_id) REFERENCES matches_r16(team_id))')

    cur.execute('CREATE TABLE IF NOT EXISTS matches_sf ('
                'match_id int primary key,'
                'team_id int,'
                'team1_name varchar(20),'
                'team1_abbr varchar(3),'
                'score1 int,'
                'score2 int,'
                'team2_abbr varchar(3),'
                'team2_name varchar(20),'
                'info varchar(120),'
                'FOREIGN KEY (team_id) REFERENCES matches_qf(team_id))')

    cur.execute('CREATE TABLE IF NOT EXISTS matches_fin ('
                'match_id int primary key,'
                'team_id int,'
                'team1_name varchar(20),'
                'team1_abbr varchar(3),'
                'score1 int,'
                'score2 int,'
                'team2_abbr varchar(3),'
                'team2_name varchar(20),'
                'info varchar(120),'
                'FOREIGN KEY (team_id) REFERENCES matches_sf(team_id))')

    conn.commit()
    conn.close()


def add_group():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # A
    cur.execute('insert into grA  values (1, "Qatar (QAT)", "QAT", "Qatar", 0,0,0)')
    cur.execute('insert into grA  values (2, "Ecuador (ECU)", "ECU", "Ecuador", 0,0,0)')
    cur.execute('insert into grA values (3, "Senegal (SEN)", "SEN", "Senegal", 0,0,0)')
    cur.execute('insert into grA values (4, "Netherlands (NED)", "NED", "Netherlands", 0,0,0)')
    # B
    cur.execute('insert into grB  values (1, "England (ENG)", "ENG", "England", 0,0,0)')
    cur.execute('insert into grB  values (2, "Iran (IRN)", "IRN", "Iran", 0,0,0)')
    cur.execute('insert into grB values (3, "USA (USA)", "USA", "USA", 0,0,0)')
    cur.execute('insert into grB values (4, "Wales (WAL)", "WAL", "Wales", 0,0,0)')
    # C
    cur.execute('insert into grC  values (1, "Argentina (ARG)", "ARG", "Argentina", 0,0,0)')
    cur.execute('insert into grC  values (2, "Saudi Arabia (KSA)", "KSA", "Saudi Arabia", 0,0,0)')
    cur.execute('insert into grC values (3, "Mexico (MEX)", "MEX", "Mexico", 0,0,0)')
    cur.execute('insert into grC values (4, "Poland (POL)", "POL", "Poland", 0,0,0)')
    # D
    cur.execute('insert into grD  values (1, "France (FRA)", "FRA", "France", 0,0,0)')
    cur.execute('insert into grD  values (2, "Australia (AUS)", "AUS", "Australia", 0,0,0)')
    cur.execute('insert into grD values (3, "Denmark (DEN)", "DEN", "Denmark", 0,0,0)')
    cur.execute('insert into grD values (4, "Tunisia (TUN)", "TUN", "Tunisia", 0,0,0)')
    # E
    cur.execute('insert into grE  values (1, "Spain  (ESP)", "ESP", "Spain", 0,0,0)')
    cur.execute('insert into grE  values (2, "Costa Rica (CRC)", "CRC", "Costa Rica", 0,0,0)')
    cur.execute('insert into grE values (3, "Germany (GER)", "GER", "Germany", 0,0,0)')
    cur.execute('insert into grE values (4, "Japan (JPN)", "JPN", "Japan", 0,0,0)')
    # F
    cur.execute('insert into grF  values (1, "Belgium  (BEL)", "BEL", "Belgium", 0,0,0)')
    cur.execute('insert into grF  values (2, "Canada (CAN)", "CAN", "Canada", 0,0,0)')
    cur.execute('insert into grF values (3, "Morocco (MAR)", "MAR", "Morocco", 0,0,0)')
    cur.execute('insert into grF values (4, "Croatia (CRO)", "CRO", "Croatia", 0,0,0)')
    # G
    cur.execute('insert into grG  values (1, "Brazil  (BRA)", "BRA", "Brazil", 0,0,0)')
    cur.execute('insert into grG  values (2, "Serbia (SRB)", "SRB", "Serbia", 0,0,0)')
    cur.execute('insert into grG values (3, "Switzerland (SUI)", "SUI", "Switzerland", 0,0,0)')
    cur.execute('insert into grG values (4, "Cameroon (CMR)", "CMR", "Cameroon", 0,0,0)')
    # H
    cur.execute('insert into grH  values (1, "Portugal  (POR)", "POR", "Portugal", 0,0,0)')
    cur.execute('insert into grH  values (2, "Ghana (GHA)", "GHA", "Ghana", 0,0,0)')
    cur.execute('insert into grH values (3, "Uruguay (URU)", "URU", "Uruguay", 0,0,0)')
    cur.execute('insert into grH values (4, "Korea Republic (KOR)", "KOR", "South Korea", 0,0,0)')

    conn.commit()
    conn.close()


def add_matches():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # A
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (1,1,2)')
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (2,3,4)')
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (3,4,2)')
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (4,1,3)')
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (5,4,1)')
    cur.execute('insert into matches_a (match_id, team_id,  team_id2) values (6,2,3)')
    # B
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (1,1,2)')
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (2,3,4)')
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (5,2,3)')
    cur.execute('insert into matches_b (match_id, team_id,  team_id2) values (6,4,1)')
    # C
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (1,1,2)')
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (2,3,4)')
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (5,2,3)')
    cur.execute('insert into matches_c (match_id, team_id,  team_id2) values (6,4,1)')
    # D
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (1,3,4)')
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (2,1,2)')
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (5,4,1)')
    cur.execute('insert into matches_d (match_id, team_id,  team_id2) values (6,2,3)')
    # E
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (1,3,4)')
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (2,1,2)')
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (5,2,3)')
    cur.execute('insert into matches_e (match_id, team_id,  team_id2) values (6,4,1)')
    # F
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (1,3,4)')
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (2,1,2)')
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (3,4,2)')
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (4,1,3)')
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (5,2,3)')
    cur.execute('insert into matches_f (match_id, team_id,  team_id2) values (6,4,1)')
    # G
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (1,1,2)')
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (2,3,4)')
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (5,4,1)')
    cur.execute('insert into matches_g (match_id, team_id,  team_id2) values (6,2,3)')
    # H
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (1,1,2)')
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (2,3,4)')
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (3,1,3)')
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (4,4,2)')
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (5,4,1)')
    cur.execute('insert into matches_h (match_id, team_id,  team_id2) values (6,2,3)')

    conn.commit()
    conn.close()


def add_matches_finals():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    # r16
    cur.execute('insert into matches_r16 (match_id, info) values (49, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (50, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (51, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (52, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (53, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (54, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (55, "Insert some info...")')
    cur.execute('insert into matches_r16 (match_id, info) values (56, "Insert some info...")')
    # qf
    cur.execute('insert into matches_qf (match_id, info) values (57, "Insert some info...")')
    cur.execute('insert into matches_qf (match_id, info) values (58, "Insert some info...")')
    cur.execute('insert into matches_qf (match_id, info) values (59, "Insert some info...")')
    cur.execute('insert into matches_qf (match_id, info) values (60, "Insert some info...")')
    # sf
    cur.execute('insert into matches_sf (match_id, info) values (61, "Insert some info...")')
    cur.execute('insert into matches_sf (match_id, info) values (62, "Insert some info...")')
    # f
    cur.execute('insert into matches_fin (match_id, info) values (63, "Insert some info...")')
    cur.execute('insert into matches_fin (match_id, info) values (64, "Insert some info...")')

    conn.commit()
    conn.close()


# group A -------------------

def update_match_a(sm1t1, sm1t2, sm2t1, sm2t2, sm3t1, sm3t2, sm4t1, sm4t2, sm5t1, sm5t2, sm6t1, sm6t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 1', (sm1t1, sm1t2))
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 2', (sm2t1, sm2t2))
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 3', (sm3t1, sm3t2))
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 4', (sm4t1, sm4t2))
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 5', (sm5t1, sm5t2))
    cur.execute('update matches_a set score1 = ?, score2 = ? where match_id = 6', (sm6t1, sm6t2))
    conn.commit()
    conn.close()


def update_group_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update gra set mp =(select count(match_id) from matches_a '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update gra set mp =(select count(match_id) from matches_a '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update gra set mp =(select count(match_id) from matches_a '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update gra set mp =(select count(match_id) from matches_a '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update gra set gd =('
                'COALESCE((select score1 - score2 from matches_a where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_a where match_id = 4), 0) + '
                'COALESCE((select score2 - score1 from matches_a where match_id = 5), 0)'
                ') where team_id =1')
    cur.execute('update gra set gd =('
                'COALESCE((select score2 - score1 from matches_a where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_a where match_id = 3), 0) + '
                'COALESCE((select score1 - score2 from matches_a where match_id = 6), 0)'
                ') where team_id =2')
    cur.execute('update gra set gd =('
                'COALESCE((select score1 - score2 from matches_a where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_a where match_id = 4), 0) + '
                'COALESCE((select score2 - score1 from matches_a where match_id = 6), 0)'
                ') where team_id =3')
    cur.execute('update gra set gd =('
                'COALESCE((select score2 - score1 from matches_a where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_a where match_id = 3), 0) + '
                'COALESCE((select score1 - score2 from matches_a where match_id = 5), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update gra set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_a where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_a where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_a where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_a where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update gra set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_a where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_a where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_a where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_a where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update gra set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_a where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_a where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_a where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_a where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update gra set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_a where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_a where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_a where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_a where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_a where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_matches_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT *  FROM matches_a')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_teams_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from gra order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grA order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grA order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grA order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_a():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_a')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group B -------------------------


def update_match_b(sm7t1, sm7t2, sm8t1, sm8t2, sm9t1, sm9t2, sm10t1, sm10t2, sm11t1, sm11t2, sm12t1, sm12t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 1', (sm7t1, sm7t2))
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 2', (sm8t1, sm8t2))
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 3', (sm9t1, sm9t2))
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 4', (sm10t1, sm10t2))
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 5', (sm11t1, sm11t2))
    cur.execute('update matches_b set score1 = ?, score2 = ? where match_id = 6', (sm12t1, sm12t2))
    conn.commit()
    conn.close()


def update_group_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grb set mp =(select count(match_id) from matches_b '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grb set mp =(select count(match_id) from matches_b '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grb set mp =(select count(match_id) from matches_b '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grb set mp =(select count(match_id) from matches_b '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grb set gd =('
                'COALESCE((select score1 - score2 from matches_b where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_b where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_b where match_id = 6), 0)'
                ') where team_id =1')
    cur.execute('update grb set gd =('
                'COALESCE((select score2 - score1 from matches_b where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_b where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_b where match_id = 5), 0)'
                ') where team_id =2')
    cur.execute('update grb set gd =('
                'COALESCE((select score1 - score2 from matches_b where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_b where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_b where match_id = 5), 0)'
                ') where team_id =3')
    cur.execute('update grb set gd =('
                'COALESCE((select score2 - score1 from matches_b where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_b where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_b where match_id = 6), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grb set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_b where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_b where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_b where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_b where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grb set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_b where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_b where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_b where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_b where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grb set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_b where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_b where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_b where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_b where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grb set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_b where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_b where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_b where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_b where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_b where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grb order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grB order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grB order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grB order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_b():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_b')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group C -------------------------

def update_match_c(sm13t1, sm13t2, sm14t1, sm14t2, sm15t1, sm15t2, sm16t1, sm16t2, sm17t1, sm17t2, sm18t1, sm18t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 1', (sm13t1, sm13t2))
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 2', (sm14t1, sm14t2))
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 3', (sm15t1, sm15t2))
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 4', (sm16t1, sm16t2))
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 5', (sm17t1, sm17t2))
    cur.execute('update matches_c set score1 = ?, score2 = ? where match_id = 6', (sm18t1, sm18t2))
    conn.commit()
    conn.close()


def update_group_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grc set mp =(select count(match_id) from matches_c '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grc set mp =(select count(match_id) from matches_c '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grc set mp =(select count(match_id) from matches_c '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grc set mp =(select count(match_id) from matches_c '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grc set gd =('
                'COALESCE((select score1 - score2 from matches_c where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_c where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_c where match_id = 6), 0)'
                ') where team_id =1')
    cur.execute('update grc set gd =('
                'COALESCE((select score2 - score1 from matches_c where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_c where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_c where match_id = 5), 0)'
                ') where team_id =2')
    cur.execute('update grc set gd =('
                'COALESCE((select score1 - score2 from matches_c where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_c where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_c where match_id = 5), 0)'
                ') where team_id =3')
    cur.execute('update grc set gd =('
                'COALESCE((select score2 - score1 from matches_c where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_c where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_c where match_id = 6), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grc set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_c where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_c where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_c where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_c where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grc set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_c where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_c where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_c where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_c where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grc set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_c where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_c where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_c where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_c where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grc set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_c where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_c where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_c where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_c where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_c where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grc order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grC order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grC order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grC order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_c():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_c')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group D-------------------------

def update_match_d(sm19t1, sm19t2, sm20t1, sm20t2, sm21t1, sm21t2, sm22t1, sm22t2, sm23t1, sm23t2, sm24t1, sm24t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 1', (sm19t1, sm19t2))
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 2', (sm20t1, sm20t2))
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 3', (sm21t1, sm21t2))
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 4', (sm22t1, sm22t2))
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 5', (sm23t1, sm23t2))
    cur.execute('update matches_d set score1 = ?, score2 = ? where match_id = 6', (sm24t1, sm24t2))
    conn.commit()
    conn.close()


def update_group_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grd set mp =(select count(match_id) from matches_d '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grd set mp =(select count(match_id) from matches_d '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grd set mp =(select count(match_id) from matches_d '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grd set mp =(select count(match_id) from matches_d '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grd set gd =('
                'COALESCE((select score1 - score2 from matches_d where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_d where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_d where match_id = 5), 0)'
                ') where team_id =1')
    cur.execute('update grd set gd =('
                'COALESCE((select score2 - score1 from matches_d where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_d where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_d where match_id = 6), 0)'
                ') where team_id =2')
    cur.execute('update grd set gd =('
                'COALESCE((select score1 - score2 from matches_d where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_d where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_d where match_id = 6), 0)'
                ') where team_id =3')
    cur.execute('update grd set gd =('
                'COALESCE((select score2 - score1 from matches_d where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_d where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_d where match_id = 5), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grd set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_d where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_d where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_d where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_d where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grd set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_d where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_d where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_d where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_d where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grd set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_d where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_d where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_d where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_d where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grd set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_d where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_d where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_d where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_d where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_d where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grd order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grD order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grD order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grD order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_d():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_d')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group E-------------------------

def update_match_e(sm25t1, sm25t2, sm26t1, sm26t2, sm27t1, sm27t2, sm28t1, sm28t2, sm29t1, sm29t2, sm30t1, sm30t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 1', (sm25t1, sm25t2))
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 2', (sm26t1, sm26t2))
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 3', (sm27t1, sm27t2))
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 4', (sm28t1, sm28t2))
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 5', (sm29t1, sm29t2))
    cur.execute('update matches_e set score1 = ?, score2 = ? where match_id = 6', (sm30t1, sm30t2))
    conn.commit()
    conn.close()


def update_group_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update gre set mp =(select count(match_id) from matches_e '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update gre set mp =(select count(match_id) from matches_e '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update gre set mp =(select count(match_id) from matches_e '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update gre set mp =(select count(match_id) from matches_e '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update gre set gd =('
                'COALESCE((select score1 - score2 from matches_e where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_e where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_e where match_id = 6), 0)'
                ') where team_id =1')
    cur.execute('update gre set gd =('
                'COALESCE((select score2 - score1 from matches_e where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_e where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_e where match_id = 5), 0)'
                ') where team_id =2')
    cur.execute('update gre set gd =('
                'COALESCE((select score1 - score2 from matches_e where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_e where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_e where match_id = 5), 0)'
                ') where team_id =3')
    cur.execute('update gre set gd =('
                'COALESCE((select score2 - score1 from matches_e where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_e where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_e where match_id = 6), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update gre set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_e where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_e where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_e where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_e where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update gre set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_e where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_e where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_e where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_e where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update gre set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_e where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_e where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_e where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_e where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update gre set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_e where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_e where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_e where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_e where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_e where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from gre order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grE order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grE order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grE order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_e():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_e')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group F-------------------------


def update_match_f(sm31t1, sm31t2, sm32t1, sm32t2, sm33t1, sm33t2, sm34t1, sm34t2, sm35t1, sm35t2, sm36t1, sm36t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 1', (sm31t1, sm31t2))
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 2', (sm32t1, sm32t2))
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 3', (sm33t1, sm33t2))
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 4', (sm34t1, sm34t2))
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 5', (sm35t1, sm35t2))
    cur.execute('update matches_f set score1 = ?, score2 = ? where match_id = 6', (sm36t1, sm36t2))
    conn.commit()
    conn.close()


def update_group_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grf set mp =(select count(match_id) from matches_f '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grf set mp =(select count(match_id) from matches_f '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grf set mp =(select count(match_id) from matches_f '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grf set mp =(select count(match_id) from matches_f '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grf set gd =('
                'COALESCE((select score1 - score2 from matches_f where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_f where match_id = 4), 0) + '
                'COALESCE((select score2 - score1 from matches_f where match_id = 6), 0)'
                ') where team_id =1')
    cur.execute('update grf set gd =('
                'COALESCE((select score2 - score1 from matches_f where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_f where match_id = 3), 0) + '
                'COALESCE((select score1 - score2 from matches_f where match_id = 5), 0)'
                ') where team_id =2')
    cur.execute('update grf set gd =('
                'COALESCE((select score1 - score2 from matches_f where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_f where match_id = 4), 0) + '
                'COALESCE((select score2 - score1 from matches_f where match_id = 5), 0)'
                ') where team_id =3')
    cur.execute('update grf set gd =('
                'COALESCE((select score2 - score1 from matches_f where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_f where match_id = 3), 0) + '
                'COALESCE((select score1 - score2 from matches_f where match_id = 6), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grf set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_f where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_f where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_f where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_f where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grf set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_f where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_f where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_f where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_f where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grf set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_f where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_f where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_f where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_f where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grf set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_f where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_f where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_f where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_f where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_f where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grf order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grF order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grF order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grF order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_f')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group G-------------------------

def update_match_g(sm37t1, sm37t2, sm38t1, sm38t2, sm39t1, sm39t2, sm40t1, sm40t2, sm41t1, sm41t2, sm42t1, sm42t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 1', (sm37t1, sm37t2))
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 2', (sm38t1, sm38t2))
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 3', (sm39t1, sm39t2))
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 4', (sm40t1, sm40t2))
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 5', (sm41t1, sm41t2))
    cur.execute('update matches_g set score1 = ?, score2 = ? where match_id = 6', (sm42t1, sm42t2))
    conn.commit()
    conn.close()


def update_group_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grg set mp =(select count(match_id) from matches_g '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grg set mp =(select count(match_id) from matches_g '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grg set mp =(select count(match_id) from matches_g '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grg set mp =(select count(match_id) from matches_g '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grg set gd =('
                'COALESCE((select score1 - score2 from matches_g where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_g where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_g where match_id = 5), 0)'
                ') where team_id =1')
    cur.execute('update grg set gd =('
                'COALESCE((select score2 - score1 from matches_g where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_g where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_g where match_id = 6), 0)'
                ') where team_id =2')
    cur.execute('update grg set gd =('
                'COALESCE((select score1 - score2 from matches_g where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_g where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_g where match_id = 6), 0)'
                ') where team_id =3')
    cur.execute('update grg set gd =('
                'COALESCE((select score2 - score1 from matches_g where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_g where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_g where match_id = 5), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grg set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_g where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_g where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_g where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_g where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grg set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_g where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_g where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_g where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_g where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grg set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_g where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_g where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_g where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_g where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grg set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_g where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_g where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_g where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_g where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_g where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grg order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grG order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grG order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grG order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_g():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_g')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# group H-------------------------


def update_match_h(sm43t1, sm43t2, sm44t1, sm44t2, sm45t1, sm45t2, sm46t1, sm46t2, sm47t1, sm47t2, sm48t1, sm48t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 1', (sm43t1, sm43t2))
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 2', (sm44t1, sm44t2))
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 3', (sm45t1, sm45t2))
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 4', (sm46t1, sm46t2))
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 5', (sm47t1, sm47t2))
    cur.execute('update matches_h set score1 = ?, score2 = ? where match_id = 6', (sm48t1, sm48t2))
    conn.commit()
    conn.close()


def update_group_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # mp
    cur.execute(
        'update grh set mp =(select count(match_id) from matches_h '
        'where (team_id =1 or team_id2 = 1) and  score1 != "") where team_id =1')
    cur.execute(
        'update grh set mp =(select count(match_id) from matches_h '
        'where (team_id =2 or team_id2 = 2) and  score1 != "") where team_id = 2')
    cur.execute(
        'update grh set mp =(select count(match_id) from matches_h '
        'where (team_id =3 or team_id2 = 3) and  score1 != "") where team_id = 3')
    cur.execute(
        'update grh set mp =(select count(match_id) from matches_h '
        'where (team_id =4 or team_id2 = 4) and  score1 != "") where team_id = 4')

    # gd
    cur.execute('update grh set gd =('
                'COALESCE((select score1 - score2 from matches_h where match_id = 1), 0) + '
                'COALESCE((select score1 - score2 from matches_h where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_h where match_id = 5), 0)'
                ') where team_id =1')
    cur.execute('update grh set gd =('
                'COALESCE((select score2 - score1 from matches_h where match_id = 1), 0) + '
                'COALESCE((select score2 - score1 from matches_h where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_h where match_id = 6), 0)'
                ') where team_id =2')
    cur.execute('update grh set gd =('
                'COALESCE((select score1 - score2 from matches_h where match_id = 2), 0) + '
                'COALESCE((select score2 - score1 from matches_h where match_id = 3), 0) + '
                'COALESCE((select score2 - score1 from matches_h where match_id = 6), 0)'
                ') where team_id =3')
    cur.execute('update grh set gd =('
                'COALESCE((select score2 - score1 from matches_h where match_id = 2), 0) + '
                'COALESCE((select score1 - score2 from matches_h where match_id = 4), 0) + '
                'COALESCE((select score1 - score2 from matches_h where match_id = 5), 0)'
                ') where team_id =4')

    # pts
    cur.execute('update grh set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_h where team_id=1), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_h where team_id2=1), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id=1 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id2=1 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_h where team_id=1), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_h where team_id2=1), 0)'
                ')where team_id = 1')
    cur.execute('update grh set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_h where team_id=2), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_h where team_id2=2), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id=2 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id2=2 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_h where team_id=2), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_h where team_id2=2), 0)'
                ')where team_id = 2')
    cur.execute('update grh set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_h where team_id=3), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_h where team_id2=3), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id=3 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id2=3 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_h where team_id=3), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_h where team_id2=3), 0)'
                ')where team_id = 3')
    cur.execute('update grh set pts =('
                'COALESCE(3*(select sum(score1 > score2) from matches_h where team_id=4), 0) +'
                'COALESCE(3*(select sum(score2 > score1) from matches_h where team_id2=4), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id=4 and score1 != ""), 0) + '
                'COALESCE(1*(select sum(score1 = score2) from matches_h where team_id2=4 and score1 != ""), 0) +'
                'COALESCE(0*(select sum(score1 < score2) from matches_h where team_id=4), 0) +'
                'COALESCE(0*(select sum(score2 < score1) from matches_h where team_id2=4), 0)'
                ')where team_id = 4')
    conn.commit()
    conn.close()


def show_teams_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from grh order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_mp_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT mp FROM grH order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_gd_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT gd FROM grH order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_pts_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT pts FROM grH order by pts desc, gd desc, team')
    rows = cur.fetchall()
    conn.close()
    return rows


def show_data_h():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_h')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    conn.close()
    return lst


# update final stages -------------------------------------------------------
def final_stages(gr):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT abbr FROM {} order by pts desc, gd desc, team '.format(gr))
    rows = cur.fetchall()
    return rows


def winners(gr):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('SELECT name FROM {} order by pts desc, gd desc, team '.format(gr))
    rows = cur.fetchall()
    return rows


def update_round16(gr1, gr2, match):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_r16 set '
                'team1_name=(select name from {} order by pts desc, gd desc limit 1),'
                'team1_abbr=(select abbr from {} order by pts desc, gd desc limit 1) '
                'where match_id = {}'.format(gr1, gr1, match))
    cur.execute('update matches_r16 set '
                'team2_name=(select name from {} order by pts desc, gd desc limit 1,1),'
                'team2_abbr=(select abbr from {} order by pts desc, gd desc limit 1,1) '
                'where match_id = {}'.format(gr2, gr2, match))
    conn.commit()
    conn.close()


def show_data_r16():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_r16')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    r5 = list(cur.fetchone())
    r6 = list(cur.fetchone())
    r7 = list(cur.fetchone())
    r8 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    lst.append(r5)
    lst.append(r6)
    lst.append(r7)
    lst.append(r8)
    conn.close()
    return lst


def update_qf(sm49t1, sm49t2, sm50t1, sm50t2, sm51t1, sm51t2, sm52t1, sm52t2, sm53t1, sm53t2, sm54t1, sm54t2, sm55t1,
              sm55t2, sm56t1, sm56t2, m1, m2, match):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # matches r16
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 49', (sm49t1, sm49t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 50', (sm50t1, sm50t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 51', (sm51t1, sm51t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 52', (sm52t1, sm52t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 53', (sm53t1, sm53t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 54', (sm54t1, sm54t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 55', (sm55t1, sm55t2))
    cur.execute('update matches_r16 set score1 = ?, score2 = ? where match_id = 56', (sm56t1, sm56t2))

    # teams qualified in qf
    cur.execute(
        'update matches_qf set team1_name = (select iif((select score1 from matches_r16 where match_id= {}), '  # m1
        '(select iif(score1>score2, team1_name, team2_name) from matches_r16 where match_id = {} ), null)),'  # m1
        '                       team2_name = (select iif((select score1 from matches_r16 where match_id= {}), '  # m2 
        '(select iif(score1>score2, team1_name, team2_name) from matches_r16 where match_id = {} ), null))'  # m2
        'where match_id = {}'.format(m1, m1, m2, m2, match))  # match
    cur.execute(
        'update matches_qf set team1_abbr = (select iif((select score1 from matches_r16 where match_id= {}), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_r16 where match_id = {} ), null)),'
        '                       team2_abbr = (select iif((select score1 from matches_r16 where match_id= {}), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_r16 where match_id = {} ), null))'
        'where match_id = {}'.format(m1, m1, m2, m2, match))
    conn.commit()
    conn.close()


def show_qf_abbr():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select team1_abbr, team2_abbr from matches_qf')
    lst = []
    row1 = cur.fetchone()
    lst.append(row1[0])
    lst.append(row1[1])
    row2 = cur.fetchone()
    lst.append(row2[0])
    lst.append(row2[1])
    row3 = cur.fetchone()
    lst.append(row3[0])
    lst.append(row3[1])
    row4 = cur.fetchone()
    lst.append(row4[0])
    lst.append(row4[1])
    conn.close()
    return lst

    # ----------------------------------------------------------------------------

    # ----------------------------------------------------------------------------


def show_data_qf():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_qf')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    r3 = list(cur.fetchone())
    r4 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    lst.append(r3)
    lst.append(r4)
    conn.close()
    return lst


def update_sf(sm57t1, sm57t2, sm58t1, sm58t2, sm59t1, sm59t2, sm60t1, sm60t2, m1, m2, match):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # matches qf
    cur.execute('update matches_qf set score1 = ?, score2 = ? where match_id = 57', (sm57t1, sm57t2))
    cur.execute('update matches_qf set score1 = ?, score2 = ? where match_id = 58', (sm58t1, sm58t2))
    cur.execute('update matches_qf set score1 = ?, score2 = ? where match_id = 59', (sm59t1, sm59t2))
    cur.execute('update matches_qf set score1 = ?, score2 = ? where match_id = 60', (sm60t1, sm60t2))

    # teams qualified in sf
    cur.execute(
        'update matches_sf set team1_name = (select iif((select score1 from matches_qf where match_id= {}), '
        '(select iif(score1>score2, team1_name, team2_name) from matches_qf where match_id = {} ), null)),'
        '                       team2_name = (select iif((select score1 from matches_qf where match_id= {}), '
        '(select iif(score1>score2, team1_name, team2_name) from matches_qf where match_id = {} ), null))'
        'where match_id = {}'.format(m1, m1, m2, m2, match))

    cur.execute(
        'update matches_sf set team1_abbr = (select iif((select score1 from matches_qf where match_id= {}), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_qf where match_id = {} ), null)),'
        '                       team2_abbr = (select iif((select score1 from matches_qf where match_id= {}), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_qf where match_id = {} ), null))'
        'where match_id = {}'.format(m1, m1, m2, m2, match))

    conn.commit()
    conn.close()


def show_data_sf():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_sf')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    conn.close()
    return lst


def show_sf_abbr():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select team1_abbr, team2_abbr from matches_sf')
    lst = []
    row1 = cur.fetchone()
    lst.append(row1[0])
    lst.append(row1[1])
    row2 = cur.fetchone()
    lst.append(row2[0])
    lst.append(row2[1])
    conn.close()
    return lst


def update_fin(sm61t1, sm61t2, sm62t1, sm62t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # matches sf
    cur.execute('update matches_sf set score1 = ?, score2 = ? where match_id = 61', (sm61t1, sm61t2))
    cur.execute('update matches_sf set score1 = ?, score2 = ? where match_id = 62', (sm62t1, sm62t2))

    # teams qualified in third place
    cur.execute(
        'update matches_fin set team1_name = (select iif((select score1 from matches_sf where match_id= 61), '
        '(select iif(score1<score2, team1_name, team2_name) from matches_sf where match_id = 61 ), null)),'
        '                       team2_name = (select iif((select score1 from matches_sf where match_id= 62), '
        '(select iif(score1<score2, team1_name, team2_name) from matches_sf where match_id = 62 ), null))'
        'where match_id = 63')

    cur.execute(
        'update matches_fin set team1_abbr = (select iif((select score1 from matches_sf where match_id= 61), '
        '(select iif(score1<score2, team1_abbr, team2_abbr) from matches_sf where match_id = 61 ), null)),'
        '                       team2_abbr = (select iif((select score1 from matches_sf where match_id= 62), '
        '(select iif(score1<score2, team1_abbr, team2_abbr) from matches_sf where match_id = 62 ), null))'
        'where match_id = 63')

    # teams qualified in fin
    cur.execute(
        'update matches_fin set team1_name = (select iif((select score1 from matches_sf where match_id= 61), '
        '(select iif(score1>score2, team1_name, team2_name) from matches_sf where match_id = 61 ), null)),'
        '                       team2_name = (select iif((select score1 from matches_sf where match_id= 62), '
        '(select iif(score1>score2, team1_name, team2_name) from matches_sf where match_id = 62 ), null))'
        'where match_id = 64')

    cur.execute(
        'update matches_fin set team1_abbr = (select iif((select score1 from matches_sf where match_id= 61), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_sf where match_id = 61 ), null)),'
        '                       team2_abbr = (select iif((select score1 from matches_sf where match_id= 62), '
        '(select iif(score1>score2, team1_abbr, team2_abbr) from matches_sf where match_id = 62 ), null))'
        'where match_id = 64')

    conn.commit()
    conn.close()


def show_data_fin():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst = []
    cur.execute('select score1, score2 from matches_fin')
    r1 = list(cur.fetchone())
    r2 = list(cur.fetchone())
    lst.append(r1)
    lst.append(r2)
    conn.close()
    return lst


def show_fin_abbr():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select team1_abbr, team2_abbr from matches_fin')
    lst = []
    row1 = cur.fetchone()
    lst.append(row1[0])
    lst.append(row1[1])
    row2 = cur.fetchone()
    lst.append(row2[0])
    lst.append(row2[1])
    conn.close()
    return lst


def decide_winners(sm63t1, sm63t2, sm64t1, sm64t2):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('update matches_fin set score1 = ?, score2 = ? where match_id = 63', (sm63t1, sm63t2))
    cur.execute('update matches_fin set score1 = ?, score2 = ? where match_id = 64', (sm64t1, sm64t2))
    conn.commit()
    conn.close()


def show_winners():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    lst_win = []
    cur.execute('select iif((select score1 from matches_fin where match_id = 64), '
                '(select iif(score1>score2, team1_name, team2_name) from matches_fin where match_id = 64), null)')
    first = cur.fetchone()
    lst_win.append(first[0])
    cur.execute('select iif((select score1 from matches_fin where match_id = 64), '
                '(select iif(score1<score2, team1_name, team2_name) from matches_fin where match_id = 64), null)')
    second = cur.fetchone()
    lst_win.append(second[0])
    cur.execute('select iif((select score1 from matches_fin where match_id = 63), '
                '(select iif(score1>score2, team1_name, team2_name) from matches_fin where match_id = 63), null)')
    third = cur.fetchone()
    lst_win.append(third[0])
    conn.close()
    return lst_win


# info from matches ------------------------------------------

def get_info(group, match):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select info from {} where match_id={}'.format(group, match))
    row = cur.fetchone()
    conn.close()
    return row


def update_info_r16(txt, id):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    # cur.execute('update matches_r16 set info = "extra time" where match_id=49')
    cur.execute('update matches_r16 set info = ? where match_id=?', (txt, id))
    conn.commit()
    conn.close()


def update_info_qf(txt, id):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    # cur.execute('update matches_r16 set info = "extra time" where match_id=49')
    cur.execute('update matches_qf set info = ? where match_id=?', (txt, id))
    conn.commit()
    conn.close()


def update_info_sf(txt, id):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    # cur.execute('update matches_r16 set info = "extra time" where match_id=49')
    cur.execute('update matches_sf set info = ? where match_id=?', (txt, id))
    conn.commit()
    conn.close()


def update_info_fin(txt, id):
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    # cur.execute('update matches_r16 set info = "extra time" where match_id=49')
    cur.execute('update matches_fin set info = ? where match_id=?', (txt, id))
    conn.commit()
    conn.close()


# ------------------------------

def reset_tables():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()

    # delete data from matches_final_stages
    cur.execute('delete from  matches_r16')
    cur.execute('delete from  matches_qf')
    cur.execute('delete from  matches_sf')
    cur.execute('delete from  matches_fin')

    # delete data from matches
    cur.execute('delete from  matches_h')
    cur.execute('delete from  matches_g')
    cur.execute('delete from  matches_f')
    cur.execute('delete from  matches_e')
    cur.execute('delete from  matches_d')
    cur.execute('delete from  matches_c')
    cur.execute('delete from  matches_b')
    cur.execute('delete from  matches_a')

    # delete data from groups
    cur.execute('delete from  gra')
    cur.execute('delete from  grb')
    cur.execute('delete from  grc')
    cur.execute('delete from  grd')
    cur.execute('delete from  gre')
    cur.execute('delete from  grf')
    cur.execute('delete from  grg')
    cur.execute('delete from  grh')

    conn.commit()

    add_group()
    add_matches()
    add_matches_finals()

    conn.close()


# ------------------------------

def f():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from gra')

    rows = cur.fetchall()
    conn.close()
    return rows


def f2():
    conn = sqlite3.connect('wc22.db')
    cur = conn.cursor()
    cur.execute('select * from matches_a')

    rows = cur.fetchall()
    conn.close()
    return rows

    # r1 = list(cur.fetchone())
    # lst.append(r1)
    # conn.close()
    # return lst


connect_db()
