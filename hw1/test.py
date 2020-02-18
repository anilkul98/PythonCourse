import unittest
import Portfolio,MutualFund,Stock

class test(unittest.TestCase):

    def testCashBalance(self):

        portfolio = Portfolio.Portfolio()
        portfolio.addCash(300)
        portfolio.withdrawCash(150)
        self.assertEqual(150, portfolio.cash)

    def testStock(self):

        portfolio = Portfolio.Portfolio()
        s = Stock.Stock(20, "HFH")
        portfolio.buyStock(5, s)
        self.assertEqual(portfolio.stocks["HFH"].owned_amount, 5)
        portfolio.sellStock("HFH", 3)
        self.assertTrue(portfolio.stocks["HFH"].owned_amount == 2, "True amount of stock sold!")

    def testMutalFund(self):
        portfolio = Portfolio.Portfolio()
        mf = MutualFund.MutualFund("BRT")
        portfolio.buyMutualFund(8, mf)
        self.assertEqual(portfolio.mutualFunds["BRT"].owned_amount, 8)
        portfolio.sellMutualFund("BRT", 3)
        self.assertTrue(portfolio.mutualFunds["BRT"].owned_amount == 5, "True amount of Mutual Fund sold!")


if __name__ == "__main__":
    unittest.main()