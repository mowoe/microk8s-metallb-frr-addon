import platform
from utils import kubectl


def validate_metallb_config(ip_ranges="192.168.0.105"):
    """
    Validate Metallb
    """
    if platform.machine() != "x86_64":
        print("Metallb tests are only relevant in x86 architectures")
        return
    out = kubectl(
        "get ipaddresspool -n metallb-system default-addresspool -o jsonpath='{.spec.addresses}"
    )
    for ip_range in ip_ranges.split(","):
        assert ip_range in out
