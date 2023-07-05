from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)


@app.route('/')
def index():
    app.logger.info('Accessed home page')
    return 'Hello, World!'


@app.route('/user/<username>')
def user_profile(username):
    app.logger.info(f'Accessed user profile: {username}')
    return f'User profile: {username}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

