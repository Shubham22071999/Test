# this is restful api using flask

from flask import Flask, jsonify, request
from query_latest2_database import number
from query_sqkite_database import bin_num, card_typ, card_catg, bank
from multi_threading_function import threading_addition
app = Flask(__name__)

@app.route('/',methods=["POST"])
def hello_world():
   return 'Hello World!'

@app.route('/acc_finder',methods=["POST"])
def acc_finder():
    bin_number=request.form["bin_number"]
    bin_no=request.form["bin_no"]
    # result1=bin_num(bin_no)
    # result2=number(bin_number)
    result= threading_addition()
    # print(result1)
    # print(result2) 
    # return jsonify({**result1,**result2})
    return jsonify(result)

@app.route('/bin_number_finder',methods=["POST"])
def bin_number_finder():
    try:
        bin_number=request.form["bin_number"]
    except:
        return{"status":"oops bin_number key not provided"}
    # name=request.form["name"]
    result=number(bin_number)
    return jsonify(result)

@app.route('/bin_num_finder',methods=["POST"])
def bin_num_finder():
    try:
        bin_no=request.form["bin_no"]
    except:
        return{"status":"oops bin_num key not provided"}
    result=bin_num(bin_no)
    return jsonify(result)

@app.route('/card_type_finder',methods=['POST'])
def card_type_finder():
    try:
        card=request.form['card']
    except:
        return{"status":"oops card key not provided"}
    result=card_typ(card)
    return jsonify(result)

@app.route('/card_category_finder',methods=['POST'])
def card_category_finder():
    try:
        catg=request.form['catg']
    except:
        return{"status":"oops catg key not provided"}
    result=card_catg(catg)
    return jsonify(result)

@app.route('/bank_name_finder',methods=['POST'])
def bank_name_finder():
    try:
        bank_name=request.form['bank_name']
    except:
        return{"status":"oops bank_name key not provided"}
    result=bank(bank_name)
    return jsonify(result)





@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10
    
    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "armstrong": True,
            "Server IP": "122.234.213.53",
            "Other Number": [1,23,43,5,3]
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "armstrong": False,
            "Server IP": "122.234.213.53",
            "Other Number": [1,23,43,5,3]
        }
    return jsonify(result)

if __name__ == '__main__':
   app.run(debug=True)

