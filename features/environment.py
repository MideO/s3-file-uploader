import mechanicalsoup

from s3fileuploader.config import app_config


def before_all(context):
    context.base_url = app_config.app.url
    context.browser = mechanicalsoup.StatefulBrowser(
        soup_config={"features": "lxml"},
        raise_on_404=True,
        user_agent="MyBot/0.1: MechanicalSoup",
    )
    context.browser.set_verbose(2)


def after_all(context):
    context.browser.close()
