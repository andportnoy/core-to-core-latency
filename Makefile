CFLAGS += -Wall -Wextra
CFLAGS += -std=c11 -pedantic
CFLAGS += -D_GNU_SOURCE
CFLAGS += -O3
CFLAGS += -flto

SMT = 1

all: core-to-core-latency.png

core-to-core-latency.png: core-to-core-latency.csv core-to-core-venv heatmap-plot.py
	. core-to-core-venv/bin/activate \
		&& python heatmap-plot.py $< $(SMT) $@

core-to-core-venv:
	python -m venv $@ \
		&& . $@/bin/activate \
		&& pip install matplotlib numpy pandas

core-to-core-latency.csv: measure
	./$< > $@

clean:
	rm -rf measure *.o *.csv *.png core-to-core-venv
