(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("biblatex" "backend=biber" "style=ieee")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "biblatex"
    "hyperref")
   (LaTeX-add-bibliographies
    "resources"))
 :latex)

