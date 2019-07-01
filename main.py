from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("user-signup.html")


@app.route("/", methods=['POST'])
def repost():
    
    name = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    name.format(name)
    password.format(password)
    verify.format(verify)
    email.format(email)
    
    
    first_place = ""
    second_place = ""
    third_place = ""
    fourth_place = ""
    
    if  name == "":
        first_place = "You need to enter a name."
        name = ""        
    elif " " in name:
        first_place = "No spaces in username."
        name = ""        
    elif len(name) < 2:
        first_place = "Name must be more 2 and less than 21 characters" 
        name = ""        
    elif len(name) > 21:
        first_place = "Name must be more 2 and less than 21 characters"                                  
        name = ""                                         
    else:
        name = name

    if  password == "":
        second_place = "You need to enter a password."
        password = "" 
    elif " " in password:
        second_place = "No spaces in password."
        password = ""
    elif len(password) < 2:
        second_place = "Password has to be more than 3 and less than 21 characters" 
        password = ""
    elif len(password) > 21:
        second_place = "Password has to be more than 3 and less than 21 characters"                                  
        password = ""                                
    else:
        password = password

    
    if verify != password:
        third_place = "The password and verify have to match."                                  
        verify = ""                                       
    else:
        verify = verify    

    if len(email) == 0:
        email =email    
    elif  "@@" in email:
        fourth_place = "A single @ symbol in your email address."
        email = ""        
    elif "@" not in email:
        fourth_place = "The email address needs to have an @ symbol."
        email = ""          
    elif ".." in email:
        fourth_place = "A single period in your email address."
        email = ""        
    elif "." not in email:
        fourth_place = "You need a period in the email address."
        email = ""                
    elif " " in email:
        fourth_place = "No spaces in verifying characters."
        email = ""        
    elif len(email) < 2:
        fourth_place = "Verifying characters has to be greater than 3." 
        email = ""        
    elif len(email) > 20:
        fourth_place = "No more than 20 characters."                                  
        email = ""                                               
    else:
        email = email
    if not first_place and not second_place and not third_place and not fourth_place:
        name = name
        return redirect("/welcome?username={0}".format(name))

    else:
        return render_template("user-signup.html", name = name, first_place = first_place, 
                                               password = password, second_place = second_place, verify = verify,
                                               third_place = third_place, email = email,fourth_place = fourth_place)

@app.route("/welcome")
def signup():
    username = request.args.get('username')  
    return render_template("welcome.html", name = username)
    


   
app.run()