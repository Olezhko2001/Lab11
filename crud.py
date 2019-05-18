from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from models.MusicType import MusicType

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class PopMusic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    music_type = db.Column(db.Enum(MusicType))
    release_year = db.Column(db.Integer)
    performer = db.Column(db.String)
    author = db.Column(db.String)

    def __init__(self,
                 name = None,
                 price = 0,
                 music_type = None,
                 release_year = 0,
                 performer = None,
                 author = None):
        self.name = name
        self.price = price
        self.music_type = music_type
        self.release_year = release_year
        self.performer = performer
        self.author = author


class PopMusicSchema(ma.Schema):
    class Meta:
        fields = ('name', 'price', 'music_type', 'release_year', 'performer', 'author')


pop_music_schema = PopMusicSchema()
pop_musics_schema = PopMusicSchema(many=True)


@app.route("/popmusic", methods=["POST"])
def add_pop_music():
    name = request.json['name']
    price = request.json['price']
    music_type = request.json['music_type']
    release_year = request.json['release_year']
    performer = request.json['performer']
    author = request.json['author']
    
    new_pop_music = PopMusic(name, price, music_type, release_year, performer, author)

    db.session.add(new_pop_music)
    db.session.commit()

    return pop_music_schema.jsonify(new_pop_music)


@app.route("/popmusic", methods=["GET"])
def get_pop_music():
    all_pop_musics = PopMusic.query.all()
    result = pop_musics_schema.dump(all_pop_musics)
    return jsonify(result.data)


@app.route("/popmusic/<id>", methods=["GET"])
def pop_music_detail(id):
    pop_music = PopMusic.query.get(id)
    return pop_music_schema.jsonify(pop_music)


@app.route("/popmusic/<id>", methods=["PUT"])
def pop_music_update(id):
    pop_music = PopMusic.query.get(id)

    pop_music.name = request.json['name']
    pop_music.price = request.json['price']
    pop_music.music_type = request.json['music_type']
    pop_music.release_year = request.json['release_year']
    pop_music.performer = request.json['performer']
    pop_music.author = request.json['author']

    db.session.commit()
    return pop_music_schema.jsonify(pop_music)


@app.route("/popmusic/<id>", methods=["DELETE"])
def pop_music_delete(id):
    pop_music = PopMusic.query.get(id)
    db.session.delete(pop_music)
    db.session.commit()

    return pop_music_schema.jsonify(pop_music)


if __name__ == '__main__':
    app.run(debug=True)
