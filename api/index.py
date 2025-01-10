from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random

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
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
   #띠 계산 
    def calculate_zodiac(birth_date.year):
     zodiac = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양","원숭이", "닭", "개", "돼지"]
     index = (birth_date.year - 4) % 12
     zodiac = calculate_zodiac(birth_date.year)
    return zodiac[index]

    
    return {
            "birthday": birthday,
            "age": str(age),
            "zodiac" : zodiac,
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
