from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def racine():
	return "Le chemin de la racine est " + request.path

@app.route('/discussion')
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
    premier_msg = 1 + 50 * (num_page - 1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)



if __name__ == '__main__':
	app.run()