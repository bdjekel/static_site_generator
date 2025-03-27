import unittest
from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node


#TODO: write more tests
#TODO: add type hinting to entire file

# Test Inputs --------------------------------------------

markdown_code_block = """```go
type User struct {
    name: Jimbo,
    password: craigLeg
}
```"""

markdown_heading1 = "# Code block below"

markdown_heading2 = "## quote below"

markdown_heading3 = "### unordered list below"

markdown_heading4 = "#### ordered list below"

markdown_heading5 = "##### paragraph below"

markdown_heading6 = "###### heading6"

markdown_blockquote = "> \"29 Kids go into the water, **22 Kids** come out of the water. The Ice _Cream Man,_ He gets the rest. April the 9th, Half past four P.M.\""

markdown_unordered_list = """
- Quoted Actor: Dana Carvey
- Quoted Movie: Master of Disguise
- IMDb Rating: `3.4 / 10`
- Metascore: 12 / 100
- My Rating: 7 / 10
"""

markdown_ordered_list = """
1. watch better movies
2. like those better [movies](https://fake.link.io)
3. stop quoting ~~thinking about~~ impressively bad movies
4. get friends ![fake pic](https://fake.picture.io/fakepic.jpg)
"""

markdown_paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#TODO: confirm this actually contains all cases. Add as you find edges.
markdown_all_cases = """
# Code block below

```go
type User struct {
    name: Jimbo,
    password: craigLeg
}
```

## quote below

> "29 Kids go into the water, **22 Kids** come out of the water. The Ice _Cream Man,_ He gets the rest. April the 9th, Half past four P.M."

### unordered list below

- Quoted Actor: Dana Carvey
- Quoted Movie: Master of Disguise
- IMDb Rating: `3.4 / 10`
- Metascore: 12 / 100
- My Rating: 7 / 10

#### ordered list below

1. watch better movies
2. like those better [movies](https://fake.link.io)
3. stop quoting ~~thinking about~~ impressively bad movies
4. get friends ![fake pic](https://fake.picture.io/fakepic.jpg)

##### paragraph below

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

"""

markdown_code_block_ignore_inlines = """
```
This is text that _should_ remain
**unemphasizes** even with inline stuff
```
"""

# Expected Results --------------------------------------------
html_code_block = """<div><code>go
type User struct {
name: Jimbo,
password: craigLeg
}</code></div>"""


html_heading1 = "<div><h1>Code block below</h1></div>"

html_heading2 = "<div><h2>quote below</h2></div>"

html_heading3 = "<div><h3>unordered list below</h3></div>"

html_heading4 = "<div><h4>ordered list below</h4></div>"

html_heading5 = "<div><h5>paragraph below</h5></div>"

html_heading6 = "<div><h6>heading6</h6></div>"

html_blockquote = "<div><blockquote>\"29 Kids go into the water, **22 Kids** come out of the water. The Ice _Cream Man,_ He gets the rest. April the 9th, Half past four P.M.\"</blockquote></div>"

html_unordered_list = "<div><ul><li>- Quoted Actor: Dana Carvey</li><li>- Quoted Movie: Master of Disguise</li><li>- IMDb Rating: <code>3.4 / 10</code></li><li>- Metascore: 12 / 100</li><li>- My Rating: 7 / 10</li></ul></div>"

html_ordered_list = "<div><ol><li>1. watch better movies</li><li>2. like those better <a href=https://fake.link.io>movies</a></li><li>3. stop quoting <s>thinking about</s> impressively bad movies</li><li>4. get friends <img src=https://fake.picture.io/fakepic.jpg alt=fake pic></li></ol></div>"

html_paragraph = "<div><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p></div>"

html_all_cases = """<div><h1>Code block below</h1><code>go
type User struct {
name: Jimbo,
password: craigLeg
}</code><h2>quote below</h2><blockquote>"29 Kids go into the water, **22 Kids** come out of the water. The Ice _Cream Man,_ He gets the rest. April the 9th, Half past four P.M."</blockquote><h3>unordered list below</h3><ul><li>- Quoted Actor: Dana Carvey</li><li>- Quoted Movie: Master of Disguise</li><li>- IMDb Rating: <code>3.4 / 10</code></li><li>- Metascore: 12 / 100</li><li>- My Rating: 7 / 10</li></ul><h4>ordered list below</h4><ol><li>1. watch better movies</li><li>2. like those better <a href=https://fake.link.io>movies</a></li><li>3. stop quoting <s>thinking about</s> impressively bad movies</li><li>4. get friends <img src=https://fake.picture.io/fakepic.jpg alt=fake pic></li></ol><h5>paragraph below</h5><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p></div>"""

class TestMarkdownToHTMLNode(unittest.TestCase):

# Standard Functionality Tests ---------------------------------------------------------------------    

    def test_paragraph(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_paragraph)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_paragraph, actual_html)

    def test_heading1(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading1)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading1, actual_html)
    
    def test_heading2(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading2)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading2, actual_html)
            
    def test_heading3(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading3)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading3, actual_html)
            
    def test_heading4(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading4)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading4, actual_html)
            
    def test_heading5(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading5)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading5, actual_html)
            
    def test_heading6(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_heading6)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_heading6, actual_html)

    def test_code_block(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_code_block)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_code_block, actual_html)

    def test_blockquote(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_blockquote)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_blockquote, actual_html)

    def test_unordered_list(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_unordered_list)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_unordered_list, actual_html)
    
    def test_ordered_list(self):
        actual_nodes: list[HTMLNode] = markdown_to_html_node(markdown_ordered_list)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_ordered_list, actual_html)

    def test_all_cases(self):
        self.maxDiff = None
        actual_nodes = markdown_to_html_node(markdown_all_cases)
        actual_html = actual_nodes.to_html()
        self.assertEqual(html_all_cases, actual_html)

# Edge Case Tests ---------------------------------------------------------------------    

    def test_no_tag(self):
        node_props = {"class": "tester", "style":"color:red;"}
        node = HTMLNode(value="Testing, testing, 1, 2, 3", children=["<p></p>","<a><a/>"], props=node_props)
        self.assertIsNone(node.tag)

    def test_no_props(self):
        node = HTMLNode("h1", "Testing, testing, 1, 2, 3", ["<p></p>","<a><a/>"])
        self.assertIsNone(node.props)

    def test_empty_string(self):
        self.assertEqual(markdown_to_html_node("").to_html(),"<div></div>")

    #TODO: test edge cases like poor/incorrect formatting of markdown
    

if __name__ == "__main__":
    unittest.main()

