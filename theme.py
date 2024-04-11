from jinja2 import Environment, PackageLoader, select_autoescape
from ruamel.yaml import YAML

yaml = YAML(typ='safe')   # default, if not specified, is 'rt' (round-trip)

themes = {
    'default': 'default.yaml',
    'moonlight': 'moonlight.yaml',
    'dawnlight': 'dawnlight.yaml',
    'daylight': 'daylight.yaml',
    'blacklight': 'blacklight.yaml'
}

for name in themes:
    with open(f'src/data/{themes[name]}') as theme_data_file:
        theme_data = yaml.load(theme_data_file)

    env = Environment(
        loader=PackageLoader('theme', 'src/templates'),
        autoescape=select_autoescape()
    )

    env.filters['bool'] = bool

    theme_template = env.get_template('theme.tmpl')
    theme_scheme_template = env.get_template('scheme.tmpl')

    with open(f'src/main/resources/{theme_data["theme_out_file"]}', 'w+') as theme_out_file:
        theme_out_file.write(theme_template.render(theme_data))
        theme_out_file.close()

    with open(f'src/main/resources/{theme_data["scheme_out_file"]}', 'w+') as scheme_out_file:
        scheme_out_file.write(theme_scheme_template.render(theme_data))
        scheme_out_file.close()
