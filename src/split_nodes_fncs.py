from extract_markdown import *
from htmlnode import *
from textnode import *



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