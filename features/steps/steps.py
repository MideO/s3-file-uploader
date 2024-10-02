from urllib.parse import urljoin

import behave


@behave.when('I visit the path "{path}"')
def visit_uri(context, path):
    url = urljoin(context.base_url, path)
    context.browser.open(url)


@behave.then('I expect the page {element} with {cls} to contain the text "{text}"')
def check_element_text(context, element, cls, text):
    node = context.browser.page.find(element, class_=cls)
    assert text in node.text
