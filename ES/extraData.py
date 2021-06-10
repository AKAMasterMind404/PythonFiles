# # Questions
#
# q1 = print("Hello! Myself Stockish.Do you want to know about a stock?")
# q3 = print("What is your Budget?")
# q4 = print("Which Sector do you want to invest in.")
# q5 = print("What type of Trade do you wish to Enter in?")
#
#
# def getMessage(theType):
#     d = {'i': 'Intraday', 's': 'Short-Term', 'l': 'Long-Term'}
#     return f"Thanks for selecting {d[theType]} Trading! Please select anyone Stock for Analysis!"
#
#
# q9 = print(
#     "If you wish we can analyze this Share for other Terms as well, should we? "
#     "This option will Tell you when exactly to Exit the Trade!")
# # q10 = print("Also, the Exit time for this is today or next Market Session!")
# q10 = print("Which type of Financial Statements do you wish?")
# q11 = print("If you wish we can given Financial Statements of the given Company?")
#
# # Sectors
#
# def showSectors():
#     sectors = {'ir': 'Internet Retail', 'si': 'Software-Infrastructure', 'ce': 'Consumer Electronics',
#                'am': 'Auto Manufacturers', 'drug': 'Drug Manufacturers—Specialty & Generic'
#                }
#     print(sectors)
#
#
# "Deprecated Functions" ##########################
#
#
# def Intraday(relative_strength_index_intraday,liquidity_ratio,current_price,fifty_days_high):
#     if ((50<=relative_strength_index_intraday<=70) or (liquidity_ratio<=10)) and (current_price>fifty_days_high):
#         print("This Stock happens to be good for Intraday!")
#         print("The Reason can be having the Relative Strength Index",relative_strength_index_intraday,"happens to be in 50 to 70! This indicates the Uptrend")
#     else:
#         print("We prefer to not to invest in this Stock currently!")
#
# def Long_Term(price_to_book_value):
#     if (price_to_book_value<=1) and ():
#         print("This Stock happens to be good for Intraday!")
#     else:
#         print("We prefer to not to invest in this Stock currently!")
#
# def Short_Term(current_price,fifty_days_high,yearly_high,div_yield,relative_strength_index_short_or_long_term):
#     if (current_price>fifty_days_high) and (yearly_high>current_price) or (4<=div_yield<=6) or (50<=relative_strength_index_short_or_long_term<=70):
#         print("This is a good choice for Short-term!")
#     else:
#         print("We prefer to not to invest in this Stock currently!")