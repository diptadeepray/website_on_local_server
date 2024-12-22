<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
</head>
<body>
    <div class="container">
        
<h3>To create virtual environment of python we need to write the following in the terminal:</h3>
<strong><i>python3 -m venv web_venv</i></strong>
web_venv is the name of the virtual environment

<h3>To activate virtual environment:</h3>
<strong><i>source web_venv/bin/activate</i></strong>

<h3>To make the website available on the Local Area Network,</h3>
the following command must be written in the terminal (inside the directory which contains all the files and folders + inside the virtual environment to access all the modules)
<strong><i>flask run --host=192.168.0.100 --port=5000</i></strong>
<h3>After this we can access the website from any device in the same Wi-Fi network using the following IP Address:</h3>
<i>http://192.168.0.100:5000</i>

<h3>You can get the IP Address of the Macbook by running the following command in my terminal:</h3>
<strong><i>ifconfig | grep inet</i></strong>



<h3>If we just write the following in the terminal:</h3>
<strong><i>flask run</i></strong> or
<strong><i>python3 app.py</i></strong>
<h3>Then the website will be only accessible from that local machine using the IP Address which looks like this:</h3>
<i>http://127.0.0.1:5000</i>

</body>
</html>
