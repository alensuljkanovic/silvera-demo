from silvera.generator.registration import GeneratorDesc


def generate(decl, output_dir, debug):
    print("Called!")
    print(decl, output_dir)


# Create Python generator.
python = GeneratorDesc(
    language_name="python",
    language_ver="3.7.4",
    description="Python 3.7.4 code generator",
    gen_func=generate
)