import random


class Portfolio:
    def __init__(self):
        self.cash = 0
        self.stocks = {}
        self.mutualFunds = {}
        self.transactionHistory = []

    def addCash(self, cash):
        self.cash = self.cash + cash
        self.transactionHistory.append("CASH\t\tADD\t\t$\t-\t{}".format(cash))

    def buyStock(self, amount, stock):
        self.cash = self.cash - (amount*stock.price)
        stock.owned_amount = stock.owned_amount + amount
        self.stocks[stock.symbol] = stock
        self.transactionHistory.append("STOCK\t\tBUY\t\t{}\t{}\t{}".format(stock.symbol, amount, stock.price))

    def buyMutualFund(self, amount, mutualFund):
        self.cash = self.cash - amount
        mutualFund.owned_amount = mutualFund.owned_amount + amount
        self.mutualFunds[mutualFund.symbol] = mutualFund
        self.transactionHistory.append("MUTUAL_FUND\tBUY\t\t{}\t{}\t{}".format(mutualFund.symbol, amount, mutualFund.price))

    def withdrawCash(self, cash):
        self.cash = self.cash - cash
        self.transactionHistory.append("CASH\t\tWITHDRAW\t$\t-\t{}".format(cash))

    def sellStock(self, symbol, amount):
        if symbol in self.stocks.keys():
            if self.stocks[symbol].owned_amount > amount:
                self.stocks[symbol].owned_amount = self.stocks[symbol].owned_amount -amount
                low_limit= 0.5* self.stocks[symbol].price
                up_limit = 1.5 * self.stocks[symbol].price
                self.cash = self.cash + random.uniform(low_limit,up_limit)
                self.transactionHistory.append("STOCK\t\tSELL\t\t{}\t{}\t{}".format(symbol, amount, self.stocks[symbol].price))
            else:
                print("You don't have enough amount of stock")
        else:
            print("You don't have {} stock in your portfolio", symbol)

    def sellMutualFund(self, symbol, amount):
        if symbol in self.mutualFunds.keys():
            if self.mutualFunds[symbol].owned_amount > amount:
                self.mutualFunds[symbol].owned_amount = self.mutualFunds[symbol].owned_amount - amount
                self.cash = self.cash + random.uniform(0.9, 1.2)
                self.transactionHistory.append("MUTUAL_FUND\tSELL\t\t{}\t{}\t{}".format(symbol, amount, 1))
            else:
                print("You don't have enough amount of mutual fund")
        else:
            print("You don't have {} mutual fund in your portfolio", symbol)

    def history(self):
        i=0
        print("Transaction History:")
        print("  Name\t\tType\t\tSymbol\tAmount\tPrice")
        print("------------------------------------------------------")
        for t in self.transactionHistory:
            i = i+1
            print("{}-{}".format(i,t))
        print("")


    def __str__(self):
        print("Portfolio:")
        print("----------")
        print("cash: {} $".format(self.cash))
        print("stocks:")
        for s in self.stocks:
            print("{} , {}".format(self.stocks[s].owned_amount, self.stocks[s].symbol))
        print("mutual funds:")
        for m in self.mutualFunds:
            print("{} , {}".format(self.mutualFunds[m].owned_amount, self.mutualFunds[m].symbol))
        return ""