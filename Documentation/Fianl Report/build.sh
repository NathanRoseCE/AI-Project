#!/usr/bin/env bash
pdflatex -shell-escape Report && biber Report && pdflatex -shell-escape Report && pdflatex -shell-escape Report
