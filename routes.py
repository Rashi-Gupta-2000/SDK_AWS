from email.mime import image
from flask import Flask,render_template,redirect,url_for,request
import s3
import ec2
import boto3
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/create')
def ec2create():
    return render_template("form.html")

@app.route('/created_ec2', methods=['POST'])
def created_ec2():
    # ec2 = boto3.client('ec2')
    if request.method == 'POST':
        image_id = request.form['imageid']
        mincount = int(request.form['mincount'])
        maxcount = int(request.form['maxcount'])
        instance_type = request.form['instancetype']
        ec2.create_instances(image_id,mincount,maxcount,instance_type)
    return render_template("success.html")

@app.route('/list')
def ec2listing():
    li = ec2.list_instances()
    return render_template("ec2list.html",list=li)

@app.route('/stop/<id>')
def ec2stop(id):
    ec2.stop_instances(id)
    return render_template("ec2stop.html")
    

@app.route('/start/<id>')
def ec2start(id):
    ec2.start_instances(id)
    return render_template("ec2start.html")

@app.route('/terminate/<id>')
def ec2terminate(id):
    ec2.terminate_instances(id)
    return render_template("ec2term.html")

@app.route('/create_bucket')
def creates3():
    return render_template("s3form.html")

@app.route('/create_s3', methods=['POST'])
def create_bucket():
    if request.method == 'POST':
        name = request.form['bucket_name']
        s3.create_bucket(name)
    return render_template("creates3.html")

@app.route('/list_bucket')
def s3list():
    li=s3.list_bucket()
    return render_template('s3list.html',list=li)

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
