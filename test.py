from seleniumbase import BaseCase
from utils import SwitchIFrame
BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def setUp(self):
        super().setUp()

    def test_infor_signin(self):
        self.maximize_window()
        self.open("https://mingle-cqa-portal.cqa.inforcloudsuite.com/v2/LCLQA_AX1/59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.type("#username", "markgil.bejasa@infor.com")
        self.type("#pass", "H1rapnaman!")
        self.click('//button[@title="Sign In"]')

        # Initialize iframe helper here
        self.utils = SwitchIFrame(self)

        #Parent iFrame
        self.utils.switch_to_main_frame()

        # self.utils.wait_until_page_loads()

        #Settings
        #Wait for element to be visible (for improvement)
        self.wait_for_element_visible('//div[@data-mgcompname="AEDroplist"]', timeout=10000)
        ae_combo_id = self.get_attribute('//div[@data-mgcompname="AEDroplist"]',"id")

        #Choosing an AE to test
        #Wait for element to be visible (for improvement)
        self.wait_for_element_clickable("//div[@id='" + ae_combo_id + "-trigger-picker']")
        self.click("//div[@id='" + ae_combo_id + "-trigger-picker']")
        self.click('td:contains("AR_M3")')

        #Switching to navbar iFrame
        self.utils.switch_to_child_frame('//div[@data-mgcompname = "AccordionUserControl"]')
        #Clicking the Settings in the navbar
        self.click('a:contains("Settings")')

        #Switching to settings card iFrame
        self.utils.switch_to_child_frame('//div[@data-mgcompname = "SubscriptionListUserControl"]')

        #Wait for element to be visible (for improvement)
        self.wait_for_element_visible('//div[@class="subCardSettings"]//div[@class="card"]')
        #Getting all settings cards
        cards = self.find_elements('//div[@class="subCardSettings"]//div[@class="card"]')
        #Loop to all available settings cards
        for card in cards:
            card.click()
            self.utils.switch_to_main_frame()
            self.click('//div[@aria-label="Close Window"]')
            self.utils.switch_to_child_frame('//div[@data-mgcompname = "SubscriptionListUserControl"]')

        # self.click('//div[@itemtype="LCSXCAddendaMaintenance"]')
        # self.switch_to_parent_frame()
        # self.click('//div[@data-mgcompname="AddButton"]')
        
        # active_inputs = self.find_elements("//input")

        # self.send_keys('//input[@data-mgcompnamevalue="CustomerIDEdit"]', 'test')

        #Accounting Entity
        # self.click('a:contains("Administration")')
        # self.click('a:contains("Accounting Entity Maintenance")')
        # self.switch_to_parent_frame()
        # self.switch_to_frame('iframe[id="ext-element-21"]', timeout=1000)
        # self.click('//button[@id="add-btn"]')
        # self.switch_to_parent_frame()

        