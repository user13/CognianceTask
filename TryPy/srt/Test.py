import unittest
import re
from ServerApi import ServerApi 

class Test(unittest.TestCase):
    
    def setUp(self):
        pass
   
    def tearDown(self):
        pass

# ---ShowAll---
       
    def test_showAll(self):
        api = ServerApi()
        self.assertEqual(200, api.showAll().status_code, msg=(''))
  
# ---ShowById---
   
    def test_showById1(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById(0).status_code, msg='') 
      
    def test_showById2(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById(3.0).status_code, msg='') 
      
    def test_showById3(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById(-1).status_code, msg='') 
     
    def test_showById5(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById("[").status_code, msg='')
  
    def test_showById6(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById("a").status_code, msg='')
  
    def test_showById7(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById("").status_code, msg='')
  
    def test_showById8(self):
        api=ServerApi()
        self.assertNotEqual(200, api.showById(" ").status_code, msg='')
  
# ---Delete---
  
    def test_delete1(self):
        api=ServerApi()
        self.assertNotEqual(200, api.delete(0).status_code, msg='') 
  
    def test_delete2(self):
        api=ServerApi()
        self.assertNotEqual(200, api.delete("h").status_code, msg='') 
  
    def test_delete3(self):
        api=ServerApi()
        self.assertNotEqual(200, api.delete("[").status_code, msg='') 
      
    def test_delete4(self):
        api=ServerApi()
        self.assertNotEqual(200, api.delete(-1).status_code, msg='') 
  
# ---Add---
  
    def test_Add1(self):
        api=ServerApi()
        name = ''
        position = '' 
        actual = api.add(name, position)
        self.assertEqual(201, actual.status_code, msg='')
  
    def test_Add2(self):
        api=ServerApi()
        name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        position = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        actual = api.add(name, position)
        self.assertEqual(201, actual.status_code, msg='')
   
    def test_Add3(self):
        api=ServerApi()
        name = '0123456789'
        position = '0123456789' 
        actual = api.add(name, position)
        self.assertEqual(201, actual.status_code, msg='')
   
    def test_Add4(self):
        api=ServerApi()
        name = '!$%^&*()_+-=<>?,./[]{}|\@~`'
        position = '!$%^&*()_+-=<>?,./[]{}|\@~`' 
        actual = api.add(name, position)
        self.assertEqual(201, actual.status_code, msg='')

    def test_chekAdd(self):
        api = ServerApi()
        countBefore = self.countAll(api.showAll().text)
        add = api.add('name', 'position')                            
        countAfter = self.countAll(api.showAll().text)
        api.delete(self.findId(add.text)[0])
        self.assertNotEqual(countBefore, countAfter, msg='')
    
    def test_checkDelete(self):
        api = ServerApi()
        add = api.add('name', 'position')
        idAdd = self.findId(add.text)[0]
        api.delete(idAdd)
        res = self.findId(api.showAll().text)[0]
        for i in range(len(res)):
            self.assertNotEqual(idAdd, res[i], msg="") 
#       
    def test_checkShowById(self):
        api=ServerApi()
        add = api.add('name', 'position')
        show = api.showById(self.findId(add.text)[0])
        api.delete(self.findId(add.text)[0])
        self.assertEqual(self.findId(add.text)[0], self.findId(show.text)[0], msg = '')
        
   
    def findId(self, myStr):
        patern = re.compile('.id.:.(\d*).')
        result = patern.search(myStr).groups()
        return result
    
    def countAll(self, myStr):
        patern = re.compile('.id.:.[\d]*')
        count = len(patern.findall(str(myStr)))
        return count


if __name__ == '__main__':
    unittest.main()