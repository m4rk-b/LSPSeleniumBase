class SwitchIFrame:
    def __init__(self, test_case):
        self.test_case = test_case

    def switch_to_main_frame(self):
        self.test_case.switch_to_default_window()
        self.test_case.switch_to_frame('iframe[name="LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c"]')

    def switch_to_child_frame(self, component):
        self.test_case.switch_to_default_window()
        self.switch_to_main_frame()
        iframe = "mg_frame" + self.test_case.get_attribute(component, "id")
        self.test_case.switch_to_frame(f"//*[@name='{iframe}']")

    def wait_until_page_loads(self):
        # busy_overlay = self.test_case.find_elements("//div[@class='mg-busy mg-busy-wait' and @style = 'display: block;']")
        self.test_case.wait_for_element_not_visible("//div[@class='mg-busy mg-busy-wait' and @style = 'display: block;']", timeout=2000)

