from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text</p>
    </div>
    <ol>
    <li class="special>This list item is special.</li>
    <li class="special>This list item is also special.</li>
    <li>This list item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.find_all("li"))
print(soup.find_all(attrs={"data-example": "yes"}))
print(soup.find_all(class_="special")) #due to conflict _ is attached to class

print(soup.select("#first")) #navigating through css selectors

print(soup.body.div)
