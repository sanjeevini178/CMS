import unittest
import adminmain
import DLL
import dequeagain

class testAdmin(unittest.TestCase):
    emp = ["EMP","Admin","admin","rootroot12","9999999999","admin@admin.com","M"]
    #obj = adminmain.add_employee
    def test_valid_phone(self):
        obj = adminmain.valid_phone(testAdmin.emp[4])
        obj2 = adminmain.valid_phone(testAdmin.emp[5])
        self.assertEqual(obj, True)
        self.assertEqual(obj2, False)
    
    def test_valid_pwd(self):
        a = adminmain.valid_pwd(testAdmin.emp[3])
        b = adminmain.valid_pwd(testAdmin.emp[2])
        self.assertEqual(a, True)
        self.assertEqual(b, False)

class test_DLL(unittest.TestCase):
    obj = DLL.DoublyLinkedList()
    # obj._insert_btn(10, None, None)
    def test_is_empty(self):
        self.assertTrue(test_DLL.obj.is_empty())
    
    def test_is_full(self):
        self.assertFalse(test_DLL.obj.is_full())

class test_Deque(unittest.TestCase):
    obj = dequeagain.Deque()
    obj.insert_first(10)
    def test_first(self):
        self.assertEqual(test_Deque.obj.first(), 10)
    
    def test_last(self):
        test_Deque.obj.insert_last(11)
        self.assertEqual(test_Deque.obj.last(), 11)