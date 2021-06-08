from flask import Flask, render_template, jsonify
from flask.globals import request
from sqlalchemy import create_engine, text
  
app = Flask(__name__)

def create_app(test_config = None):
    app.config.from_pyfile('config.py')

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
    app.database = database

    @app.route('/Join', methods = ['POST'])
    def Join():
        user = request.json
        user_id = app.database.execute(text("""
                                            INSERT INTO users (
                                            email,
                                            password
                                           ) VALUES (
                                            :email,
                                            :password
                                           )
                                            """), user).lastrowid

        return "", 200

    return app

# 메인페이지 
@app.route('/')
def main():
    return render_template('main.html')

#FAQ페이지 (자주묻는질문)
@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')

#병원검색 / 예약
@app.route('/HSearch')
def Hsearch():
    return render_template('H.serach.html')

#회원가입 페이지
@app.route('/Join')
def join():
    return render_template('join.html')

#로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')


#마이페이지 - QNA
@app.route('/Myqna')
def Myqna():
    return render_template('Myqna.html')

#마이페이지 - 프로필
@app.route('/Myprofile')
def Myprofile():
    return render_template('Myprofile.html')

#마이페이지 - 자주가는병원
@app.route('/Myhosipital')
def Myhosipital():
    return render_template('Myhosipital.html')

#공지사항
@app.route('Notice')
def Notice():
    return render_template('Notice.html')

#게시글 목록
@app.route('/PostService')
def PostService():
    return render_template('PostService.html')

#게시글 작성
@app.route('Post')
def Post():
    return render_template('Post.html')


#질문게시판
@app.route('Postqna')
def Postqna():
    return render_template('Postqna.html')

    								
if __name__ == '__main__':				
									
    app.run(debug=True)	 