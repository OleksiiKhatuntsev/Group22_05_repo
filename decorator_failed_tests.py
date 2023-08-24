def decorator_screenshot(func):
    driver = Driver().driver
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="FAILED SCREEN",
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper