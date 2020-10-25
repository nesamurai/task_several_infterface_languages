link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_btn_for_provided_language(browser):
	browser.implicitly_wait(5)
	browser.get(link)
	
	assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary").text != '', "The button is not found"