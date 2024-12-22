<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
</head>
<body>
    <div class="container">
        
To create virtual environment of python we need to write t:
python3 -m venv web_venv
web_venv is the name of the virtual environment

To activate virtual environment:
source web_venv/bin/activate

To make the website available on the Local Area Network, the following command must be written in the terminal (inside the directory which contains all the files and folders + inside the virtual environment to access all the modules)
flask run --host=192.168.0.100 --port=5000
After this we can access the website from any device in the same Wi-Fi network using the following IP Address
http://192.168.0.100:5000

You can get the IP Address of the Macbook by running the following command in my terminal:
ifconfig | grep inet



If we just write the following in the terminal:
flask run or
python3 app.py 
Then the website will be only accessible from that local machine using the IP Address which looks like this:
http://127.0.0.1:5000

</body>
</html>
