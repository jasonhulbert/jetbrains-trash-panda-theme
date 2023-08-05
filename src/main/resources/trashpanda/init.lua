local config = require("trashpanda.config")
local colors = require("trashpanda.colors")
local theme = require("trashpanda.theme")

-- TODO add error checking

-- init file for theme

local trashpanda = {}

trashpanda.register = function()
	if vim.fn.exists('syntax_on') then
		vim.api.nvim_command('syntax reset')
	end
	vim.g.colors_name = 'trashpanda'
	config.configure(theme.classic)	
end

return trashpanda
