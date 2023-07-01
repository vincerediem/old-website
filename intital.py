from flask import Flask, render_template, request
app = Flask(__name__)
import sys
sys.path.append(r"C:\Users\kopen\OneDrive\Desktop\Code\Algo Trading\RSI\RSI 2")
import RSIv2_html as rsi2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    stocks = request.form.get('stock_symbols')
    stock_list = stocks.split()

    final_balance, initial_balance, stock, row, positions, cash, trade_gains_losses = rsi2.backtest_strategy(stocks.split())
    metrics = rsi2.display_final_metrics(final_balance, initial_balance, stock, row, positions, cash, trade_gains_losses)
    return render_template('result.html', result=metrics)

def perform_calculations(stock_symbols):
    final_balance, initial_balance, stock, row, positions, cash, trade_gains_losses = rsi2.backtest_strategy(rsi2.stock_list(stock_symbols))
    results = rsi2.display_final_metrics(final_balance, initial_balance, stock, row, positions, cash, trade_gains_losses)
    return results  # You'll need to adjust the display_final_metrics function to return results instead of print

if __name__ == '__main__':
    app.run(debug=True)