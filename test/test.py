from clixmod.clixmod import run
import lxml.etree
from lxml.etree import tostring

import unittest


class Test(unittest.TestCase):
    def test_merge(self):
        SIMPLE = '''<html>
        <body>
            <h2>one</h2>
            <h2>two</h2>
        </body>
        </html>'''

        result = ''.join(run(SIMPLE, ['//h2', '<h1>{content}</h1>']))
        tree = lxml.etree.HTML(result)
        self.assertEqual(len(tree.xpath('//h1')), 2)

    def test_string(self):
        DATA = '''
        <html>
        <body>
           one
           <h1></h1>
           two
        </body>
        </html>

        '''
        result = ''.join(run(DATA, ['//h1', '']))
        self.assertTrue('one' in result)
        self.assertTrue('two' in result)
        self.assertTrue(result.index('one') < result.index('two'))


if __name__ == "__main__":
    unittest.main()
