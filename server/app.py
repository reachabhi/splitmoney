from flask import Flask


app=Flask(__name__)

@app.route("/welcome")
def welcome():
    print("~~~~~~ Hello All ~~~~~~")

if(__name__)=='__main__':
    app.run()