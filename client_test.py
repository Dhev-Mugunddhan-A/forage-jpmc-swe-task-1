import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),((quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),((quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2)))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceBequalszero(self):
    prices = [{'priceA':100,'priceB':0},{'priceA':1.5,'priceB':0}]
    for items in prices:
      self.assertEqual(getRatio(items['priceA'],items['priceB']),None)
      
  def test_getRatio_priceAequalszero(self):
    prices = [{'priceA':0,'priceB':1000},{'priceA':0,'priceB':30.8}]
    for items in prices:
      self.assertEqual(getRatio(items['priceA'],items['priceB']),0.0)
    
  def test_getRatio_pricenonzero(self):
    prices = [{'priceA':101.5,'priceB':98.7},{'priceA':117.5,'priceB':1}]
    for items in prices:
      self.assertEqual(getRatio(items['priceA'],items['priceB']),items['priceA']/items['priceB'])
      
      
    


if __name__ == '__main__':
    unittest.main()
