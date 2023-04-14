" Name:			trashpanda
" Author:		Original Author: Jason Hulbert, https://github.com/jasonhulbert
" Maintainer:		Current Maintainer: Charlie McLovins, https://github.com/charlie-mclovins

set background=dark

hi clear

let g:colors_name= 'trashpanda'

let s:t_Co = exists('&t_Co') && !has('gui_running') ? (&t_Co ?? 0) : -1

hi! link Terminal Normal
hi! link Boolean Constant
hi! link Character Constant
hi! link Conditional Statement
hi! link Debug Special
hi! link Define PreProc
hi! link Delimiter Special
hi! link Exception Statement
hi! link Float Number
hi! link Function Identifier
hi! link Include PreProc
hi! link IncSearch Visual
hi! link Keyword Statement
hi! link Label Statement
hi! link LineNrAbove LineNr
hi! link LineNrBelow LineNr
hi! link Macro PreProc
hi! link Number Constant
hi! link Operator Statement
hi! link PopupSelected PmenuSel
hi! link PreCondit PreProc
hi! link Repeat Statement
hi! link SpecialChar Special
hi! link SpecialComment Special
hi! link StatusLineTerm StatusLine
hi! link StatusLineTermNC StatusLineNC
hi! link StorageClass Type
hi! link String Constant
hi! link Structure Type
hi! link Tag Special
hi! link Typedef Type
hi! link lCursor Cursor
hi! link CurSearch Search
hi! link CursorLineFold CursorLine
hi! link CursorLineSign CursorLine
hi! link MessageWindow Pmenu
hi! link PopupNotification Todo
" Format
" hi [element] guifg=[color] guibg=[color]
" gui=[bold,undercurl,italic], cterm=[], ctermfg=[], ctermbg=[]
hi Normal guifg=#B8BABD guibg=#141618 gui=NONE cterm=NONE
hi ColorColumn guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi CursorColumn guifg=NONE guibg=#2C99DB gui=NONE cterm=NONE
hi CursorLine guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi CursorLineNr guifg=#42BA90 guibg=#141618 gui=NONE cterm=NONE
hi Folded guifg=#B5B6E3 guibg=#2C3135 gui=NONE cterm=NONE
hi QuickFixLine guifg=#113A52 guibg=NONE gui=NONE cterm=NONE
hi Conceal guifg=NONE guibg=#2C3135 gui=NONE cterm=NONE
hi Cursor guifg=#141618 guibg=#406BF3 gui=NONE cterm=NONE
hi Directory guifg=#2C99DB guibg=#141618 gui=NONE cterm=NONE
hi EndOfBuffer guifg=#B8BABD guibg=#141618 gui=NONE cterm=NONE
hi ErrorMsg guifg=#F05553 guibg=NONE gui=NONE cterm=NONE
hi FoldColumn guifg=NONE guibg=#5F656A gui=NONE cterm=NONE
hi LineNr guifg=#2C3135 guibg=NONE gui=NONE cterm=NONE
hi MatchParen guifg=#FFFFFF guibg=#406BF4 gui=NONE cterm=NONE
hi ModeMsg guifg=#1D2123 guibg=#42BA90 gui=NONE cterm=NONE
hi MoreMsg guifg=#215D48 guibg=NONE gui=NONE cterm=NONE
hi NonText guifg=#B8BABD guibg=#141618 gui=NONE cterm=NONE
hi PMenu guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi PMenuSbar guifg=NONE guibg=#2C3135 gui=NONE cterm=NONE
hi PMenuSel guifg=#1D2123 guibg=#42BA90 gui=NONE cterm=NONE
hi PMenuThumb guifg=NONE guibg=#42BA90 gui=NONE cterm=NONE
hi Question guifg=#F05553 guibg=#5F656A gui=NONE cterm=NONE
hi Search guifg=#B8BABD guibg=#113A52 gui=NONE cterm=NONE
hi SignColumn guifg=#2C3135 guibg=#FFFFFF gui=NONE cterm=NONE
hi SpecialKey guifg=#6E623E guibg=NONE gui=NONE cterm=NONE
hi SpellBad guifg=NONE guibg=NONE gui=undercurl cterm=underline
hi SpellCap guifg=NONE guibg=NONE gui=undercurl cterm=underline
hi SpellLocal guifg=NONE guibg=NONE gui=undercurl cterm=underline
hi SpellRare guifg=NONE guibg=NONE gui=undercurl cterm=underline
hi StatusLine guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi StatusLineNC guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi TabLine guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi TabLineFill guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi TabLineSel guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi Title guifg=#215D48 guibg=#1D2123 gui=NONE cterm=NONE
hi VertSplit guifg=#2C3134 guibg=#141618 gui=NONE cterm=NONE
hi Visual guifg=#406BF4 guibg=#101B3D gui=NONE cterm=NONE
hi VisualNOS guifg=#406BF4 guibg=#101B3D gui=NONE cterm=NONE
hi WarningMsg guifg=#F05553 guibg=#3C1515 gui=NONE cterm=NONE
hi WildMenu guifg=#42BA90 guibg=#1D2123 gui=NONE cterm=NONE
hi Comment guifg=#727A7F guibg=NONE gui=NONE cterm=NONE
hi Constant guifg=#B8BABD guibg=NONE gui=NONE cterm=NONE
hi Error guifg=#3C1515 guibg=#F05553 gui=NONE cterm=NONE
hi Identifier guifg=#B8BABD guibg=NONE gui=NONE cterm=NONE
hi Ignore guifg=#686A4E guibg=NONE gui=NONE cterm=NONE
hi PreProc guifg=#DCC37C guibg=NONE gui=NONE cterm=NONE
hi Special guifg=#215D48 guibg=NONE gui=NONE cterm=NONE
hi Statement guifg=#A07CF1 guibg=NONE gui=NONE cterm=NONE
hi Todo guifg=#406BF4 guibg=#101B3D gui=NONE cterm=NONE
hi Type guifg=#8EC475 guibg=NONE gui=NONE cterm=NONE
hi Underline guifg=#F05553 guibg=NONE gui=bold,underline cterm=underline
hi CursorIM guifg=NONE guibg=NONE gui=NONE cterm=NONE
hi ToolbarLine guifg=NONE guibg=NONE gui=NONE cterm=NONE
hi ToolbarButton guifg=NONE guibg=NONE gui=NONE cterm=NONE
hi DiffAdd guifg=#42BA90 guibg=NONE gui=NONE cterm=NONE
hi DiffChange guifg=#F07F5B guibg=NONE gui=NONE cterm=NONE
hi DiffText guifg=#B8BABD guibg=NONE gui=NONE cterm=NONE
hi DiffDelete guifg=#F05553 guibg=NONE gui=NONE cterm=NONE

if s:t_Co >= 256
	" For colors possible see 256colors

	hi Normal ctermfg=250 ctermbg=233 cterm=NONE
	hi ColorColumn ctermfg=079 ctermbg=234 cterm=NONE
	hi CursorColumn ctermfg=NONE ctermbg=039 cterm=NONE
	hi CursorLine ctermfg=079 ctermbg=234 cterm=NONE
	hi CursorLineNr ctermfg=079 ctermbg=233 cterm=NONE
	hi Folded ctermfg=097 ctermbg=235 cterm=NONE
	hi QuickFixLine ctermfg=006 ctermbg=NONE cterm=NONE
	hi Conceal ctermfg=NONE ctermbg=235 cterm=NONE
	hi Cursor ctermfg=079 ctermbg=NONE cterm=NONE
	hi Directory ctermfg=039 ctermbg=233 cterm=NONE
	hi EndOfBuffer ctermfg=250 ctermbg=233 cterm=NONE
	hi ErrorMsg ctermfg=203 ctermbg=NONE cterm=NONE
	hi FoldColumn ctermfg=NONE ctermbg=240 cterm=NONE
	hi LineNr ctermfg=235 ctermbg=NONE cterm=NONE
	hi MatchParen ctermfg=015 ctermbg=027 cterm=NONE
	hi ModeMsg ctermfg=234 ctermbg=079 cterm=NONE
	hi MoreMsg ctermfg=023 ctermbg=NONE cterm=NONE
	hi NonText ctermfg=250 ctermbg=233 cterm=NONE
	hi PMenu ctermfg=079 ctermbg=234 cterm=NONE
	hi PMenuSbar ctermfg=NONE ctermbg=235 cterm=NONE
	hi PMenuSel ctermfg=234 ctermbg=079 cterm=NONE
	hi PMenuThumb ctermfg=NONE ctermbg=079 cterm=NONE
	hi Question ctermfg=203 ctermbg=240 cterm=NONE
	hi Search ctermfg=250 ctermbg=006 cterm=NONE
	hi SignColumn ctermfg=235 ctermbg=015 cterm=NONE
	hi SpecialKey ctermfg=058 ctermbg=NONE cterm=NONE
	hi SpellBad ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellCap ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellLocal ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellRare ctermfg=NONE ctermbg=NONE cterm=underline
	hi StatusLine ctermfg=079 ctermbg=234 cterm=NONE
	hi StatusLineNC ctermfg=079 ctermbg=234 cterm=NONE
	hi TabLine ctermfg=079 ctermbg=234 cterm=NONE
	hi TabLineFill ctermfg=079 ctermbg=234 cterm=NONE
	hi TabLineSel ctermfg=079 ctermbg=234 cterm=NONE
	hi Title ctermfg=023 ctermbg=234 cterm=NONE
	hi VertSplit ctermfg=235 ctermbg=233 cterm=NONE
	hi Visual ctermfg=027 ctermbg=017 cterm=NONE
	hi VisualNOS ctermfg=027 ctermbg=017 cterm=NONE
	hi WarningMsg ctermfg=203 ctermbg=052 cterm=NONE
	hi WildMenu ctermfg=079 ctermbg=234 cterm=NONE
	hi Comment ctermfg=243 ctermbg=NONE cterm=NONE
	hi Constant ctermfg=250 ctermbg=NONE cterm=NONE
	hi Error ctermfg=052 ctermbg=203 cterm=NONE
	hi Identifier ctermfg=250 ctermbg=NONE cterm=NONE
	hi Ignore ctermfg=058 ctermbg=NONE cterm=NONE
	hi PreProc ctermfg=186 ctermbg=NONE cterm=NONE
	hi Special ctermfg=023 ctermbg=NONE cterm=NONE
	hi Statement ctermfg=141 ctermbg=NONE cterm=NONE
	hi Todo ctermfg=027 ctermbg=017 cterm=NONE
	hi Type ctermfg=114 ctermbg=NONE cterm=NONE
	hi Underline ctermfg=203 ctermbg=NONE cterm=underline
	hi CursorIM ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarButton ctermfg=NONE ctermbg=NONE cterm=NONE
	hi DiffAdd ctermfg=079 ctermbg=NONE cterm=NONE
	hi DiffChange ctermfg=209 ctermbg=NONE cterm=NONE
	hi DiffText ctermfg=250 ctermbg=NONE cterm=NONE
	hi DiffDelete ctermfg=203 ctermbg=NONE cterm=NONE
	unlet s:t_Co
	finish
endif

if s:t_Co >= 16
	" For colors possible see 16colors

	hi Normal ctermfg=007 ctermbg=000 cterm=NONE
	hi ColorColumn ctermfg=010 ctermbg=000 cterm=NONE
	hi CursorColumn ctermfg=NONE ctermbg=012 cterm=NONE
	hi CursorLine ctermfg=010 ctermbg=000 cterm=NONE
	hi CursorLineNr ctermfg=010 ctermbg=000 cterm=NONE
	hi Folded ctermfg=097 ctermbg=000 cterm=NONE
	hi QuickFixLine ctermfg=004 ctermbg=NONE cterm=NONE
	hi Conceal ctermfg=NONE ctermbg=000 cterm=NONE
	hi Cursor ctermfg=010 ctermbg=NONE cterm=NONE
	hi Directory ctermfg=012 ctermbg=000 cterm=NONE
	hi EndOfBuffer ctermfg=007 ctermbg=000 cterm=NONE
	hi ErrorMsg ctermfg=009 ctermbg=NONE cterm=NONE
	hi FoldColumn ctermfg=NONE ctermbg=008 cterm=NONE
	hi LineNr ctermfg=000 ctermbg=NONE cterm=NONE
	hi MatchParen ctermfg=015 ctermbg=012 cterm=NONE
	hi ModeMsg ctermfg=000 ctermbg=010 cterm=NONE
	hi MoreMsg ctermfg=002 ctermbg=NONE cterm=NONE
	hi NonText ctermfg=007 ctermbg=000 cterm=NONE
	hi PMenu ctermfg=010 ctermbg=000 cterm=NONE
	hi PMenuSbar ctermfg=NONE ctermbg=000 cterm=NONE
	hi PMenuSel ctermfg=000 ctermbg=010 cterm=NONE
	hi PMenuThumb ctermfg=NONE ctermbg=010 cterm=NONE
	hi Question ctermfg=009 ctermbg=008 cterm=NONE
	hi Search ctermfg=007 ctermbg=004 cterm=NONE
	hi SignColumn ctermfg=000 ctermbg=015 cterm=NONE
	hi SpecialKey ctermfg=003 ctermbg=NONE cterm=NONE
	hi SpellBad ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellCap ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellLocal ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellRare ctermfg=NONE ctermbg=NONE cterm=underline
	hi StatusLine ctermfg=010 ctermbg=000 cterm=NONE
	hi StatusLineNC ctermfg=010 ctermbg=000 cterm=NONE
	hi TabLine ctermfg=010 ctermbg=000 cterm=NONE
	hi TabLineFill ctermfg=010 ctermbg=000 cterm=NONE
	hi TabLineSel ctermfg=010 ctermbg=000 cterm=NONE
	hi Title ctermfg=002 ctermbg=000 cterm=NONE
	hi VertSplit ctermfg=000 ctermbg=000 cterm=NONE
	hi Visual ctermfg=012 ctermbg=004 cterm=NONE
	hi VisualNOS ctermfg=012 ctermbg=004 cterm=NONE
	hi WarningMsg ctermfg=009 ctermbg=052 cterm=NONE
	hi WildMenu ctermfg=010 ctermbg=000 cterm=NONE
	hi Comment ctermfg=008 ctermbg=NONE cterm=NONE
	hi Constant ctermfg=007 ctermbg=NONE cterm=NONE
	hi Error ctermfg=052 ctermbg=009 cterm=NONE
	hi Identifier ctermfg=007 ctermbg=NONE cterm=NONE
	hi Ignore ctermfg=003 ctermbg=NONE cterm=NONE
	hi PreProc ctermfg=011 ctermbg=NONE cterm=NONE
	hi Special ctermfg=002 ctermbg=NONE cterm=NONE
	hi Statement ctermfg=005 ctermbg=NONE cterm=NONE
	hi Todo ctermfg=012 ctermbg=004 cterm=NONE
	hi Type ctermfg=010 ctermbg=NONE cterm=NONE
	hi Underline ctermfg=009 ctermbg=NONE cterm=underline
	hi CursorIM ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarButton ctermfg=NONE ctermbg=NONE cterm=NONE
	hi DiffAdd ctermfg=010 ctermbg=NONE cterm=NONE
	hi DiffChange ctermfg=009 ctermbg=NONE cterm=NONE
	hi DiffText ctermfg=007 ctermbg=NONE cterm=NONE
	hi DiffDelete ctermfg=009 ctermbg=NONE cterm=NONE
	unlet s:t_Co
	finish
endif

if s:t_Co >= 8
	" For colors possible see 8colors

	hi Normal ctermfg=007 ctermbg=000 cterm=NONE
	hi ColorColumn ctermfg=002 ctermbg=000 cterm=NONE
	hi CursorColumn ctermfg=NONE ctermbg=004 cterm=NONE
	hi CursorLine ctermfg=002 ctermbg=000 cterm=NONE
	hi CursorLineNr ctermfg=002 ctermbg=000 cterm=NONE
	hi Folded ctermfg=017 ctermbg=000 cterm=NONE
	hi QuickFixLine ctermfg=004 ctermbg=NONE cterm=NONE
	hi Conceal ctermfg=NONE ctermbg=000 cterm=NONE
	hi Cursor ctermfg=002 ctermbg=NONE cterm=NONE
	hi Directory ctermfg=004 ctermbg=000 cterm=NONE
	hi EndOfBuffer ctermfg=007 ctermbg=000 cterm=NONE
	hi ErrorMsg ctermfg=001 ctermbg=NONE cterm=NONE
	hi FoldColumn ctermfg=NONE ctermbg=007 cterm=NONE
	hi LineNr ctermfg=000 ctermbg=NONE cterm=NONE
	hi MatchParen ctermfg=007 ctermbg=004 cterm=NONE
	hi ModeMsg ctermfg=000 ctermbg=002 cterm=NONE
	hi MoreMsg ctermfg=002 ctermbg=NONE cterm=NONE
	hi NonText ctermfg=007 ctermbg=000 cterm=NONE
	hi PMenu ctermfg=002 ctermbg=000 cterm=NONE
	hi PMenuSbar ctermfg=NONE ctermbg=000 cterm=NONE
	hi PMenuSel ctermfg=000 ctermbg=002 cterm=NONE
	hi PMenuThumb ctermfg=NONE ctermbg=002 cterm=NONE
	hi Question ctermfg=001 ctermbg=007 cterm=NONE
	hi Search ctermfg=007 ctermbg=004 cterm=NONE
	hi SignColumn ctermfg=000 ctermbg=007 cterm=NONE
	hi SpecialKey ctermfg=003 ctermbg=NONE cterm=NONE
	hi SpellBad ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellCap ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellLocal ctermfg=NONE ctermbg=NONE cterm=underline
	hi SpellRare ctermfg=NONE ctermbg=NONE cterm=underline
	hi StatusLine ctermfg=002 ctermbg=000 cterm=NONE
	hi StatusLineNC ctermfg=002 ctermbg=000 cterm=NONE
	hi TabLine ctermfg=002 ctermbg=000 cterm=NONE
	hi TabLineFill ctermfg=002 ctermbg=000 cterm=NONE
	hi TabLineSel ctermfg=002 ctermbg=000 cterm=NONE
	hi Title ctermfg=002 ctermbg=000 cterm=NONE
	hi VertSplit ctermfg=000 ctermbg=000 cterm=NONE
	hi Visual ctermfg=004 ctermbg=004 cterm=NONE
	hi VisualNOS ctermfg=004 ctermbg=004 cterm=NONE
	hi WarningMsg ctermfg=001 ctermbg=052 cterm=NONE
	hi WildMenu ctermfg=002 ctermbg=000 cterm=NONE
	hi Comment ctermfg=007 ctermbg=NONE cterm=NONE
	hi Constant ctermfg=007 ctermbg=NONE cterm=NONE
	hi Error ctermfg=052 ctermbg=001 cterm=NONE
	hi Identifier ctermfg=007 ctermbg=NONE cterm=NONE
	hi Ignore ctermfg=003 ctermbg=NONE cterm=NONE
	hi PreProc ctermfg=003 ctermbg=NONE cterm=NONE
	hi Special ctermfg=002 ctermbg=NONE cterm=NONE
	hi Statement ctermfg=005 ctermbg=NONE cterm=NONE
	hi Todo ctermfg=004 ctermbg=004 cterm=NONE
	hi Type ctermfg=002 ctermbg=NONE cterm=NONE
	hi Underline ctermfg=001 ctermbg=NONE cterm=underline
	hi CursorIM ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
	hi ToolbarButton ctermfg=NONE ctermbg=NONE cterm=NONE
	hi DiffAdd ctermfg=002 ctermbg=NONE cterm=NONE
	hi DiffChange ctermfg=001 ctermbg=NONE cterm=NONE
	hi DiffText ctermfg=007 ctermbg=NONE cterm=NONE
	hi DiffDelete ctermfg=001 ctermbg=NONE cterm=NONE
	unlet s:t_Co
	finish
endif

if s:t_Co >= 0
	hi Normal term=NONE
  	hi ColorColumn term=reverse
  	hi Conceal term=NONE
  	hi Cursor term=reverse
  	hi CursorColumn term=NONE
  	hi CursorLine term=underline
  	hi CursorLineNr term=bold
  	hi DiffAdd term=reverse
  	hi DiffChange term=NONE
  	hi DiffDelete term=reverse
  	hi DiffText term=reverse
  	hi Directory term=NONE
  	hi EndOfBuffer term=NONE
  	hi ErrorMsg term=bold,reverse
  	hi FoldColumn term=NONE
  	hi Folded term=NONE
  	hi IncSearch term=bold,reverse,underline
  	hi LineNr term=NONE
  	hi MatchParen term=bold,underline
  	hi ModeMsg term=bold
  	hi MoreMsg term=NONE
  	hi NonText term=NONE
  	hi Pmenu term=reverse
  	hi PmenuSbar term=reverse
  	hi PmenuSel term=bold
  	hi PmenuThumb term=NONE
  	hi Question term=standout
  	hi Search term=reverse
  	hi SignColumn term=reverse
  	hi SpecialKey term=bold
  	hi SpellBad term=underline
  	hi SpellCap term=underline
  	hi SpellLocal term=underline
  	hi SpellRare term=underline
  	hi StatusLine term=bold,reverse
  	hi StatusLineNC term=bold,underline
  	hi TabLine term=bold,underline
  	hi TabLineFill term=NONE
  	hi Terminal term=NONE
  	hi TabLineSel term=bold,reverse
  	hi Title term=NONE
  	hi VertSplit term=NONE
  	hi Visual term=reverse
  	hi VisualNOS term=NONE
  	hi WarningMsg term=standout
  	hi WildMenu term=bold
  	hi CursorIM term=NONE
  	hi ToolbarLine term=reverse
  	hi ToolbarButton term=bold,reverse
  	hi CurSearch term=reverse
  	hi CursorLineFold term=underline
  	hi CursorLineSign term=underline
  	hi Comment term=bold
  	hi Constant term=NONE
  	hi Error term=bold,reverse
  	hi Identifier term=NONE
  	hi Ignore term=NONE
  	hi PreProc term=NONE
  	hi Special term=NONE
  	hi Statement term=NONE
  	hi Todo term=bold,reverse
  	hi Type term=NONE
  	hi Underlined term=underline
	unlet s:t_Co
	finish
endif
" Colors			256		16		8
"        	Hexcode		Xterm 256 code	Ansi 16 code    Ansi 8 code
" base1: 	#141618		233 #121212	000		000
" base2: 	#1D2123		234 #1C1C1C	000		000
" base3: 	#2C3135		235 #262626	000		000
" base4: 	#5F656A		240 #585858	008		007
" base5: 	#727A7F		243 #767676	008		007
" base6:	#B8BABD		250 #BCBCBC	007		007
" base7:	#E2E2E2		254 #E4E4E4	015		007
" base8: 	#FFFFFF		015 #FFFFFF	015		007
"
" accent: 	#406BF4		027 #005FFF	012		004
" accent_mod1: 	#3050B7		025 #005FAF	012		004
" accent_mod2: 	#18285C		019 #0000AF 	004		004
" accent_mod3: 	#101B3D		017 #00005F	004		004

" lime: 	#8EC475		114 #87D787	010		002
" lime_mod1: 	#6B9358		107 #87AF5F	010		002
" lime_mod2: 	#47623B		065 #5F875F	002		002
" lime_mod3: 	#24311D		234 #1C1C1C	002		002

" green: 	#42BA90		079 #5FD7AF	010		002
" green_mod1: 	#328B6C		029 #00875F	010		002
" green_mod2: 	#215D48		023 #005F5F	002		002
" green_mod3: 	#102F24		022 #005F00	002		002

" blue: 	#2C99DB		039 #00AFFF 	012		004
" blue_mod1: 	#2173A4		031 #0087AF	012		004
" blue_mod2: 	#113A52		006 #008080	004		004
" blue_mod3: 	#0B2637		004 #000080	004		004

" cyan: 	#50CAE5		081 #5FD7FF	014		006
" cyan_mod1: 	#3C98AC		037 #00AFAF	014		006
" cyan_mod2: 	#1E4C56		024 #005F87	006		006
" cyan_mod3: 	#143239		235 #262626	006		006

" purple: 	#A07CF1		141 #AF87FF	005		005
" purple_mod1: 	#785DB5		097 #875FAF	005		005
" purple_mod2: 	#3C2f5B		054 #5F0087	005		005
" purple_mod3: 	#281F3C		053 #5F005F	005		005

" pink: 	#DC6096		168 #D75F87	013		005
" pink_mod1: 	#A54871		132 #AF5F87	013		005
" pink_mod2: 	#532439		089 #87005F	013		005
" pink_mod3: 	#371826		088 #870000	013		005

" red: 		#F05553		203 #FF5F5F	009		001
" red_mod1: 	#B4403E		131 #AF5F5F	009		001
" red_mod2: 	#5A201F		001 #800000	001		001
" red_mod3: 	#3C1515		052 #5F0000	001		001
"
" orange: 	#F07F5B		209 #FF875F	009		003
" orange_mod1: 	#B45F44		130 #AF5F00	009		003
" orange_mod2: 	#5A3022		094 #875F00	003		003
" orange_mod3: 	#3C2017		235 #262626	001		003

" yellow: 	#DCC37C		186 #DFDF87	011		003
" yellow_mod1: 	#A5925D		143 #AFAF5F	011		003
" yellow_mod2: 	#6E623E		058 #5F5F00	003		003

" Not Used or merged with similar color in smaller color spaces
" disabled: 	#686A4E		
" macro_gold: 	#908B25
" macro_blue:	#4AEDE5
" class_purple: #B5B6E3
" typedef: 	#B9BCD1
" function:	#FFC66D
" Git stuff
" green -> green
" orange -> orange
" red -> red
" blue -> blue
" grey -> ase6
" white -> base7
