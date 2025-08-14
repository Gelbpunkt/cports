pkgname = "qca-swiss-army-knife"
pkgver = "0_git20250603"
pkgrel = 0
depends = ["python"]
pkgdesc = "Utilities to help and debug Qualcomm Atheros wireless driver development"
license = "ISC"
url = "https://github.com/qca/qca-swiss-army-knife"
_commit = "7c191e5530d32391105653b276ab587d2af9e02a"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "207595e36b325de4db9b8da335b842e4263c029467c8c7fd31ff7e92b1a60fe6"


def install(self):
    self.install_license("LICENSE")

    for f in self.cwd.glob("tools/scripts/**/*"):
        if f.is_file():
            self.install_bin(f)
