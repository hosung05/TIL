from flask import Flask, render_template  # pip install requests
import requests  # pip install requests
import random
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    return render_template('pick_lotto.html', numbers=lucky_numbers)


@app.route('/get_lotto/<int:num>')
def get_lotto(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type == String
    data = json.loads(res)  # type == dict

    real_numbers = []

    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()

    return render_template(
        'get_lotto.html',
        numbers=real_numbers,
        draw_no=num
    )


@app.route('/lotto/<int:num>')
def lotto(num):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()

    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type == String
    data = json.loads(res)  # type == dict
    bonus_number = data['bnusNo']

    real_numbers = []

    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()

    # 등수 비교
    lucky = set(lucky_numbers)
    real = set(real_numbers)

    match_count = len(real.intersection(lucky))

    result = '꽝'
    if match_count == 6:
        result = 1
    elif match_count == 5 and bonus_number in lucky_numbers:
        result = 2
    elif match_count == 5:
        result = 3
    elif match_count == 4:
        result = 4
    elif match_count == 3:
        result = 5

    return render_template(
        'lotto.html',
        result=result,
        real_numbers=real_numbers,
        lucky_numbers=lucky_numbers,
        bonus=bonus_number,
        winning=data['firstAccumamnt']
    )

@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
