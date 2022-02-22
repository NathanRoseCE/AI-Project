#!/usr/bin/env bash
pdflatex main && biber main && pdflatex main && pdflatex main
