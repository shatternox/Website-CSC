from flask import render_template, request, Blueprint, current_app, session
from website.models import User, Article
from website import db
import os

core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
def index():
    # # Core
    # kaifa = User(email="kaifaraihanafatah@gmail.com", name="Kaifa Raihana Fatah", username="0xkaifa",
    #              role=2, division="Chairman", password="2201838714", profile_image="kaifa.jpg")
    # nico = User(email="nico.christian001@binus.ac.id", name="Nico Christian", username="0xnico",
    #             role=2, division="Vice Chairman", password="2201737122", profile_image="nico.jpg")
    # stefan = User(email="reusp3ct@gmail.com", name="Stefan Adisurya", username="0xstefan",
    #               role=2, division="Secretary", password="2201753706", profile_image="stefan.jpg")
    # alex = User(email="alexander.christianb@gmail.com", name="Alexander Christian", username="0xalex",
    #             role=2, division="Treasurer", password="2201727222", profile_image="alex.jpg")
    # bryan = User(email="bryanmitchell2000@gmail.com", name="Bryan Mitchell Lee", username="0xbryan",
    #              role=1, division="Human", password="2201749961", profile_image="bryan.jpg")
    # ardie = User(email="ardie.putra@binus.ac.id", name="Ardie Wijaya Eka Putra", username="0xardie",
    #              role=1, division="Event", password="2201747615", profile_image="ardie.jpg")
    # jeremy = User(email="jychrisyanto5@gmail.com", name="Jeremy Yonathan Chrisyanto", username="0xjeremy",
    #               role=1, division="Education", password="2201743642", profile_image="jeremy.jpg")

    # db.session.add_all([kaifa, nico, stefan, alex, bryan, ardie, jeremy])

    # # Human
    # tonto = User(email="Tonto.c510@gmail.com", name="Tonto Claudinus", username="0xtonto",
    #              role=0, division="Human", password="2201730740", profile_image="default.png")
    # dragon = User(email="michael.dragon477@gmail.com", name="Michael Dragon Muliawidjaja",
    #               username="0xdragon", role=0, division="Human", password="2201738522", profile_image="default.png")
    # rei = User(email="reinaldy.sukamto@gmail.com", name="Reinaldy Sukamto", username="0xrei",
    #            role=0, division="Human", password="2301853136", profile_image="default.png")
    # timo = User(email="ioo16701@gmail.com", name="Timotius Eldwin Valentino", username="0xtimo",
    #             role=0, division="Human", password="2301856301", profile_image="default.png")

    # leon = User(email="leonchandra95@gmail.com", name="Leon Fernandy Chandra", username="0xleon",
    #             role=0, division="Human", password="2301850310", profile_image="default.png")
    # selada = User(email="lordblaze26@gmail.com", name="Daniel Russell Alexander", username="0xselada",
    #               role=0, division="Human", password="2301866504", profile_image="default.png")
    # naufaly = User(email="Naufal.zi2620@gmail.com", name="Naufaly Zuhdi Indriandi", username="0xnaufal",
    #                role=0, division="Human", password="2301944481", profile_image="default.png")
    # udin = User(email="awaludinar741@gmail.com", name="Awaludin", username="0xudin",
    #             role=0, division="Human", password="2301933162", profile_image="default.png")

    # db.session.add_all([tonto, dragon, rei, timo,
    #                     leon, selada, naufaly, udin])

    # # Research
    # danny = User(email="ardian775danny@gmail.com", name="Ardian Danny", username="0xdanny",
    #              role=3, division="Research", password="2301847303", profile_image="default.png")
    # excel = User(email="excelantonio27@gmail.com", name="Excel Antonio", username="0xexcel",
    #              role=3, division="Research", password="2301872766", profile_image="default.png")
    # william = User(email="hastantawilliam@gmail.com", name="William Hastanta", username="0xwh",
    #                role=3, division="Research", password="2301854454", profile_image="default.png")
    # rifqi = User(email="rifqiaufa43human1@gmail.com", name="Rifqi Aufa Rabbani Putra", username="0xrifqi",
    #              role=0, division="Research", password="2301944595", profile_image="default.png")
    # komang = User(email="kenpai.77@gmail.com", name="I Komang Sughosa Anantawijaya", username="0xkomang",
    #               role=0, division="Research", password="2301897983", profile_image="default.png")
    # felix = User(email="felix.deegawijaya!@gmail.com", name="Felix Alexander", username="0xfelix",
    #              role=0, division="Research", password="2301859253", profile_image="default.png")
    # valentino = User(email="valentinonooril@gmail.com", name="Valentino Nooril", username="0xvalentino",
    #                  role=0, division="Research", password="2301894155", profile_image="default.png")
    # ficky = User(email="achmadfickyabdullah@gmail.com", name="Achmad Ficky Abdullah", username="0xficky",
    #              role=0, division="Research", password="2301881682", profile_image="default.png")
    # sugi = User(email="sugiarta.wijaya05@gmail.com", name="Sugiarta Wijaya", username="0xsugiarta",
    #             role=0, division="Research", password="2201745074", profile_image="default.png")
    # ricky = User(email="moving.ricky@gmail.com", name="Ricky Aryanto", username="0xricky",
    #              role=0, division="Research", password="2301875515", profile_image="default.png")

    # db.session.add_all([sugi, ficky, excel, william, rifqi,
    #                     danny, komang, felix, valentino, ricky])

    # # Education
    # kelvin = User(email="kelvinnatalino07@gmail.com", name="Kelvin Natalino Halim", username="0xkelvin",
    #               role=0, division="Education", password="2201776211", profile_image="default.png")
    # osvaldo = User(email="osvaldo.riady@yahoo.co.id", name="Osvaldo Richie Riady", username="0xosvaldo",
    #                role=0, division="Education", password="2201823290", profile_image="default.png")
    # farel = User(email="farelharden13@gmail.com", name="Mochammad Farel Herqutanto", username="0xmochammad",
    #              role=0, division="Education", password="2301907416", profile_image="default.png")
    # daniel = User(email="danielstefanus928@gmail.com", name="Daniel Stefanus Christiawan",
    #               username="0xdaniel", role=0, division="Education", password="2301881575", profile_image="default.png")
    # kristian = User(email="kristiananwar00xn@gmail.com", name="Kristian Anwar", username="0xkristian",
    #                 role=0, division="Education", password="2301853786", profile_image="default.png")
    # fabian = User(email="devalpha01@gmail.com", name="Fabian Ferristo Tirtabudi", username="0xfabian",
    #               role=0, division="Education", password="2301864581", profile_image="default.png")
    # hardwin = User(email="dromax98@gmail.com", name="Hardwin", username="0xhardwin",
    #                role=0, division="Education", password="2301914390", profile_image="default.png")
    # umi = User(email="umyal30@gmail.com", name="Umi al mu'minati", username="0xumi",
    #            role=0, division="Education", password="2201750471", profile_image="default.png")
    # abraham = User(email="abrahammangisiparuntu@gmail.com", name="Abraham Tigor Mangisi Paruntu",
    #                username="0xabraham", role=0, division="Education", password="2301948460", profile_image="default.png")

    # db.session.add_all([kelvin, osvaldo, farel, daniel,
    #                     kristian, fabian, hardwin, umi, abraham])

    # # Event
    # carolus = User(email="carolus.raditya@gmail.com", name="Carolus Raditya", username="0xcarolus",
    #                role=0, division="Event", password="2201742255", profile_image="default.png")
    # ryan = User(email="ryanricardo.liauw@gmail.com", name="Ryan Ricardo", username="0xryan",
    #             role=0, division="Event", password="2201748403", profile_image="default.png")
    # fawwaz = User(email="fawwazzulfa@gmail.com", name="Fawwaz Zulfaa", username="0xfawwaz",
    #               role=0, division="Event", password="2301955844", profile_image="default.png")
    # leonardo = User(email="lepedhi10@yahoo.com", name="Leonardus Pedro Hidayat", username="0xleonardus",
    #                 role=0, division="Event", password="2301920714", profile_image="default.png")
    # jessica = User(email="geofanie48@gmail.com", name="Jessica Geofanie Ganadhi", username="0xjessica",
    #                role=0, division="Event", password="2301916023", profile_image="default.png")
    # zia = User(email="zizikasyfi@gmail.com", name="Zia Kasyfi Nugroho", username="0xzia",
    #            role=0, division="Event", password="2301881581", profile_image="default.png")
    # satria = User(email="aryanuruzzaman75@gmail.com", name="Muhammad Satria Nuruzzaman",
    #               username="0xsatria", role=0, division="Event", password="2301944821", profile_image="default.png")
    # davin = User(email="natdavin@gmail.com", name="Nathaniel Davin", username="0xdavin",
    #              role=0, division="Event", password="2301853773", profile_image="default.png")
    # db.session.add_all([carolus, ryan, fawwaz, leonardo,
    #                     jessica, zia, udin, satria, davin])

    # db.session.commit()

    user = User.query.all()

    return render_template('index_new.html', user=user)


@core.route("/ourpeople")
def ourpeople():
    user = User.query.all()
    return render_template('ourpeople.html', user=user, title="About Us")


@core.route('/soon')
def coming_soon():
    return render_template('coming.html')


@core.route('/divisi')
def divisi():
    return render_template('divisi.html')
