pkgname = "plasma-nano"
pkgver = "6.3.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kitemmodels-devel",
    "kpackage-devel",
    "kservice-devel",
    "kwayland-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Minimal plasma shell package intended for embedded devices"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://invent.kde.org/plasma/plasma-nano"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-nano-{pkgver}.tar.xz"
sha256 = "fea36cc88172c8699f6c643cdae9a01f92408a76942a23eb56577dcf0fc38d5f"
hardening = ["vis"]
