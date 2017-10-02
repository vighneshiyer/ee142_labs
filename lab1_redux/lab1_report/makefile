srcdir  = .

main = lab1_report
figs = $(wildcard figs/*)

pdf : lab1_report.pdf
.PHONY: pdf

%.pdf: lab1_report.tex common.tex $(figs)
	pdflatex -shell-escape lab1_report.tex

clean :
	rm -rf *.pdf *.aux *.out *.log _minted*
