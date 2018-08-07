
import argparse
import sys
import lxml.etree
from lxml.etree import tostring

def build_parser():
    parser = argparse.ArgumentParser(prog='clixmod', description='Modify xml or html documents')
    parser.add_argument('xpath', type=str, help='XPATH to modify', metavar='XPATH')
    parser.add_argument('selection_xpath', nargs='*', type=str, help='relative XPATH to select. Use name=XPATH for named groups')
    parser.add_argument('replacement', type=str, help='XML to replace XPATH with. {} for entire match, {1}... for selection XPATHs')
    parser.add_argument('--filter', '-f', action='store_true', help='Show matches rather than output text')
    return parser

def main():
    data = sys.stdin.read()
    for line in run(data, sys.argv[1:]):
        print(line)


def run(data, args):
    args = build_parser().parse_args(args)
    tree = lxml.etree.HTML(data)

    matches = tree.xpath(args.xpath)
    if args.filter:
        for m in matches:
            yield tostring(m, encoding='unicode')
    else:
        for m in matches:
            children = m.xpath('node()')
            child_string = ''.join(map(clixmod_tostring, children))
            output = args.replacement.format(content=child_string)
            try:
                new = lxml.etree.fromstring(output)
            except:
                new = output
            replace_element(m, new)
        yield clixmod_tostring(tree)

def clixmod_tostring(x):
    if isinstance(x, str):
        return x
    else:
        return tostring(x, encoding='unicode')


def insert_after(element, new_element):
    if isinstance(new_element, str):
        element.tail += new_element
    else:
        element.addnext(new_element)

def replace_element(element, new_element):
    insert_after(element, new_element)
    remove(element)

def remove(element):
    parent = element.getparent()
    text_index = parent.index(element) - 1
    print('text_index', text_index)
    if element.tail:
        if text_index == -1:
            parent.text = (parent.text or '') + element.tail
        else:
            previous = parent.getchildren()[text_index]
            previous.tail = (previous.tail or '') + element.tail

    parent.remove(element)
