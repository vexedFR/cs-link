from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define the main route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        year = request.form["year"]
        year2 = year[-2:]
        sess = request.form["session"]
        session = sess.lower()
        paper = request.form["paper"]
        variant = request.form["variant"]

        # Create URLs based on form data
        qp_link = f"https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/{year}/9618_{session}{year2}_qp_{paper}{variant}.pdf"
        ms_link = f"https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/{year}/9618_{session}{year2}_ms_{paper}{variant}.pdf"
        
        # Render the result.html template with generated URLs
        return render_template("result.html", qp_link=qp_link, ms_link=ms_link)
    
    # Render the index.html form if it's a GET request
    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)