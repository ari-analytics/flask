from flask import Flask
import numpy as np
import matplotlib.pyplot as ppt

app = Flask(__name__)

@app.route('/')

def hello_world():
	x = np.linspace(0,10,100)
	y = np.sin(x)
	ppt.plot(x,y)
	return 'Hello World!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')

