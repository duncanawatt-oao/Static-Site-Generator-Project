from htmlnode import *
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        working_list_splits = old_node.text.split(delimiter)

        if len(working_list_splits) % 2 == 0:
            raise Exception("Closing delimiter missing")
        for i in range(len(working_list_splits)):
            block = working_list_splits[i]
            if block == "":
                continue
            if i % 2 == 0:
                new_node = TextNode(block, TextType.PLAIN)
            else:
                new_node = TextNode(block, text_type)
            new_nodes.append(new_node)

    return new_nodes

#if __name__ == "__main__":
 #   from textnode import TextNode, TextType
#
 #  result = split_nodes_delimiter([node], "**", TextType.BOLD)
  #  print(result)



