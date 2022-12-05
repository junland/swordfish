MARLIN_DIR := Marlin
PLATFORMIO := pio
PLATFORMIO_MAIN_DIR := $(PWD)/.pio
PLATFORMIO_BUILD_DIR := $(PLATFORMIO_MAIN_DIR)/build
PLATFORMIO_CONF := $(PWD)/platformio-local.ini
PLATFORMIO_PROJECT_DIR := $(PWD)/marlin
PLATFORMIO_ENV := mega2560
PWD := $(shell pwd)
PYTHON := python3
SCRIPTS_DIR := $(shell pwd)/scripts

clean:
	rm -f $(PLATFORMIO_CONF)
	rm -rf $(PLATFORMIO_BUILD_DIR)
	rm -rf $(PLATFORMIO_MAIN_DIR)
.PHONY: clean$

dirs:
	mkdir -p $(PLATFORMIO_BUILD_DIR)
	mkdir -p $(PLATFORMIO_MAIN_DIR)
	mkdir -p $(PLATFORMIO_PROJECT_DIR)
.PHONY: dirs

config:
	cp marlin/platformio.ini $(PLATFORMIO_CONF)
	$(PYTHON) $(SCRIPTS_DIR)/inject-config.py marlin/$(PLATFORMIO_CONF) platformio extra_configs $(PWD)/*.ini -a -n
.PHONY: config

build: dirs
	$(PLATFORMIO) run -d $(PLATFORMIO_PROJECT_DIR) -c $(PLATFORMIO_CONF) -e $(PLATFORMIO_ENV)
.PHONY: build