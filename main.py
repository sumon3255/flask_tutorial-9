from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/textanalyzer",methods=['GET','POST'])
def textAnalyze():
    text = request.args.get('text')
    wordcount = request.args.get('wordcount',default="off")
    removepunch =  request.args.get('removepunc',default="off")

    if wordcount == "on":
        text = text.split()
        analyzed = len(text)

    elif  removepunch== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in text:
            if char in punctuations:
                text = text.replace(char,"")
        analyzed = text
    
    else:
        return "error"
    params = {'task':'Word Counting','analyzed_text':analyzed}
    return render_template('analyze.html',params=params)
  



if __name__ == "__main__":
    app.run(debug=True)