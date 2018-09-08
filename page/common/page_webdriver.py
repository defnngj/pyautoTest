import time


class WebDriver(object):

    def wait(self, sec):
        """
        sleep
        :param sec: second
        :return:
        """
        time.sleep(sec)

    def get_title(self):
        """
        Get window title.
        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_alert_text(self):
        """
        Gets the text of the Alert.
        Usage:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        """
        Accept warning box.
        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()
