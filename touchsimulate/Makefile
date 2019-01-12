ARCHS = arm64 armv7
export TARGET = iphone:clang:11.2:8.0

include $(THEOS)/makefiles/common.mk

TWEAK_NAME = touchsimulate
touchsimulate_FILES = Tweak.xm
touchsimulate_LDFLAGS = -lstouchHelper

include $(THEOS_MAKE_PATH)/tweak.mk

after-install::
	install.exec "killall -9 SpringBoard"
