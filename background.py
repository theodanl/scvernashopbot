import requests



app = Flask('')

@app.route('/')
def home():
    return "bot started"



def run():
    app.run(host= '0.0.0.0', port = 80)


def keep_alive():
    t = Thread(target = run)
    t.start()