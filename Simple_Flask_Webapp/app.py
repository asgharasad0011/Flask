from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)


# @app.route("/", methods=["GET"])
# def Welcome():
#     return ("Welcome to the home page")

# @app.route("/index", methods=["GET"])
# def Index():
#     return ("Welcome to the index page")
 
@app.route("/success/<int:scores>")
def success(scores):
    return ("The Person is pass and average scores are: "+ str(scores))

@app.route("/fail/<int:scores>")
def fail(scores):
    return ("The Person is fail and average scores are: "+ str(scores))

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        maths = float(request.form["Maths"])  # Corrected key access
        com = float(request.form["Computer"])  # Corrected key access
        phy = float(request.form["Physics"])  # Corrected key access

        total_marks=(maths + com + phy)

        ave_marks = total_marks / 3  # Calculate average

        # return render_template("form.html", score=ave)  # Pass `score` to template

        res=""
        if ave_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res, scores=ave_marks))




if __name__=="__main__":
    app.run(debug=True)
