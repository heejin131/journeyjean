from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random
import korean_age_calculator as kac
import sys
import pandas as pd
import json
import os
import psycopg
from  dotenv import load_dotenv
from psycopg.rows import dict_row

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """

    today = date.today()
    birth_date = datetime.strptime (birthday, "%Y-%m-%d").date()

   # 파이썬 버전 출력
    version = sys.version

   # 랜덤으로 이름이 나오기

    names = ["조민규","강현룡","권오준","서민혁","백지원","안재영","전희진","배형균","조성근"]
    presenter = random.choice(names)

    #만나이 계산
    age = today.year - birth_date.year
    #한국식 나이 계산

    kage = kac.how_korean_age(year_of_birth=birth_date.year)

    #띠 계산
    zodiac = ["🐀 Rat","🐂 Ox", "🐅 Tiger", "🐇 Rabbit", "🐉 Dragon", "🐍 Snake", "🐎 Horse", "🐐 Goat", "🐒 Monkey", "🐓 Rooster", "🐕 Dog", "🐖 Pig"]
    index = (birth_date.year - 4) %12
    zodiac = zodiac[index]
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
       age -= 1

    return {
            "birthday": birthday,
            "age": f"만나이는:{age}살/ 한국나이는:{kage}살 / {zodiac} ",
            "version": sys.version,
            "zodiac" : zodiac,
            "basedate": str(today),
            "os-name" : get_os_pretty_name(),
            "message": "Age calculated successfully!"
            }

def get_os_pretty_name():
    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('PRETTY_NAME='):
                return line.split('=')[1].replace('\n', '').strip('"')
    return None 

load_dotenv()
# DB_CONFIG = {
#     "dbname": os.getenv("DB_NAME"),
#     "user": os.getenv("DB_USERNAME"),
#     "password": os.getenv("DB_PASSWORD"),
#     "host": os.getenv("DB_HOST"),
#     "port": os.getenv("DB_PORT"),
# }

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DATABASE"),
    "user": os.getenv("POSTGRES_USE"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

@app.get("/api/py/select_all")
def select_all():
    with psycopg.connect(**DB_CONFIG, row_factory=dict_row) as conn:
        cur = conn.execute("SELECT * FROM view_select_all")
        rows = cur.fetchall()
        return rows
