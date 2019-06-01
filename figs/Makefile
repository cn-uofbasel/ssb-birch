# figs/Makefile

all: birch_log_entry.pdf

birch_log_entry.pdf: Makefile birch_log_entry.dot
	dot -Teps birch_log_entry.dot >birch_log_entry.eps
	epstopdf birch_log_entry.eps
	rm -f birch_log_entry.eps
	dot -Tpng birch_log_entry.dot >birch_log_entry.png

# eof
