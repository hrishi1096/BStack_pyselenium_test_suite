

# Locators for all the pages involved in this test suite
# We are using xpaths for all the locators

class Locators():
    # Locators for main page
    about_us_xpath = '//*[@id="menu-item-25037"]/a/span'

    # Locators for login page
    email_textbox_xpath             = '//*[@id="user_email_login"]'
    password_textbox_xpath          = '//*[@id="user_password"]'
    sign_me_in_button_xpath         = '//*[@id="user_submit"]'
    invalid_username_message_xpath  = '//*[@id="signin_signup_form"]/div[1]/div/div[1]/div[4]/div/div/div/span'

    # Locators for home page (post login)
    account_menu_xpath = '//*[@id="account-menu-toggle"]'
    logout_link_xpath  = '//*[@id="sign_out_link"]'


