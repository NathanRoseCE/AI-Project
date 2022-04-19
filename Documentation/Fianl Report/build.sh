#!/usr/bin/env bash
pdflatex Report && biber Report && pdflatex Report && pdflatex Report
