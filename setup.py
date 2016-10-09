from distutils.core import setup, Extension

ext = Extension('bzip2', 
    sources=['bzip2.c'],
    extra_compile_args=['-O3', '-std=c99', '-Ofast'],
    extra_link_args=["-s", "-pthread"],
    language="c",
)

setup(
    name='bzip2', 
    author='S-YOU', author_email='S-YOU@users.noreply.github.com',
    description='bzip2 decompress + pthreads, python bindings',
    version='0.0.1', 
    url = 'https://github.com/S-YOU/bzip2',
    download_url = 'https://github.com/S-YOU/bzip2/tarball/master',
    ext_modules=[ext]
)
