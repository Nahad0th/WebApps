import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

#MODELS

class Activity(db.Model):
  __tablename__ = 'activities'
  id = db.Column(db.Integer, primary_key=True)
  phySed = db.Column(db.String(10))
  excRel = db.Column(db.String(10))
  indOut = db.Column(db.String(10))
  hobTas = db.Column(db.String(10))
  simCom = db.Column(db.String(10))
  name = db.Column(db.String(64), unique = True)
  desc = db.Column(db.String(128))
  img = db.Column(db.String(128))
  def __repr__(self):
    return '<Activity %r>' % self.name

@app.route('/', methods=['POST','GET'])
def index():
  db.drop_all()
  db.create_all()
  
  #ACTIVITIES
  task1 = Activity(id = 1, phySed = 'physical', excRel = 'relaxing', indOut = 'indoors', hobTas = 'task', simCom = 'simple', name = 'Clean', desc = 'Take some time to clean your enviorment, vacum, sweep, dust, etc and sanatize all surfaces around you.', img = 'https://cleanmyspace.com/wp-content/uploads/2017/08/professional-cleaning-tips.jpg')
  task2 = Activity(id= 2, phySed='pysical', excRel='either', indOut='either', hobTas='either', simCom='simple', name='Work Out', desc='Its time to stay in shape! Work out for 30 minutes. Focus more on your form than speed.', img='https://static.vecteezy.com/system/resources/previews/000/162/135/original/push-up-pose-vector.jpg')
  task3 = Activity(id= 3, phySed='physical', excRel='relaxing', indOut='outdoors', hobTas='either', simCom='simple', name='Go On A Walk', desc='Just enjoy your enviorment and go on a walk. Remember to mind those around you and stay away from strangers.', img='https://mindfulnessatwork.ie/wp-content/uploads/2013/05/walk-mindfully.jpg')
  task4 = Activity(id= 4, phySed='mental', excRel='either', indOut='indoors', hobTas='hobby', simCom='either', name='Play A Game', desc='Find any game you can play, on your phone or computer, even a board game will do. Take some time to relax and have some fun.', img='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/board-game-royalty-free-image-1584714025.jpg?crop=1.00xw:0.756xh;0,0.0856xh&resize=1200:*')
  task5 = Activity(id= 5, phySed='physical', excRel='relaxing', indOut='outdoors', hobTas='task', simCom='simple', name='Yard Work', desc='Summer is comming and its time to make sure your yard is ready! If you dont have a yard, maybe spruce up your place with some plants.', img='https://cdn2.cityofhanahan.com/wp-content/uploads/2018/03/22085728/yard-work.jpg')
  task6 = Activity(id= 6, phySed='mental', excRel='either', indOut='indoors', hobTas='hobby', simCom='simple', name='Call A Friend', desc=' Take time to call someone, check up on how they have been and just catch up. Its important to keep in touch with others.', img='https://www.techlicious.com/images/phones/calling-on-smartphone-700px.jpg')
  task7 = Activity(id= 7, phySed='mental', excRel='relaxing', indOut='indoors', hobTas='hobby', simCom='simple', name='Watch A Youtube Video', desc='Find a youtube video you like and watch it. No one will judge you if you look up cute cats, everyone does it.', img='https://lh3.googleusercontent.com/lMoItBgdPPVDJsNOVtP26EKHePkwBg-PkuY9NOrc-fumRtTFP4XhpUNk_22syN4Datc')
  task8 = Activity(id= 8, phySed='mental', excRel='exciting', indOut='either', hobTas='hobby', simCom='complex', name='Learn Something New', desc='Find something new you can learn, maybe a programing language, or a cooking recipie. The limits are endless.', img='https://landscapelightingguru.com/wp-content/uploads/2017/01/lightbulb1.jpg')
  task9 = Activity(id= 9, phySed='physical', excRel='exciting', indOut='indoors', hobTas='hobby', simCom='complex', name='Chopped', desc='Its time to work on your cooking skills! Break out that cutting board and make some comfort food. Maybe make something new or a favorite dish.', img='https://images.yswcdn.com/-6709878151531560371-ql-85/800/600/ay/chefknivestogo/konosuke-hinoki-cutting-board-16-5-x-9-5-16.png')
  task10 = Activity(id= 10, phySed='either', excRel='relaxing', indOut='either', hobTas='hobby', simCom='simple', name='You Time', desc='With the world as it is, it\'s time for you to relax a little. Grab any kind of drink, kick back and relax. Read a book, or watch tv. This is your time.', img='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkpf_YJK-n8JumKoyeAaWmdACGjzQ4vujhyBFjIp3LyOtdAqgk&usqp=CAU')
  task11 = Activity(id= 11, phySed='physical', excRel='relaxing', indOut='either', hobTas='hobby', simCom='simple', name='Pet Love', desc='Show your pets how much they are loved. Play with them or just spend time with them. If you dont have a pet, go on to another task.', img='https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&poi=face&w=1864&h=976&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F37%2F2020%2F01%2Fcat-playing-with-toy.jpg')

  db.session.add_all([task1,task2,task3,task4,task5,task6,task7,task8,task9,task10,task11])
  db.session.commit()
  return render_template('index.html')

@app.route('/projMotiv')
def projMotiv():
  return render_template('projMotiv.html')

@app.route('/teamIntro')
def teamIntro():
  return render_template('teamIntro.html')

@app.route('/api/get_productive', methods=['GET'])
def get_productive():
  return util.rand_act(Activity.query.filter(Activity.hobTas != 'hobby'))

@app.route('/api/get_rand', methods=['GET'])
def get_rand():
  return util.rand_act(Activity.query.all())

@app.route('/api/get_fun', methods=['GET'])
def get_fun():
  return util.rand_act(Activity.query.filter(Activity.hobTas != 'task'))

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404_error.html'), 404

@app.errorhandler(500)
def server_error(e):
  print(e)
  return render_template('500_error.html'), 500

if __name__ == '__main__':
  app.debug = True
  ip = '127.0.0.1'
  app.run(host=ip)