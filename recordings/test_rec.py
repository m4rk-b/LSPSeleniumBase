from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_infor_signin(self):
        self.open("https://mingle-cqa-portal.cqa.inforcloudsuite.com/v2/LCLQA_AX1/59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.switch_to_frame('iframe[name="LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c"]')
        self.open("https://saasap-lclsp.ssmgf.dev.inforcloudsuite.com/WSWebClient//default.aspx?tenant=LCLQA_AX1&HybridCertified=1&OnPremCertified=1&portalV2Certified=1&forcesso=1&Form=LCSXCHomePage&configgroup=LCLQA_LCLSP_AX1&stype=full&page=FormOnly&config=LCLQA_LCLSP_AX1_DEFAULT&LogicalId=lid://infor.lcl-lsp.lclsp&inforThemeName=Light&inforThemeColor=amethyst&inforCurrentLocale=en-US&inforCurrentLanguage=en-US&infor10WorkspaceShell=1&inforWorkspaceVersion=2024.09.00&inforOSPortalVersion=2024.09.00&inforTimeZone=(UTC+08:00) Kuala Lumpur&inforStdTimeZone=Asia/Manila&inforStartMode=0&inforTenantId=LCLQA_AX1&inforSessionId=LCLQA_AX1~057b440d-1600-4921-8b2f-212be0100724")
        self.open("https://saasap-lclsp.ssmgf.dev.inforcloudsuite.com/WSWebClient/PlainForm.aspx?Form=LCSXCHomePage&HybridCertified=1&LogicalId=lid://infor.lcl-lsp.lclsp&OnPremCertified=1&config=LCLQA_LCLSP_AX1_DEFAULT&configgroup=LCLQA_LCLSP_AX1&forcesso=1&infor10WorkspaceShell=1&inforCurrentLanguage=en-US&inforCurrentLocale=en-US&inforOSPortalVersion=2024.09.00&inforSessionId=LCLQA_AX1~057b440d-1600-4921-8b2f-212be0100724&inforStartMode=0&inforStdTimeZone=Asia/Manila&inforTenantId=LCLQA_AX1&inforThemeColor=amethyst&inforThemeName=Light&inforTimeZone=(UTC+08:00) Kuala Lumpur&inforWorkspaceVersion=2024.09.00&page=FormOnly&portalV2Certified=1&stype=full&tenant=LCLQA_AX1")
