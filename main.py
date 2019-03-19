# datebase

from flask import *

from sqlalchemy import create_engine, Column, String, Integer, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import os
from makedice import makedice
from taisai import judge_game

app = Flask(__name__)
engine = create_engine('sqlite:///app.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    money = Column(Integer)

    def __repr__(self):
        return "User<{}, {}>".format(self.name, self.money)

class BetTable(Base):
    __tablename__ = 'bettable'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    position = Column(String)
    value = Column(Integer)
    bet = Column(Integer, server_default="0")

    def __repr__(self):
        return "BetTable<{}, {}, {}>".format(self.name, self.position, self.bet)

class Dice(Base):
    __tablename__="dicetable"
    id = Column(Integer, primary_key = True)
    one = Column(Integer)
    two = Column(Integer)
    three = Column(Integer)

Base.metadata.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = scoped_session(SessionMaker)

def d(num):
    if num == "":
        return 0
    return num

# routing

@app.route("/", methods=["GET","POST"])
def main_page():
    if os.path.isfile("./app.db"):
        session.query(User).delete()
        session.query(BetTable).delete()
        session.query(Dice).delete()
        session.commit()

    if request.method == "POST":
        user1 = User(name = request.form["name1"], money = 0)
        user2 = User(name = request.form["name2"], money = 0)
        user3 = User(name = request.form["name3"], money = 0)
        user4 = User(name = request.form["name4"], money = 0)
        user5 = User(name = request.form["name5"], money = 0)

        session.add(user1)
        session.add(user2)
        session.add(user3)
        session.add(user4)
        session.add(user5)

        session.commit()

        dealer = session.query(User).filter(User.id == 1).first()
        others = session.query(User).filter(User.id != 1).all()
        return render_template("bet.html", dealer=dealer.name, others=others, id=1)

    else:
        return render_template("top.html")

@app.route("/bet/<int:id>", methods=["GET", "POST"])
def bet_page(id):

    if request.method == "POST":
        dealer = session.query(User).filter(User.id == id).first()
        others = session.query(User).filter(User.id != id).all()
        id_max = len(others)+1
        bets = [d(request.form.getlist("big")),
                d(request.form.getlist("small")),
                '''
                d(request.form.getlist("sum_4")),
                d(request.form.getlist("sum_5")),
                d(request.form.getlist("sum_6")),
                d(request.form.getlist("sum_7")),
                d(request.form.getlist("sum_8")),
                d(request.form.getlist("sum_9")),
                d(request.form.getlist("sum_10")),
                d(request.form.getlist("sum_11")),
                d(request.form.getlist("sum_12")),
                d(request.form.getlist("sum_13")),
                d(request.form.getlist("sum_14")),
                d(request.form.getlist("sum_15")),
                d(request.form.getlist("sum_16")),
                d(request.form.getlist("sum_17")),
                d(request.form.getlist("combi_12")),
                d(request.form.getlist("combi_13")),
                d(request.form.getlist("combi_14")),
                d(request.form.getlist("combi_15")),
                d(request.form.getlist("combi_16")),
                d(request.form.getlist("combi_23")),
                d(request.form.getlist("combi_24")),
                d(request.form.getlist("combi_25")),
                d(request.form.getlist("combi_26")),
                d(request.form.getlist("combi_34")),
                d(request.form.getlist("combi_35")),
                d(request.form.getlist("combi_36")),
                d(request.form.getlist("combi_45")),
                d(request.form.getlist("combi_46")),
                d(request.form.getlist("combi_56")),
                d(request.form.getlist("in_1")),
                d(request.form.getlist("in_2")),
                d(request.form.getlist("in_3")),
                d(request.form.getlist("in_4")),
                d(request.form.getlist("in_5")),
                d(request.form.getlist("in_6")),
                d(request.form.getlist("double_1")),
                d(request.form.getlist("double_2")),
                d(request.form.getlist("double_3")),
                d(request.form.getlist("double_4")),
                d(request.form.getlist("double_5")),
                d(request.form.getlist("double_6")),
                d(request.form.getlist("anytriple")),
                d(request.form.getlist("triple_1")),
                d(request.form.getlist("triple_2")),
                d(request.form.getlist("triple_3")),
                d(request.form.getlist("triple_4")),
                d(request.form.getlist("triple_5")),
                d(request.form.getlist("triple_6")),
                '''
                ]
        i = 0
        for another in others:
            name = another.name

            big = BetTable(name=name, position="big", value=0, bet=bets[0][i])
            small = BetTable(name=name, position="small", value=0, bet=bets[1][i])
            '''
            sum_4 = BetTable(name=name, position="sum", value=4, bet=bets[2][i])
            sum_5 = BetTable(name=name, position="sum", value=5, bet=bets[3][i])
            sum_6 = BetTable(name=name, position="sum", value=6, bet=bets[4][i])
            sum_7 = BetTable(name=name, position="sum", value=7, bet=bets[5][i])
            sum_8 = BetTable(name=name, position="sum", value=8, bet=bets[6][i])
            sum_9 = BetTable(name=name, position="sum", value=9, bet=bets[7][i])
            sum_10 = BetTable(name=name, position="sum", value=10, bet=bets[8][i])
            sum_11 = BetTable(name=name, position="sum", value=11, bet=bets[9][i])
            sum_12 = BetTable(name=name, position="sum", value=12, bet=bets[10][i])
            sum_13 = BetTable(name=name, position="sum", value=13, bet=bets[11][i])
            sum_14 = BetTable(name=name, position="sum", value=14, bet=bets[12][i])
            sum_15 = BetTable(name=name, position="sum", value=15, bet=bets[13][i])
            sum_16 = BetTable(name=name, position="sum", value=16, bet=bets[14][i])
            sum_17 = BetTable(name=name, position="sum", value=17, bet=bets[15][i])
            combi_12 = BetTable(name=name, position="combi", value=12, bet=bets[16][i])
            combi_13 = BetTable(name=name, position="combi", value=13, bet=bets[17][i])
            combi_14 = BetTable(name=name, position="combi", value=14, bet=bets[18][i])
            combi_15 = BetTable(name=name, position="combi", value=15, bet=bets[19][i])
            combi_16 = BetTable(name=name, position="combi", value=16, bet=bets[20][i])
            combi_23 = BetTable(name=name, position="combi", value=23, bet=bets[21][i])
            combi_24 = BetTable(name=name, position="combi", value=24, bet=bets[22][i])
            combi_25 = BetTable(name=name, position="combi", value=25, bet=bets[23][i])
            combi_26 = BetTable(name=name, position="combi", value=26, bet=bets[24][i])
            combi_34 = BetTable(name=name, position="combi", value=34, bet=bets[25][i])
            combi_35 = BetTable(name=name, position="combi", value=35, bet=bets[26][i])
            combi_36 = BetTable(name=name, position="combi", value=36, bet=bets[27][i])
            combi_45 = BetTable(name=name, position="combi", value=45, bet=bets[28][i])
            combi_46 = BetTable(name=name, position="combi", value=46, bet=bets[29][i])
            combi_56 = BetTable(name=name, position="combi", value=56, bet=bets[30][i])
            in_1 = BetTable(name=name, position="in", value=1, bet=bets[31][i])
            in_2 = BetTable(name=name, position="in", value=2, bet=bets[32][i])
            in_3 = BetTable(name=name, position="in", value=3, bet=bets[33][i])
            in_4 = BetTable(name=name, position="in", value=4, bet=bets[34][i])
            in_5 = BetTable(name=name, position="in", value=5, bet=bets[35][i])
            in_6 = BetTable(name=name, position="in", value=6, bet=bets[36][i])
            double_1 = BetTable(name=name, position="double", value=1, bet=bets[37][i])
            double_2 = BetTable(name=name, position="double", value=2, bet=bets[38][i])
            double_3 = BetTable(name=name, position="double", value=3, bet=bets[39][i])
            double_4 = BetTable(name=name, position="double", value=4, bet=bets[40][i])
            double_5 = BetTable(name=name, position="double", value=5, bet=bets[41][i])
            double_6 = BetTable(name=name, position="double", value=6, bet=bets[42][i])
            anytriple = BetTable(name=name, position="anytriple", value=0, bet=bets[43][i])
            triple_1 = BetTable(name=name, position="triple", value=1, bet=bets[44][i])
            triple_2 = BetTable(name=name, position="triple", value=2, bet=bets[45][i])
            triple_3 = BetTable(name=name, position="triple", value=3, bet=bets[46][i])
            triple_4 = BetTable(name=name, position="triple", value=4, bet=bets[47][i])
            triple_5 = BetTable(name=name, position="triple", value=5, bet=bets[48][i])
            triple_6 = BetTable(name=name, position="triple", value=6, bet=bets[49][i])
            '''

            session.add(big)
            session.add(small)
            '''
            session.add(sum_4)
            session.add(sum_5)
            session.add(sum_6)
            session.add(sum_7)
            session.add(sum_8)
            session.add(sum_9)
            session.add(sum_10)
            session.add(sum_11)
            session.add(sum_12)
            session.add(sum_13)
            session.add(sum_14)
            session.add(sum_15)
            session.add(sum_16)
            session.add(sum_17)
            session.add(combi_12)
            session.add(combi_13)
            session.add(combi_14)
            session.add(combi_15)
            session.add(combi_16)
            session.add(combi_23)
            session.add(combi_24)
            session.add(combi_25)
            session.add(combi_26)
            session.add(combi_34)
            session.add(combi_35)
            session.add(combi_36)
            session.add(combi_45)
            session.add(combi_46)
            session.add(combi_56)
            session.add(in_1)
            session.add(in_2)
            session.add(in_3)
            session.add(in_4)
            session.add(in_5)
            session.add(in_6)
            session.add(double_1)
            session.add(double_2)
            session.add(double_3)
            session.add(double_4)
            session.add(double_5)
            session.add(double_6)
            session.add(anytriple)
            session.add(triple_1)
            session.add(triple_2)
            session.add(triple_3)
            session.add(triple_4)
            session.add(triple_5)
            session.add(triple_6)
            '''

            session.commit()

        dice = makedice()
        sai = Dice(one=dice[0], two=dice[1], three=dice[2])
        session.add(sai)
        session.commit()
        return render_template("dice.html", dice=dice)


'''
        dealer = session.query(User).filter(User.id == id+1).first()
        others = session.query(User).filter(User.id != id+1).all()
        return render_template("bet.html", dealer=dealer.name, others=others, id=id+1)

    dealer = session.query(User).filter(User.id == 2).first()
    others = session.query(User).filter(User.id != 2).all()
    return render_template("bet.html", dealer=dealer.name, others=others, id=2)
'''

@app.route("/result/<int:id>", methods=["GET","POST"])
def result_page(id):
    result = []
    dealer = session.query(User).filter(User.id == id).first()
    others = session.query(User).filter(User.id != id).all()
    dice = session.query(Dice).first()
    sai = [dice.one, dice.two, dice.three]
    totalwin = 0
    for other in others:
        pasonalwin = 0
        bets = session.query(BetTable).filter(BetTable.name == other.name).all()
        for bet in bets:
            your_ex = [bet.position, bet.value, bet.bet]
            win = judge_game(sai, your_ex)
            parsonalwin += win
            result.append(win)
        totalwin += parsonalwin
        other.money += parsonalwin
    dealer.money -= totalwin
    session.commit()
    return render_template("result.html", users=users, result=result)

@app.route("/again", methods=["GET", "POST"])
def again():
    session.query(BetTable).delete()
    session.query(Dice).delete()
    session.commit()
    dealer = session.query(User).filter(User.id == 1).first()
    others = session.query(User).filter(User.id != 1).all()
    return render_template("bet.html", dealer=dealer.name, others=others, id=1)

@app.route("/end", methods=["GET", "POST"])
def end():
    session.query(User).delete()
    session.query(BetTable).delete()
    session.query(Dice).delete()
    session.commit()
    return render_template("top.html")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
