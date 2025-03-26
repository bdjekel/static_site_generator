import unittest

from markdown_to_html_node import markdown_to_html_node


#TODO: confirm this actually contains all cases. Add as you find edges.
markdown_all_cases = """
# Code block below

```go
type User struct {
    name: Jimbo
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
the **same** even with inline stuff
```
"""

html_all_cases = """
<div>
<h1>Code block below</h1>
<code>go
type User struct {
name: Jimbo
password: craigLeg
}
</code><h2>quote below</h2><blockquote>"29 Kids go into the water, **22 Kids** come out of the water. The Ice _Cream Man,_ He gets the rest. April the 9th, Half past four P.M."</blockquote><h3>unordered list below</h3><ul><li>- Quoted Actor: Dana Carvey</li><li>- Quoted Movie: Master of Disguise</li><li>- IMDb Rating: <code>3.4 / 10</code></li><li>- Metascore: 12 / 100</li><li>- My Rating: 7 / 10</li></ul><h4>#### ordered list below</h4><ol><li>1. watch better movies</li><li>2. like those better <a href=https://fake.link.io>movies</a></li><li>3. stop quoting <s>thinking about</s> impressively bad movies</li><li>4. get friends <img src=https://fake.picture.io/fakepic.jpg alt=fake pic></li></ol><h5>##### paragraph below</h5><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p></div>
"""

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_all_cases(self):
        self.assertEqual(html_all_cases, markdown_to_html_node(markdown_all_cases))

    def test_no_tag(self):
        node_props = {"class": "tester", "style":"color:red;"}
        node = HTMLNode(value="Testing, testing, 1, 2, 3", children=["<p></p>","<a><a/>"], props=node_props)
        self.assertIsNone(node.tag)

    def test_no_props(self):
        node = HTMLNode("h1", "Testing, testing, 1, 2, 3", ["<p></p>","<a><a/>"])
        self.assertIsNone(node.props)
    

if __name__ == "__main__":
    unittest.main()

