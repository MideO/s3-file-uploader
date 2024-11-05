from urllib.parse import urljoin

import behave
from tenacity import retry, stop_after_attempt, wait_fixed


@behave.when('I visit the path "{path}"')
@retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(2))
def visit_uri(context, path):
    url = urljoin(context.base_url, path)
    context.browser.open(url)


@behave.then('I expect the page "{element}" with "{cls}" to contain the text "{text}"')
def check_element_text(context, element, cls, text):
    node = context.browser.page.find(element, class_=cls)
    assert text in node.text
