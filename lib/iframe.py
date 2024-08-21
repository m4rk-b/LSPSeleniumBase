from seleniumbase import BaseCase

class SwitchIFrame(BaseCase):
    def switch_to_main_frame(self):
        self.switch_to_frame('iframe[name="LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c"]')

    def switch_to_child_frame(self, component):
        self.switch_to_default_window()
        iframe = "mg_frame" + self.get_attribute(component, "id")
        self.switch_to_main_frame()
        self.switch_to_frame(f"//*[@name={iframe}]")