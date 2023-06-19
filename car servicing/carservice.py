from flask import *
import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "car"
    )
cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/appointment")
def appointment():
    cursor.execute("select * from users")
    data = cursor.fetchall()
    return render_template("appointment.html",data=data)

@app.route("/appointment",methods=['POST'])
def create():
    
    name = request.form.get('fname')
    last = request.form.get('lname')
    contact = request.form.get('contact')
    email = request.form.get('email')
    car_num = request.form.get('carnum')
    dist = request.form.get('km')
    car_name = request.form.get('carname')
    atime = request.form.get('atime')
    dtime = request.form.get('dtime')
    total = request.form.get('total')
    creq = "insert into users(First_Name,Last_Name,Contact_no,Email,Car_number,Km_Run,Car_name,Arrived_time,Delivery_time,Total_amount) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,last,contact,email,car_num,dist,car_name,atime,dtime,total)
    try:
        cursor.execute(creq)
        db.commit()
        return redirect(url_for('appointment'))
    except:
        db.rollback()
        return "Error In Query"

@app.route("/delete")
def delete():
    id = request.args.get('id')
    delw = "delete from users where id = '{}'".format(id)
    try:
        cursor.execute(delw)
        db.commit()
        return redirect(url_for('appointment'))
    except:
        db.rollback()
        return "Error In Query"
    
@app.route("/edit")
def edit():  
    id = request.args.get('id')
    selc = "select * from users where id='{}'".format(id)
    cursor.execute(selc)
    data = cursor.fetchone()
    return render_template("edit.html",row=data)
    
@app.route("/update",methods=['POST'])
def update():
    sno = request.form.get('id')
    name = request.form.get('fname')
    last = request.form.get('lname')
    contact = request.form.get('contact')
    email = request.form.get('email')
    car_num = request.form.get('carnum')
    dist = request.form.get('km')
    car_name = request.form.get('carname')
    atime = request.form.get('atime')
    dtime = request.form.get('dtime')
    total = request.form.get('total')
    insq = "update users set First_Name='{}',Last_Name='{}',Contact_no='{}',Email='{}',Car_number='{}',Km_Run='{}',Car_name='{}',Arrived_time='{}',Delivery_time='{}',Total_amount='{}' where id={}".format(name,last,contact,email,car_num,dist,car_name,atime,dtime,total,sno)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('appointment'))
    except:
        db.rollback()
        return "Error In Query"

@app.route("/getdata",methods=["POST"])
def getdata():
    sno = request.form.get('id')
    selu = "select * from users where id={}".format(sno)
    cursor.execute(selu)
    data = cursor.fetchone()
    return render_template("search.html",row=data)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)