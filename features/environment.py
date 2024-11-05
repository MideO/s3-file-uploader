import mechanicalsoup


def before_all(context):
    context.base_url = "http://localhost:9000"
    context.browser = mechanicalsoup.StatefulBrowser(
        soup_config={"features": "lxml"},
        raise_on_404=True,
        user_agent="MyBot/0.1: MechanicalSoup",
    )
    context.browser.set_verbose(2)


def after_all(context):
    context.browser.close()
