#import notify2 as notify2


class LinuxNotification:

    def _set_notification(self, message):
        """Set notification for unix system"""
        print(f"The conversion rate is - ", message)
        # notify2.init('Rate Alert!')
        # n = notify2.Notification(message["source"] + " 1 = " + message["target"] + " " + str(message["rate"]))
        # n.show()

    def set_notification(self, message):
        """Set notification code for unix system"""
        return self._set_notification(message)