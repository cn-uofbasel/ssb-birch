# Makefile

all:
	protoc --python_out=. -I ../.. ssb-birch.proto
	./test.py

clean:
	rm -rf ssb_birch_pb2.py __pycache__ *~

# eof
