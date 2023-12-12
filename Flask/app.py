from flask import Flask
import csv
from datetime import datetime


HASH = "17.55.18.263808"

f = None
wr = None
def reopenFile():
    global f, wr
    try:
        f.close()
    except:
        print("> Close Failed")
    
    f = open("Location" + HASH + ".csv", 'a')
    wr = csv.writer(f)

app = Flask(__name__)

@app.route('/<id>/<int:range>')
def home(id:str, range:int):
    wr.writerow([
        datetime.now().strftime("%H:%M:%S.%f"),
        id,
        str(range)
    ])

    reopenFile()

    if id=="A":
        print("%8d|        |"%range)
    elif id=="B":
        print("        |%8d|"%range)
    elif id=="C":
        print("        |        |%8d"%range)
    return 'OK'

if __name__ == '__main__':
    reopenFile()
    app.run(host='0.0.0.0', port=5050 ,debug=True)