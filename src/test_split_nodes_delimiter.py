from split_nodes_delimiter import *

old_nodes = [
    TextNode("this **is** very **bold**", TextType.PLAIN),
    TextNode("this _stuff is in_ italics", TextType.PLAIN),
    TextNode("and this is just plain", TextType.PLAIN)
]


new_list = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

print("These are the results for ** and BOLD:")

for block in new_list:
    print(block)