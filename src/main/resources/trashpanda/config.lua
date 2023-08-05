local theme = require("trashpanda.theme")
-- General Configs for theme

local trashpanda = {}

trashpanda.configure = function(colorscheme)
	local function apply_theme(colorscheme)
		for group, parameters in pairs(colorscheme) do
			vim.api.nvim_set_hl(0, group, parameters)
		end
	end

	apply_theme(colorscheme)	
end

return trashpanda
