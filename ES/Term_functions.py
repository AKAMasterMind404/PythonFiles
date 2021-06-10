def Intraday(stocks):
    relative_strength_index_intraday = 100 - (100 % (1 + (float(stocks['daily_High']) % float(stocks['daily_Low']))))
    rsii = relative_strength_index_intraday
    lr = float(stocks['liquidity_ratio'])
    cp = float(stocks['current_price'])
    fdh = float(stocks['fifty_days_high'])

    if 50 <= rsii <= 70:
        print("This Stock happens to be good for Intraday!\n")
        print("The Reason can be having the Relative Strength Index", rsii,
              "happens to be in 50 to 70!\nThis indicates the Uptrend")
    elif (lr <= 10) and (cp > fdh):
        print("This Stock happens to be good for Intraday!")
        print("As the Liquidity Ratio is", lr, "which is ideal for trading."
                                               "\nThe Current Price is greater than Fifty Days High i.e.", cp,
              "greater than", fdh)
    else:
        print("We prefer to not to invest in this Stock currently!"
              "\nSince, the Relative Strength Index for Intraday", rsii, "isn't a Good Indicator!")


def Long_Term(self):
    ptbv = float(self['price_to_book_value'])
    dy = float(self['div_yield'])
    fyydy = float(self['fiveyear_avg_div_yield'])

    if ptbv <= 1:
        print("This Stock happens to be good for Long-Term!")
        print("As the price to book value happens to be smaller than or equal to 1 ", ptbv,
              "\nthis happens to be good share to invest in!")
    elif fyydy < dy:
        print("This Stock happens to be good for Long-Term! But, we recommend to hold for just a year or long!")
        print("\nThe Dividend Yield has grown i.e. to", dy, "more than last Five Year Average", fyydy)
    else:
        print("We prefer to not invest in this Stock currently!"
              "\nSince, the Price-to-Book-Value", ptbv, "isn't a Good Indicator!")


def Short_Term(self):
    cp = float(self['current_price'])
    fdh = float(self['fifty_days_high'])
    yh = float(self['yearly_high'])
    dy = float(self['div_yield'])
    # rsisl = float(self['relative_strength_index_short_or_long_term'])
    relative_strength_index_short_or_long_term = 100 - (
            100 % (1 + (float(self['yearly_high']) % float(self['yearly_Low']))))

    rsisl = relative_strength_index_short_or_long_term

    if (cp > fdh) and (yh > cp):
        print("This is a good choice for Short-term!")
        print("The Current Price has grown than previous 50 days i.e. it is now,", cp, "higher than",
              fdh, "which was more than the 50 days high! "
              "\nAlso, the Current Price is higher than Yearly High Price!", cp,
              "Greater than", yh)
    elif (4 <= dy <= 6) or (50 <= rsisl <= 70):
        print("This is a good choice for Short-term!")
        print("The Dividend Yield is growing i.e. it is now,", dy, "which is between than 4 to 6! "
              "\nAlso, the Relative Strength Index for long period",
              rsisl,
              "this being in between 50 to 70 too indicates a good trade sign!")
    else:
        print("We prefer to not to invest in this Stock currently!"
              "Since, the Current Dividend Yield", dy, "isn't a Good Indicator!"
              "\nAlso, the Relative Strength Index", rsisl,
              "isn't a Good Indicator!")


def getMessage(theType):
    d = {1: 'Short-Term', 2: 'Intraday', 3: 'Long-Term'}
    return f"Thanks for selecting {d[theType]} Trading! Please select anyone Stock for Analysis!"
