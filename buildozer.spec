[app]

title = 虚拟主播立绘AI防护系统

package.name = vtuber_ai_protection

package.domain = org.vtuber

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0.0

requirements = python3,kivy,pillow,plyer

icon.filename = %(source.dir)s/icon.png

orientation = all

fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA

android.api = 33

android.minapi = 21

android.ndk = 25b

android.skip_update = False

android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

log_level = 2

warn_on_root = 1
