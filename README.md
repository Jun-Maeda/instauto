# Name
 
instauto
 
Instagramの指定ハッシュタグの検索で表示された投稿に自動でいいねをつける。
また、もしフォローしていなければ自動フォロー、コメントをする。
 
# DEMO
 
インスタでなかなかフォロワーが増えない。。。いいねをつけるのが面倒。。。
そんなあなたにぜひ ""instaauto"" を。
 
# Features
 
ただ "いいね" をつけるだけでなく、フォローしていないアカウントには自動でフォローします。
その上、フォロー時にはコメントを残すことができます。
 
# Requirement
 
- autopep8==1.5.4
- chromedriver-binary==87.0.4280.88.0
- docopt==0.6.2
- et-xmlfile==1.0.1
- jdcal==1.4.1
- openpyxl==2.4.11
- pycodestyle==2.6.0
- python-dotenv==0.15.0
- records==0.5.3
- selenium==3.141.0
- SQLAlchemy==1.3.22
- tablib==3.0.0
- toml==0.10.2
- urllib3==1.26.2

chromedriver-binaryについては使用するPCの環境に合ったバージョンに変更してください。

 
# Installation
 
```bash
git clone https://github.com/Jun-Maeda/instauto.git
touch .env
echo USERNAME="インスタアカウント名" >> .env
echo PASSWORD="インスタパスワード" >> .env
echo DBNAME=データベース名.db >> .env
echo COMMENT="コメント文" >> .env
echo HASHTAG="ハッシュタグの名前" >> .env
python3 venv venv
source venv/bin/activate
pip install -r requirements.txt
```
 
# Usage

```bash
pip install -r requirements.txt
python db_init.py
python main.py
```
 
# Note
 
一度いいねをしていたものはもう一度実行するといいねを取り消してしまうので注意。
 
# Author
 

 
* 作成者 Jun
 
# License

あくまで個人で使用し、サーバーに負担がないレベルで使用してください。