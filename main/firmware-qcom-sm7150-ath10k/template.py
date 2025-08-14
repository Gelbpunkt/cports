pkgname = "firmware-qcom-sm7150-ath10k"
pkgver = "20250815"
pkgrel = 0
archs = ["aarch64"]
hostmakedepends = ["qca-swiss-army-knife"]
replaces = ["firmware-linux-ath10k"]
pkgdesc = "Linux ath10k board files for Qualcomm SM7150 devices"
license = "custom:proprietary"
url = "https://github.com/sm7150-mainline/firmware-qcom-sm7150-ath10k"
_commit = "792c716c85c06861c4d17bce5ec21fba7f0f7de6"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "8df165e2f4b9d82f3d0c3e2ea7c13489f561b84aabbb6a831275a513f3704e0c"
options = ["!distlicense"]


def build(self):
    self.do("ath10k-bdencoder", "-c", "board-2.json")
    self.do(
        "ath10k-fwencoder",
        "--create",
        "--features=wowlan,no-nwifi-decap-4addr-padding,allows-mesh-bcast,mgmt-tx-by-ref,non-bmi,single-chan-info-per-channel",
        "--set-wmi-op-version=tlv",
        "--set-htt-op-version=tlv",
        "--set-fw-api=5",
    )


def install(self):
    self.install_file("board-2.bin", "usr/lib/firmware/ath10k/WCN3990/hw1.0")
    self.install_file("firmware-5.bin", "usr/lib/firmware/ath10k/WCN3990/hw1.0")
