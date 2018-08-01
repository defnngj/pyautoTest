import time


class WebDriver(object):

    def sleep(self, sec):
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
