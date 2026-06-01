#!/usr/bin/env bash

EXNUM=$1
EXPATH=$(find . -type f -name "E$1*.tex")
EXNAME=$(basename $EXPATH)
EXBASE=${EXNAME%.*}

latexmk -latexoption="-shell-escape" -pdflatex=lualatex -auxdir=auxdir -outdir=pdfs -jobname=$EXBASE -pdf src/$EXBASE
