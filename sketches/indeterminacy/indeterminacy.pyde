# Define constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
NUM_POINTS = 35
NUM_STOCKS = 40
INITIAL_PRICE = 100
PRICE_RANGE = 5

def setup():
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    background(235, 230, 230)
    
    
    global stocks
    stocks = []
    for i in range(NUM_STOCKS):
        stock_prices = [INITIAL_PRICE]
        for j in range(NUM_POINTS):
            # Calculate the new price and add it to the list of prices
            price = stock_prices[-1] + random(-PRICE_RANGE, PRICE_RANGE)
            stock_prices.append(price)
        stocks.append(stock_prices)

    # Find the minimum and maximum prices across all stocks
    min_price = min([min(stock) for stock in stocks])
    max_price = max([max(stock) for stock in stocks])

    # Draw the lines
    for stock in stocks:
        for i in range(len(stock) - 1):
            # slide x values to the right and map to desired range
            x1 = map(i, 0, len(stock) - 1, 0, width)
            x2 = map(i + 1, 0, len(stock) - 1, 0, width)
            
            # map the stock price to the desired range
            y1 = map(stock[i], min_price, max_price, 0, height)
            y2 = map(stock[i+1], min_price, max_price, 0, height)
            
            if stock[i+1] > stock[i]:
                stroke(random(0,255), random(0,255), random(0,255), random(200,220))

                strokeWeight(random(9,10))
            elif stock[i+1] < stock[i]:
                stroke(random(0,255), random(0,255), random(0,255), random(230,240))
                
                strokeWeight(random(4,20))
            else:
                stroke(0)
            line(x1, y1, x2, y2)
