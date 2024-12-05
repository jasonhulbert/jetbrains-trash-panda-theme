from jinja2 import Environment, PackageLoader, select_autoescape
from ruamel.yaml import YAML
from color_utils import srgb_to_p3, hex_to_srgb

yaml = YAML(typ='safe')

themes = {
    'default': 'default.yaml',
    'starlight': 'starlight.yaml',
    'moonlight': 'moonlight.yaml',
    'dawnlight': 'dawnlight.yaml',
    'daylight': 'daylight.yaml',
    'blacklight': 'blacklight.yaml'
}

def generate_theme_file(theme_template, theme_data):
    with open(f'src/main/resources/META-INF/{theme_data["theme_out_file"]}', 'w+') as theme_out_file:
        theme_out_file.write(theme_template.render(theme_data))
        theme_out_file.close()

def generate_scheme_file(scheme_template, theme_data):
    with open(f'src/main/resources/META-INF/{theme_data["scheme_out_file"]}', 'w+') as scheme_out_file:
        scheme_out_file.write(scheme_template.render(theme_data))
        scheme_out_file.close()

def generate_iterm_theme_file(iterm_theme_template, theme_data):
    add_iterm_theme_data = {'srgb': {}, 'p3': {}}

    for (key, value) in theme_data['theme'].items():
        if value is not None:
            srgb = hex_to_srgb(value)
            p3 = srgb_to_p3(srgb)

            add_iterm_theme_data['srgb'][key] = srgb
            add_iterm_theme_data['p3'][key] = p3

    theme_data['iterm'] = add_iterm_theme_data

    with open(f'iterm/{theme_data["iterm_theme_out_file"]}', 'w+') as iterm_theme_out_file:
        iterm_theme_out_file.write(iterm_theme_template.render(theme_data))
        iterm_theme_out_file.close()

def generate_warp_theme_file(warp_theme_template, theme_data):
    with open(f'warp/{theme_data["warp_theme_out_file"]}', 'w+') as scheme_out_file:
        scheme_out_file.write(warp_theme_template.render(theme_data))
        scheme_out_file.close()

def generate_theme_files():
    for name in themes:
        with open(f'src/data/{themes[name]}') as theme_data_file:
            theme_data = yaml.load(theme_data_file)

        jinja_env = Environment(
            loader=PackageLoader('theme', '../src/templates'),
            autoescape=select_autoescape()
        )

        jinja_env.filters['bool'] = bool

        generate_theme_file(jinja_env.get_template('theme.tmpl'), theme_data)
        generate_scheme_file(jinja_env.get_template('scheme.tmpl'), theme_data)
        generate_iterm_theme_file(jinja_env.get_template('iterm-theme.tmpl'), theme_data)
        generate_warp_theme_file(jinja_env.get_template('warp-theme.tmpl'), theme_data)