from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MLOpsDB"
mongo = PyMongo(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Adding to MongoDB
        data = {"Name": name, "Email": email}
        mongo.db.inventory.insert_one(data)
        
        return 'Data stored in MongoDB!'
    else:
        return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True,host=0.0.0.0)