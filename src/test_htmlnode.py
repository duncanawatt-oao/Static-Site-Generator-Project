from htmlnode import *


node = HTMLNode("<a>", "a value", "a child or two", {"a key": "and its prop"})
node2= HTMLNode("img", "another value", None, None)
node3 = HTMLNode("<b>", "a third value", "a child or two", {"a key": "and its prop", "another key": "another prop"})



def test_to_html():
    try:
        node.to_html

    except Exception as e:
        print(e)

def test_props_to_html():
    print("Testing props to html:")
    res_one = node.props_to_html
    res_two = node3.props_to_html
    
    print(res_one)
    print(res_two)
