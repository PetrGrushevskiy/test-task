from pytest import mark


class TestRegistration:

    @mark.ui
    def test_register_new_user(self, app):
        app.base_page.open_base_page()
        app.base_page.click_on_get_started()
        app.registration.register_new_user()
        app.wizard.skip_wizard()
        app.dashboard.open_personal_settings()
        app.account.update_account()
