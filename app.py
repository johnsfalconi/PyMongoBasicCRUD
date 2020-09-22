# since I'm a forgetful freddy, here's the process to push to git and heroku
    # 1. $ pip freeze > requirements.txt
    # 2. $ git add .
    # 3. $ git commit -m "<update summary here>"
    # 4. $ git remote -v
    # 5. $ git push heroku master


from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_DBNAME'] = # DB Name
app.config["MONGO_URI"] = # MongoDB connection URI
mongo = PyMongo(app)

def __repr__(self):
    return '<Task %r' % self.id

#add
@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            mongo.db.myMovies.insert_one({'title':str(request.form['title']), 'year':int(request.form['year']), 'type':str(request.form['type']) })
            return redirect('/')
        except:
            return 'There was an issue adding'
    else:
        my_movie = list(mongo.db.myMovies.find())
        return render_template("index.html", movies = my_movie)

#delete
@app.route('/delete/<id>')
def delete(id):
    try:
        mongo.db.myMovies.delete_one({"_id":ObjectId(id)})
        return redirect('/')
    except:
        return 'there was a problem deleting'

# update
@app.route('/update/<id>', methods = ['GET', 'POST'])
def update(id):
    my_movie = mongo.db.myMovies.find_one_or_404({'_id':ObjectId(id)})

    if request.method == 'POST':
        mongo.db.myMovies.update_one({"_id":ObjectId(id)},{"$set":{'title':str(request.form['title']), 'year':int(request.form['year']), 'type':str(request.form['type']) }})
        try:
            return redirect('/')
        except:
            return 'there was an issue updating'
    else:
        return render_template('update.html', movies = my_movie)

if __name__ == "__main__":
    app.run(debug=True)
