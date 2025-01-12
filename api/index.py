from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random
import korean_age_calculator as kac

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
            "age": str(age) + " (" + zodiac + ") 한국나이:" + str(kage),
            "kage": str(kage)
            "zodiac" : zodiac,
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }

