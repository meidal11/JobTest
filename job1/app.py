from flask import Flask, render_template
import docker

app = Flask(__name__, template_folder='templates')

client = docker.from_env()
answer = client.containers.list()

@app.route('/')
def hello():
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
#if you want it in the console
print (client.containers.list(all=True))



