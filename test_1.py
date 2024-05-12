from testpage import OperationsHelper
import yaml, time
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]
def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"

def test_step3(browser):
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == 'testtitle'




