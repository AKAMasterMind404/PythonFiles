from ES import customData as data
from ES import Term_functions as t


def stockRecommender():
    print("\nSTOCK RECOMMENDER")
    print("Welcome,\nHello! Myself Stockish, an Expert System 🔥🔥")

    budget = float(input("\nWhat is your budget? $"))

    print("\nWhich sector do you want to invest in among the below sectors")
    for i in range(len(data.SECTORS)):
        print(f"{i + 1}. {data.SECTORS[i]}")

    sector_to_choose = int(input("\nChoose as per number: "))

    type_of_trade = int(input(  # 1 2 3
        "\nWhat type of trade do you wish to enter in?\n"
        "1.Short-term\n"
        "2.Intra-day\n"
        "3.Long-term\n"
        "Choose as per number: "))

    print(t.getMessage((type_of_trade)))

    print("\nWhich stock do you want us to analyze:")

    num=0
    for i in range(len(data.STOCKS)):
        stock = data.STOCKS[i]
        if float(stock['current_price']) <= budget and stock['Sector'] == data.SECTORS[sector_to_choose - 1]:
            print(f"{i + 1}. {stock['Name']}")
        else:
            num+=1

    if num==7:
        print('No stocks match your selection!Try again.')
    else:
        stock_to_choose = int(input("Choose as per number:"))

        print()
        # print("this is i:", stock_to_choose)
        print(f"You chose to analyse {data.STOCKS[stock_to_choose-1]['Name']}. Great Choice!")
        print()
        if type_of_trade == 1:
            t.Short_Term(data.STOCKS[stock_to_choose-1])
        elif type_of_trade == 2:
            t.Intraday(data.STOCKS[stock_to_choose-1])
        elif type_of_trade == 3:
            t.Long_Term(data.STOCKS[stock_to_choose-1])
        else:
            print("INVALID")

        show_details = input(
            "\nDo you want us to show the details about the stock? Type 'y' for yes, or 'n' for no: ").lower()
        if show_details == 'y':
            for keys, values in data.STOCKS[stock_to_choose - 1].items():
                print(f"{keys}: {values}")

    again = input("\nDo you want us to analyze again? Type 'y' for yes, or 'n' for no: ").lower()

    if again == 'y':
        stockRecommender()
    else:
        print("THANK YOU!")


if __name__ == "__main__":
    stockRecommender()
