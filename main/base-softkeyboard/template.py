pkgname = "base-softkeyboard"
pkgver = "1"
pkgrel = 0
depends = ["buffyboard", "ttyescape", "networkmanager"]
pkgdesc = "Chimera base package for devices without physical keyboards"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(self.files_path / "USB_Networking.nmconnection", "usr/lib/NetworkManager/system-connections")
