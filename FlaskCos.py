from flask import Flask
import random

app = Flask(__name__)

#This return a random num
@app.route("/getRandomNumber")
def getRandomNumber():
    
    
    myrandom = "<h1>" + r + "</h1>"
    
    return myrandom
######################################################
@app.route("/")
def home():
    myhtml = '''
<!DOCTYPE html>
<html>
<head>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
setInterval(function()
{
    $.ajax({
        type:"get",
        url:"/getRandomNumber",
        datatype:"html",
        success:function(data)
        {
            //Whatever is returned by app.route("getTableContents") will be inside the variable "data"
            //all the html inside of the <div class ="random"> will be replaced
            $( ".random").html(data);
        }
    });
}, 500);
</script>
</head>
<body>
<h1>Ajax Example</h1>

Here is your table:
<div class = "table">
This is the table that will be replaced
</div>
</body>
</html>
'''
    return myhtml

###########################################################
if __name__=='__main__':
    app.run(host = '0.0.0.0', port=80)