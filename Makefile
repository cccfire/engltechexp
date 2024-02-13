TEX=$(wildcard *.tex)
BIB=$(wildcard *.bib)

proceedings.pdf: $(TEX) $(BIB)
	latexmk -pdf -pdflatex='pdflatex -interaction nonstopmode' proceedings.tex

diff:
	latexdiff-git --force --flatten -r 6fdde proceedings.tex
	python3 clean-diff2.py proceedings-diff6fdde.tex
	latexmk -pdf -pdflatex='pdflatex -interaction nonstopmode' proceedings-diff6fdde.tex

clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.log *.out *.vtc *.fdb_latexmk *.fls
	rm -f abstract.txt
