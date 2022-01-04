# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
from configparser import RawConfigParser


# -- Project information -----------------------------------------------------

project = 'MIS developer doc'
copyright = '2021, YOEM Rattana'
author = 'YOEM Rattana'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'djangodocs',
    #'doc_extensions',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'notfound.extension',
    'hoverxref.extension',
    'sphinx_search.extension',
    'sphinxemoji.sphinxemoji',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

root_doc = 'index'

latex_elements = {
  'extraclassoptions': 'openany,oneside',
  # 'preamble': r'''
  #   \setmainfont[Script=Khmer,Scale=0.95]{Khmer OS Battambang} 
  # ''',

  'preamble': r'''
    \usepackage[sumlimits]{amsmath}  
    \usepackage{amssymb,amsthm} 
    \usepackage{xltxtra}  
    \usepackage{titlesec} 
    \usepackage{titletoc} 
    \usepackage{hyperref} 
    \usepackage[title,page,titletoc]{appendix} 

    
    \usepackage[x11names,svgnames,dvipsnames]{xcolor}
    \everymath{\displaystyle}
    \usepackage[cal=boondoxo]{mathalfa} % mathcal
    \usepackage{mathtools}
    \usepackage{amsfonts}
    \usepackage{amsthm}
    \usepackage{palatino}
    \usepackage{mathpazo}
    \usepackage{tikz}%for draw
    \usepackage{wrapfig}
    \usepackage{pdfpages}
    \usetikzlibrary{mindmap} % LATEX and plain TEX
    \usepgflibrary{decorations.text} % LATEX and plain TEX and pure pgf 
    \usepgflibrary[decorations.text] % ConTEXt and pure pgf 
    \usetikzlibrary{decorations.text} % LATEX and plain TEX when using TikZ 
    \usetikzlibrary[decorations.text] % ConTEXt when using TikZ
    \usetikzlibrary{automata} % LATEX and plain TEX
    \usetikzlibrary[automata] % ConTEXt
    \usepackage{fontspec}
    %\usepackage{minted}
    %===============================
    \defaultfontfeatures{Script=khmr,Mapping=tex-text} % to support TeX conventions like ``---'' 
    \newfontscript{Khmer}{khmr} 
    \usepackage{xunicode}  
    \newcommand{\KhOS}{\fontspec[Script=Khmer,Scale=0.92]{Khmer OS}\selectfont} 
    \newcommand{\KhOSML}{\fontspec[Script=Khmer]{Khmer OS Muol Light} \selectfont} 
    %\newcommand{\KhMEF}{\fontspec[Script=Khmer]{Khmer MEF2} \selectfont} 

    \setmainfont[Script=Khmer,Scale=0.95]{Khmer OS Battambang} 
    %%%%%%% This macro is to produce khmer numbering by adopting the thai numbering method
    \makeatletter  
    \def\@khmernum#1{\expandafter\@@khmernum\number#1\@nil}  
    \def\@@khmernum#1{%  
      \ifx#1\@nil  
      \else  
      \char\numexpr#1+"17E0\relax  
      \expandafter\@@khmernum\fi  
    }  
    %\def\khmercounter#1{\expandafter\@khmernum\csname c@#1\endcsname}  
    \renewcommand\@arabic{\@khmernum} % to reset number in \arabic to \khmernum  
    \makeatother  

    \theoremstyle{plain}  
    \newtheorem{theorem}{\KhOSML ទ្រឹស្ដីបទ}[chapter]   
    \newtheorem{proposition}{\KhOSML សំណើ}[theorem]  
    \newtheorem{corollary}{\KhOSML កូរ៉ូលែរ}[theorem] 

    \theoremstyle{definition} 
    \newtheorem{definition}{\KhOSML និយមន័យ}[chapter]%
    \newtheorem{lemma}{\KhOSML ឡែម}[definition]%

    \theoremstyle{remark} 
    \newtheorem{remark}{\KhOSML សម្គាល់}%[theorem] 
    \newtheorem{example}{\KhOSML  ឧទាហរណ៍}[chapter] 
    \newtheorem{exercise}{\KhOSML លំហាត់}[chapter] 
    \renewcommand{\figurename}{\KhOSML  រូប} 
    \renewcommand{\proofname}{\KhOSML សម្រាយបញ្ជាក់} 

    \renewcommand{\contentsname}{មាតិកា} 
    \renewcommand{\indexname}{លិបិក្រម} 
    \renewcommand{\chaptername}{ជំពូកទី} 
    \renewcommand{\partname}{ផ្នែកទី} 
    \renewcommand{\appendixname}{ជំពូកបន្ថែម} 
    \renewcommand{\listfigurename}{បញ្ជីរូបភាព} 
    \renewcommand{\listtablename}{បញ្ជីតារាង} 
    \renewcommand{\appendixpagename}{\KhOSML ជំពូកបន្ថែម} 

    %%%% to format part, chapter, section, subsection and subsubsection using titlesec package

    \titleformat{\section}[block] 
    {\large \KhOSML}{{\large\thesection}}{1em}{}

    \titleformat{\subsection}[block] 
    {\normalsize \KhOSML}{{\normalsize\thesubsection}}{1em}{}

    \titleformat{\subsubsection}[block] 
    {\normalsize\KhOSML }{{\normalsize\thesubsubsection}}{1em}{}

    \titleformat{\chapter}[display] 
        {\Huge\KhOSML }{\filright\LARGE\normalfont\chaptername\ \thechapter}{2ex}         %sep
        {\filcenter} 

    \titleformat{\part}[display] 
    {\filcenter\LARGE\KhOSML}{{\large\partname\; \thepart}}{1em}{\thispagestyle{empty}}

    \makeatletter 
    %%% to set khmer calendar 
    \renewcommand\today{\@khmernum\day\space-\space\ifcase\month\or 
      មករា\or កុម្ភៈ\or មិនា\or មេសា\or ឧសភា\or មិថុនា\or
      កក្កដា\or សីហា\or កញ្ញា\or តុលា\or វិច្ឆិកា\or ធ្នូ\fi
    \space-\space\@khmernum\year} 
    \makeatother 
    %%%%%%%%%%


    \title{\KhOSML Machine Learning} 
    \author{ ថុល​ ចាន់ថន}
    \date{\today}

    \XeTeXlinebreaklocale "khm" % allow line breaks 
    \XeTeXlinebreakskip = 0pt plus 1pt minus 1pt % for line breakskip suitable for Khmer Unicode fonts 

  ''',
}

latex_engine = 'xelatex'