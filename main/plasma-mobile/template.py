pkgname = "plasma-mobile"
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
    "kcmutils-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kwayland-devel",
    "kwin-devel",
    "layer-shell-qt-devel",
    "libkscreen-devel",
    "libplasma-devel",
    "modemmanager-qt-devel",
    "networkmanager-qt-devel",
    "plasma-activities-devel",
    "plasma-workspace-devel",
    "qcoro-devel",
    "qt6-qtbase-private-devel",  # qtguiglobal_p.h
    "qt6-qtsensors-devel",
    "qt6-qtwayland-devel",
]
depends = [
    "bluez-qt",
    "breeze",
    "kactivitymanagerd",
    "kirigami",
    "kirigami-addons",
    "kscreen",
    "milou", # search
    "plasma-integration",
    "plasma-nano",
    "plasma-nm",
    "plasma-pa",
    "plasma-workspace",
    "qqc2-breeze-style",
]
pkgdesc = "Modules providing phone functionality for Plasma"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://plasma-mobile.org"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-mobile-{pkgver}.tar.xz"
sha256 = "067c5def164ea8c534a910fb57b4dd69b1c83a6877975efebe1b7b274045f497"
hardening = ["vis"]
