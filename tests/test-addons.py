import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_metallb_addon(self):
        addon = "metallb"
        ip_ranges = (
            "192.168.0.105-192.168.0.105,192.168.0.110-192.168.0.111,192.168.1.240/28"
        )
        print("Enabling metallb")
        microk8s_enable("{}:{}".format(addon, ip_ranges), timeout_insec=500)
        validate_metallb_config(ip_ranges)
        print("Disabling metallb")
        microk8s_disable("metallb")
