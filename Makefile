.PHONY: build
build:
	mkdir -p build && \
	cd build && \
	cmake -DCMAKE_INSTALL_PREFIX=../install .. && \
	make all && \
	make install

.PHONY: names
names:
	nm -D --defined-only build/libconvert.so