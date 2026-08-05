# conf.py for Sphinx + LaTeX + PDF

import os
import sys
from docutils import nodes

# -- Project information -----------------------------------------------------

project = 'JAKA MiniCab Lite硬件用户手册'
copyright = ' 2026, JAKA Robotics'
author = 'JAKA'
release = 'V01'

# -- Substitution ------------------------------------------------------------

rst_epilog = """
.. |product_name| replace:: MiniCab Lite
.. |company_name| replace:: JAKA
.. |软件| replace:: Cobo π
"""

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
master_doc = 'index'

# 自动编号
numfig = True
numfig_secnum_depth = 1

# -- HTML -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/Logo.png'
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

html_css_files = [
    'custom.css',
]

numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码块 %s',
    'section': '节 %s'
}

# 中文搜索
html_search_language = 'zh'
html_search_options = {
    'type': 'jieba',
    'lang': 'zh_CN'
}

# 查找图片偏好
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/png', 'image/jpeg']

# -- LaTeX -------------------------------------------------

latex_engine = 'xelatex'

latex_documents = [
    ('index', 'JAKA MiniCab Lite硬件用户手册.tex', 'JAKA MiniCab Lite硬件用户手册', author, 'manual'),
]

# standard 样式会生成全部横线和竖线；longtable 仍由 list-table 的
# :class: longtable 按需启用。booktabs 会主动省略竖线，不能满足全框线要求。
latex_table_style = ['standard']

latex_elements = {

    'papersize': 'a4paper',
    'pointsize': '11pt',

    'figure_align': 'H',

    'maketitle': r'\input{cover.tex}',
    
    # 恢复原状，去除会导致??的锚点
    'atendofbody': r'''
    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{图目录}
    \begingroup
    \hypersetup{allcolors=black}
    \listoffigures
    \endgroup

    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{表目录}
    \begingroup
    \hypersetup{allcolors=black}
    \listoftables
    \endgroup

    \cleardoublepage
    \input{backcover.tex}
    ''',

    'fncychap': r'\usepackage[Sonny]{fncychap}',

    'extraclassoptions': 'openany,oneside',

    'preamble': r'''

\usepackage{longtable}
\usepackage{booktabs}    

% ===== 中文支持 =====
\usepackage{xeCJK}
\usepackage[fontset=none]{ctex}

% ===== PDF 正文字体 =====

% 英文字体：
% Windows 本地使用 Arial；
% Read the Docs/Linux 使用 Liberation Sans。
\IfFontExistsTF{Arial}{
    \setmainfont{Arial}[
        UprightFont = Arial,
        BoldFont = Arial Bold,
        ItalicFont = Arial Italic,
        BoldItalicFont = Arial Bold Italic
    ]
}{
    \setmainfont{Liberation Sans}[
        UprightFont = Liberation Sans,
        BoldFont = Liberation Sans Bold,
        ItalicFont = Liberation Sans Italic,
        BoldItalicFont = Liberation Sans Bold Italic
    ]
}

% 中文字体：
% 本地存在思源宋体文件时直接加载；
% Read the Docs 使用系统安装的 Noto Serif CJK SC。
\IfFileExists{C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/SourceHanSerifCN-Regular.ttf}{
    \setCJKmainfont{SourceHanSerifCN}[
        Path = C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/,
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf,
        ItalicFont = *-Regular.ttf,
        BoldItalicFont = *-Bold.ttf,
        ItalicFeatures = {FakeSlant=0.2},
        BoldItalicFeatures = {FakeSlant=0.2}
    ]
}{
    \setCJKmainfont{Noto Serif CJK SC}[
        UprightFont = Noto Serif CJK SC,
        BoldFont = Noto Serif CJK SC Bold,
        AutoFakeSlant = 0.2
    ]
}

% Arial/Liberation Sans 可能不包含这两个组合字符。
\XeTeXcharclass"2103=1 % ℃
\XeTeXcharclass"2109=1 % ℉

% ===== 页面边距与页眉空间分配 =====
\usepackage{geometry}
\geometry{
    left=25mm,
    right=25mm,
    top=30mm,
    bottom=25mm,
    headheight=25pt, % 留足页眉高度
    headsep=8mm      % 页眉与正文的距离
}

% ===== 图片路径 =====
\graphicspath{{images/}}

% ===== 禁止图表浮动 =====
\usepackage{float}
\usepackage{placeins}

\makeatletter
\def\fps@figure{H}
\def\fps@table{H}
\def\fps@sphinxfigure{H}
\def\fps@sphinxTable{H}
\makeatother

% ==== 强制图片后换行 ===
\usepackage{etoolbox}
\AtEndEnvironment{figure}{\par\noindent}
\AtEndEnvironment{sphinxfigure}{\par\noindent}

% ===== 代码高亮 =====
\usepackage{listings}

% ===== PDF书签 =====
\usepackage{bookmark}

% ===== 自定义变量 =====
\newcommand{\docversion}{''' + release + r'''}
\newcommand{\docname}{''' + project + r'''}

% ===== 页眉页脚 (恢复 LastPage 避免??) =====
\usepackage{fancyhdr}
\usepackage{lastpage} 

% 1. 重定义 Sphinx 的正文页样式 (normal)
\fancypagestyle{normal}{
    \fancyhf{}  
    \fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}}  
    \fancyfoot[L]{版本： \docversion}
    % 使用最稳定的 LastPage
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt} 
    \renewcommand{\footrulewidth}{0.4pt}
}

% 2. 重定义 Sphinx 的章节起始页样式 (plain)
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}} 
    \fancyfoot[L]{版本： \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}   
    \renewcommand{\footrulewidth}{0.4pt}
}

% ===== 标题样式 =====
\usepackage{titlesec}
\usepackage{xcolor}

% 定义红色
\definecolor{TitleRed}{HTML}{D80C1E}

% 章节间距
\titlespacing*{\chapter}{0pt}{-30pt}{20pt}

% Chapter
\titleformat{\chapter}
{\Huge\bfseries\color{TitleRed}}
{\thechapter}{0.5em}{}

% Section
\titleformat{\section}
{\Large\bfseries\color{TitleRed}}
{\thesection}{0.5em}{}

% Subsection
\titleformat{\subsection}
{\large\bfseries\color{TitleRed}}
{\thesubsection}{0.5em}{}

% Subsubsection
\titleformat{\subsubsection}
{\normalsize\bfseries\color{TitleRed}}
{\thesubsubsection}{0.5em}{}

% ===== 超链接颜色 =====
\usepackage{hyperref}

\hypersetup{
colorlinks=true,
linkcolor=blue,
urlcolor=blue,
citecolor=blue
}

% ===== 所有目录页变黑，正文恢复蓝色 (强力黑盒覆盖版) =====

% 1. 主目录
\let\origsphinxtableofcontents\sphinxtableofcontents
\renewcommand{\sphinxtableofcontents}{
    \begingroup
    \cleardoublepage
    \pagenumbering{Roman}
    \pagestyle{plain} 
    \hypersetup{linkcolor=black}
    \origsphinxtableofcontents
    \clearpage
    \endgroup
    \pagenumbering{arabic}
    \pagestyle{normal}
}

% 2. 图目录
\let\origlistoffigures\listoffigures
\renewcommand{\listoffigures}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoffigures
    \endgroup
}

% 3. 表目录
\let\origlistoftables\listoftables
\renewcommand{\listoftables}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoftables
    \endgroup
}

% ===== 表格样式 =====
\usepackage{colortbl}
\usepackage{longtable}

% 表头 #D80C1E；边框 #9E9E9E、0.75 pt。
\definecolor{tableheader}{HTML}{D80C1E}
\definecolor{tableborder}{HTML}{9e9e9e}
\setlength{\arrayrulewidth}{0.75pt}
\arrayrulecolor{tableborder}

% Sphinx 会在每个表头单元格开头调用此命令。使用 cellcolor 比在
% varwidth 内调用 rowcolor 稳定，并且兼容 tabulary 与 longtable。
\renewcommand{\sphinxstyletheadfamily}{%
  \cellcolor{tableheader}\color{white}\bfseries%
}

% ===== 表格跨页与宽度控制 =====
\usepackage{tabularx}
\usepackage{ltablex}
\keepXColumns

% 表格自动换行
\renewcommand{\tabularxcolumn}[1]{m{#1}}

% 表格不要超出页边距
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}

% ===== 代码块分页优化 =====
\sphinxsetup{
verbatimwithframe=false
}

\usepackage{tocloft}

% ===== 中文图表名称 =====
\AtBeginDocument{
    \renewcommand{\figurename}{图}
    \renewcommand{\tablename}{表}
    \renewcommand{\listfigurename}{图目录}
    \renewcommand{\listtablename}{表目录}
    
    % 防止图表目录编号和名称重叠
    \setlength{\cftfignumwidth}{3em}
    \setlength{\cfttabnumwidth}{3em}
}

''',
}

latex_additional_files = [
    '_static/cover.tex',
    '_static/backcover.tex',
    '_static/Logo.png',
    '_static/官网二维码.png',
    '_static/MiniCab Lite.png',
]

latex_keep_old_macro_names = True
latex_use_xindy = False
latex_toplevel_sectioning = 'chapter'

latex_elements.update({
    'releasename': '版本',
})

# -- todo extension ---------------------------------------

todo_include_todos = True

# -- autodoc ----------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- list-table 空单元格自动合并 -------------------------------------------

def _table_entry_is_empty(entry):
    """只把真正没有可见文字的 entry 视为空单元格。"""
    return not entry.astext().strip()


def _merge_empty_cells_in_table(table, logger):
    """按阅读顺序安全合并空单元格：同一行优先，再处理同一列。

    只处理规则的 list-table 网格。已有 rowspan/colspan 的表格会跳过，
    避免产生 LaTeX 无法表达的非矩形（L 形）合并区域。
    """
    tgroup = next(
        (child for child in table.children if isinstance(child, nodes.tgroup)),
        None,
    )
    if tgroup is None:
        return

    entries = list(tgroup.findall(nodes.entry))
    if any(entry.get('morerows', 0) or entry.get('morecols', 0)
           for entry in entries):
        logger.warning(
            '自动空单元格合并已跳过：该表格已经包含跨行或跨列单元格。',
            location=table,
        )
        return

    tbody = next(
        (child for child in tgroup.children if isinstance(child, nodes.tbody)),
        None,
    )
    if tbody is None:
        return

    rows = [child for child in tbody.children if isinstance(child, nodes.row)]
    if not rows:
        return

    column_count = int(tgroup.get('cols', 0)) or max(
        len(row.children) for row in rows
    )
    if any(len(row.children) != column_count for row in rows):
        logger.warning(
            '自动空单元格合并已跳过：该表格不是规则矩形。',
            location=table,
        )
        return

    # 使用固定网格记录原始位置；已合并并删除的单元格标记为 None。
    grid = [list(row.children) for row in rows]

    # 1. 从左到右：只要本行左侧有非空内容，空格优先并入左侧。
    # 例如 ``I/O端口,,说明`` 会把前两格横向合并；这一步必须早于
    # 纵向合并，否则空白的第二格会被错误并入上一行的“工业协议”。
    for row_index, row in enumerate(rows):
        anchor = None
        for column in range(column_count):
            cell = grid[row_index][column]
            if _table_entry_is_empty(cell) and anchor is not None:
                anchor['morecols'] = int(anchor.get('morecols', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = None if _table_entry_is_empty(cell) else cell

    # 2. 从上到下：只处理横向阶段后仍然存在的空格。
    # 为保证合并区域是矩形，不把空格并入已经横跨多列的单元格。
    for column in range(column_count):
        anchor = None
        for row_index, row in enumerate(rows):
            cell = grid[row_index][column]
            if cell is None:
                anchor = None
                continue
            if (_table_entry_is_empty(cell) and anchor is not None
                    and not anchor.get('morecols', 0)):
                anchor['morerows'] = int(anchor.get('morerows', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = (
                    None
                    if _table_entry_is_empty(cell) or cell.get('morecols', 0)
                    else cell
                )


def _merge_empty_table_cells(app, doctree, docname):
    """在输出 HTML/LaTeX 前转换 Docutils 表格节点。"""
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    for table in list(doctree.findall(nodes.table)):
        # 个别表格可用 :class: no-auto-merge 明确关闭自动合并。
        if 'no-auto-merge' not in table.get('classes', []):
            _merge_empty_cells_in_table(table, logger)


# -- 自定义 ------------------------------------------------

def setup(app):
    app.add_css_file('custom.css')
    app.connect('doctree-resolved', _merge_empty_table_cells)
    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

latex_elements['utf8extra'] = ''
