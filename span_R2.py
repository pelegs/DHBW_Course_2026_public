import argparse
from pathlib import Path
from string import Template
from subprocess import run

import sympy as sym


# Changing the delimeter for substitution to "#"
# (otherwise LaTeX issues)
class LatexTemplate(Template):
    delimiter = "#"


# Parsing commandline arguments
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-i",
    "--input-filename",
    default="R2_span_template",
    help="Name of the LaTeX template file",
)
parser.add_argument(
    "-o",
    "--output-filename",
    default="R2_span_solution",
    help="Name of the output file",
)
parser.add_argument(
    "-r",
    "--remove-redundant",
    action="store_true",
    help="Remove redundant files (artifacts of pdflatex)",
)
parser.add_argument(
    "-x",
    "--redundant-exclude",
    nargs="*",
    default=".pdf",
    help="List of extension to exclude from redundant files removal",
)
args = parser.parse_args()

# Base variables
alpha, beta = sym.symbols(r"\alpha \beta")
a_x, a_y = sym.symbols(r"a_{x} a_{y}")
b_x, b_y = sym.symbols(r"b_{x} b_{y}")
x, y = sym.symbols("x y")

# Base equations
eq_x = sym.Eq(alpha * a_x + beta * b_x, x)
eq_y = sym.Eq(alpha * a_y + beta * b_y, y)

# Solution
solution = sym.solve([eq_x, eq_y], [alpha, beta])
alpha_sol, beta_sol = solution.values()

# Formating equations for latex align env
format_dict = {
    "alphaSol": rf"{alpha} &= {sym.latex(alpha_sol)}",
    "betaSol": rf"{beta} &= {sym.latex(beta_sol)}",
}

# Get LaTeX template
with open(f"{args.input_filename}.tex", "r") as file:
    latex_template = LatexTemplate(file.read())

# Populate template
populated_template = latex_template.substitute(format_dict)

# Save .tex file
with open(f"{args.output_filename}.tex", "w") as file:
    file.write(populated_template)

# Compile LaTeX file
run(f"pdflatex {args.output_filename}", shell=True)

# Remove redundant files
if args.remove_redundant:
    files_to_remove = [
        p
        for p in Path.cwd().glob(f"{args.output_filename}.*")
        if p.suffix not in args.redundant_exclude
    ]
    for file in files_to_remove:
        file.unlink()
