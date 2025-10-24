import unittest

def get_formatted_name(first, last):
    """生成整洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()
    
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_get_formatted_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
