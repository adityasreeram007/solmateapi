
from flask import Flask,jsonify
import csv
app=Flask(__name__)

vals=[]
with open('questions.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        vals.append(row)
print(vals)

@app.route('/',methods=['GET'])      
def senddata():
    
    return jsonify({'data':vals})
    


if __name__=='__main__':
    app.run(debug=True)
