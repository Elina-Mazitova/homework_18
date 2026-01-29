from selene import browser


def set_cookie(name, value):
    browser.open("/")
    browser.driver.add_cookie({"name": name, "value": value})
