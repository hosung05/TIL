from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template(
        'search_stock.html',
        is_first_stcok_=True,
    )

@app.route('/search_result')
def result():
    user_input = request.args.get('keyword')

    TOKEN = 'pk_935931b54f044ce386d87df582ff6da8'
    user_input = request.args.get('keyword')
    if user_input:
        stock = Stock(use0r_input, token=TOKEN)
        data = stock.get_quote()
    else:
        return render_template(
            'search_stock.html',
            is_search=True
        )

    try:
        data = stock.get_quote()
    except:
        return render_template(
            'search_stock.html',
            is_search=True
        )
    # pp.pprint(aapl.get_quote())

    return render_template(
        'search_stock.html',
        is_success=True,
        c_name=data['companyName'],
        l_price=data['latestPrice'],
                           )

if __name__ == '__main__':
    app.run(debug=True)