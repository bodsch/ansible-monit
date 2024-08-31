# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
    """
    def filters(self):
        return {
            'has_valid_values': self.has_values,
            'services': self.monit_services,
            'configured_monitors': self.configured_monitors,
        }

    def has_values(self, var):
        result = False
        result_value = var

        # display.v("var   : {} ({})".format(var, type(var)))

        if isinstance(var, int) and int(var) > 0:
            result = True
        if (isinstance(var, str) or type(var).__name__ == "AnsibleUnsafeText"):
            result_value = '"{}"'.format(str(var))
            if len(var) > 0:
                result = True
        if isinstance(var, list) and len(var) > 0:
            result_value = "{}".format((', ').join(var))
            result = True

        return result, result_value

    def monit_services(self, data, monit_mail = {}, monit_webinterface = {}):
        """
        """
        # display.v(f"monit_services({data}, {monit_mail}, {monit_webinterface})")
        result = []

        result = [x.get("name") for x in data]

        if isinstance(monit_mail, dict):
            if monit_mail.get("enabled", False):
                result.append("mail")

        if isinstance(monit_webinterface, dict):
            if monit_webinterface.get("enabled", False):
                result.append("webinterface")

        display.v(f"= result: {result}")
        return result

    def configured_monitors(self, data, base_directory):
        """
        """
        # display.v(f"configured_monitors({data}, {base_directory})")
        result = []

        if isinstance(data, dict):
            files = data.get("files", [])
            if len(files) > 0:
                """
                    get path variable, this contains the full path
                    split the path and get the last entry from the list
                """
                result = [x.get("path").split("/")[-1:][0] for x in files]

        display.v(f"= result: {result}")
        return result
