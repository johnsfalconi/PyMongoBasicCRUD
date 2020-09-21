from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'video'
app.config["MONGO_URI"] = 'mongodb://jfalconi:drummer3@cluster0-shard-00-00.bjwrh.mongodb.net:27017,cluster0-shard-00-01.bjwrh.mongodb.net:27017,cluster0-shard-00-02.bjwrh.mongodb.net:27017/video?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)


#client = MongoClient('mongodb://jfalconi:drummer3@cluster0-shard-00-00.bjwrh.mongodb.net:27017,cluster0-shard-00-01.bjwrh.mongodb.net:27017,cluster0-shard-00-02.bjwrh.mongodb.net:27017/video?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')


@app.route("/")
def home_page():
    my_movie = mongo.db.myMovies.find({"year": 2013})
    return render_template("index2.html", my_movie = my_movie)