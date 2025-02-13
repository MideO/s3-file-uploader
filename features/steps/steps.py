from urllib.parse import urljoin

import behave
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed


@behave.when('I visit the path "{path}"')
@retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(2))
def visit_uri(context, path):
    url = urljoin(context.base_url, path)
    context.browser.open(url)


@behave.step('I get the path "{path}"')
@retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_path(context, path):
    url = urljoin(context.base_url, path)
    context.response = httpx.get(url)


@behave.then('I expect the page "{element}" with "{cls}" to contain the text "{text}"')
def check_element_text(context, element, cls, text):
    try:
        node = context.browser.page.find(element, class_=cls)
    except AttributeError as exc:
        raise AssertionError(f"{element} with class {cls} not found on page") from exc
    assert text in node.text


@behave.step('I expect the content to contain the text "{text}"')
def check_response_text(context, text):
    assert (
        text in context.response.text
    ), f"expected {context.response.text} to contain {text}"


@behave.step('I expect the status code to be "{code}"')
def check_response_code(context, code):
    assert context.response.status_code == int(
        code
    ), f"expected {context.response.status_code} to be {code}"


@behave.when('I upload a "{filename}"')
def upload_file(context, filename):
    try:
        context.browser.select_form('form[action="http://localhost:9000/uploads"]')
    except AttributeError as exc:
        raise AssertionError(
            'form[action="http://localhost:9000/uploads"] not found on page'
        ) from exc
    resource_file = f"{context.resources_directory}/{filename}"
    with open(resource_file, "rb") as resource:
        context.browser["file"] = resource
        context.upload_result = context.browser.submit_selected()
