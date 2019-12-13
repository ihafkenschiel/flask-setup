# Start working on your project

Each time you work on this project, you need to activate the virtual environment. From a new Terminal window:

```sh
cd helloflask
source bin/activate
```

You can check that your environment is active because virtualenv puts the name of the app before the

Any packages you install now using pip or easy_install get installed into `helloflask/lib/python2.7/site-packages`

---

# Run the application:

```
python helloflask.py
```

You should be able to surf to `http://127.0.0.1:5000` and see a cheery “Hello World!” message.

To stop the server process, press control-C.

---

# List your requirements

When deploying to a webserver it is important to register which requirements we need. To do this we freeze the installed packages and store this setup in a requirements.txt file:

```
pip freeze > requirements.txt
```

This writes a plain text file that contains the names of the required Python packages and their versions, for example Flask==0.9. We’ll use this file later when we’re setting up our server..
