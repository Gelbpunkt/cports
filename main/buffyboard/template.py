pkgname = "buffyboard"
pkgver = "3.2.0"
_lvgl_commit = "ceadda8a468b7d5fa6ba973bd82cf610166278d8"
pkgrel = 0
build_wrksrc = "buffyboard"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["inih-devel", "libinput-devel"]
depends = ["kbd"]
pkgdesc = "Touch-enabled framebuffer keyboard (not only) for vampire slayers"
license = "GPL-2.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/buffybox"
source = [
    f"{url}/-/archive/{pkgver}/buffybox-{pkgver}.tar.gz",
    f"https://github.com/lvgl/lvgl/archive/{_lvgl_commit}.tar.gz",
]
source_paths = [".", "lvgl"]
sha256 = [
    "fd182fd6caf101545daee24de58a9c222bcc18db99543164545174eb436d5d45",
    "03c55df27395cc3b7e352672d71b82df4ad00fe99898740a9db9845c1ea44b57",
]
