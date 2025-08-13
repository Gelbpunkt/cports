pkgname = "rmtfs"
pkgver = "1.1.1"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_use_env = True
makedepends = ["udev-devel", "qrtr-devel", "linux-headers", "udev-devel"]
pkgdesc = "Qualcomm Remote Filesystem Service Implementation"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/rmtfs"
source = f"https://github.com/linux-msm/rmtfs/archive/v{pkgver}/rmtfs-v{pkgver}.tar.gz"
sha256 = "190b50e97d2bb2cfa2ea20137a91aa5b113351f53f8c05fbb152ab97f31b57f7"
# no tests
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "udev.rules", "usr/lib/udev/rules.d", name="65-rmtfs.rules")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "rmtfs")
    self.uninstall("usr/lib/systemd/system")
