pkgname = "firmware-google-sunfish"
pkgver = "20250809"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "Nonfree firmware blobs for Google Pixel 4a"
license = "custom:proprietary"
url = "https://github.com/sm7150-mainline/firmware-google-sunfish"
_commit = "30ad3029cb916e5f44121d23ce604f5ed45c0af4"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "76be98d6ecf1aa752310b4e1d944deceb4bb5120f3ac7e5132c3050ab9db0d51"
options = ["!distlicense", "!strip", "execstack", "foreignelf", "textrels"]


def post_extract(self):
    self.mv("lib", "usr/lib")
    # The files are in usr/share, we want them in usr/lib/firmware/hexagonfs
    self.mv("usr/share", "usr/lib/firmware/hexagonfs")

def install(self):
    for f in self.cwd.rglob("*"):
        if f.is_file():
            self.install_file(f, f.relative_to(self.cwd).parent)
