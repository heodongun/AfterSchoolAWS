
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi AWS world / .env 테스트 : {}'.format(con.DB_SCHEMA)

@app.route('/health')
def health():
    return Response("Success Health Check", status=200)


if __name__ == '__main__':
    # db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
    # print("connect ok")
    app.run(host='0.0.0.0')
