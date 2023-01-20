import unittest
class funcTest(unittest.TesrCase):
  def test_1 (self):
    self.assertEqual(f(0, 0), 0)
    
  def test_2 (self):
    self.assertEqual(f(1, 2), 5)
    
  def test_3 (self):
    self.assertEqual(f(2, 2), 8)
 
if __name__ == "__main__":
    unittest.main()
