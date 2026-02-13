from htmlnode import *
from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
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
                new_node = TextNode(block, TextType.TEXT)
            else:
                new_node = TextNode(block, text_type)
            new_nodes.append(new_node)

    return new_nodes


def split_nodes_image(old_nodes):

    new_nodes = []
    
    for sample in old_nodes:
            
        if sample.text_type != TextType.TEXT:
            new_nodes.append(sample)
            continue
        
        images_list = extract_markdown_images(sample.text)
        num_images = len(images_list)
        if num_images == 0:
            new_nodes.append(sample)
            continue
        curr_text = sample.text
        for splitter in images_list:
            alt = splitter[0]
            url = splitter[1]
            markdown = f"![{alt}]({url})"
            before, after = curr_text.split(markdown, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            curr_text= after
        if curr_text != "":
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
                             

    return new_nodes





def split_nodes_link(old_nodes):
    new_nodes = []
    
    for sample in old_nodes:
            
        if sample.text_type != TextType.TEXT:
            new_nodes.append(sample)
            continue
        
        links_list = extract_markdown_links(sample.text)
        if len(links_list) == 0:
            new_nodes.append(sample)
            continue
        curr_text = sample.text
        for splitter in links_list:
            link_text = splitter[0]
            url = splitter[1]
            markdown = f"[{link_text}]({url})"
            before, after = curr_text.split(markdown, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            curr_text= after
        if curr_text != "":
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
                             

    return new_nodes

def extract_markdown_images(text):
    results = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return results

def extract_markdown_links(text):
    results = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return results


def text_to_textnodes(text):
    starting_node = TextNode(text, TextType.TEXT)
    nodes = [starting_node]
    delimiters = [
        ("**", TextType.BOLD), 
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
        ]
    
    for delimiter, type in delimiters:
        nodes = split_nodes_delimiter(nodes, delimiter, type)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes 


#def testytest(text):
 #   res = text_to_textnodes(text)
  #  print("Testing now...")
   # for thing in res:
    #    print(thing)

    #print("Done")

#testtext = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#test_node = TextNode(test_text, TextType.TEXT)
#testytest(testtext)


#if __name__ == "__main__":
 #   test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

  #  result = text_to_textnodes(test_text)
   # print("Testing now...")
  #  for node in result:
   #     print(node)
   # print("Done")

