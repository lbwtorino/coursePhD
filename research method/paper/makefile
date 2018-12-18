PAPER = paper
LATEX = pdflatex -synctex=1
BIBTEX = bibtex

TEXFILES = $(shell ls *.tex sec/*.tex *.bib)

$(PAPER).pdf: $(TEXFILES)
	$(LATEX) $(PAPER)
	$(BIBTEX) $(PAPER)
	$(LATEX) $(PAPER)
	$(LATEX) $(PAPER)

clean:
	rm -f $(PAPER).ps $(PAPER).pdf $(PAPER).synctex.gz *~ *.dvi *.log *.aux *.blg *.bbl *.toc *.backup *.bak $(PAPER).out
