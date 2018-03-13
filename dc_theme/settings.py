import os

root_path = os.path.dirname(os.path.abspath(__file__))

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.ManifestFinder',
)

SASS_INCLUDE_PATHS = (
    root_path + '/static/dc_theme/scss/',
)

SASS_ARGUMENT_LIST = ["-I " + p for p in SASS_INCLUDE_PATHS]
SASS_ARGUMENT_LIST.append("--style compressed")
SASS_ARGUMENT_LIST.append("--sourcemap")

DEFAULT_PIPELINE = {
    'COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
    ),
    'SASS_BINARY': 'sassc',
    'SASS_ARGUMENTS': ' '.join(SASS_ARGUMENT_LIST),
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'STYLESHEETS': {
        'styles': {
            'source_filenames': [],
            'output_filename': 'css/styles.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.JSMinCompressor',
    'JAVASCRIPT': {
        'scripts': {
            'source_filenames': [
                'dc_theme/js/jquery.js',
                'dc_theme/js/app.js'
            ],
            'output_filename': 'js/scripts.js',
        }
    }
}


def get_pipeline_settings(extra_css=None, extra_js=None):
    PIPELINE = DEFAULT_PIPELINE
    if extra_css:
        PIPELINE['STYLESHEETS']['styles']['source_filenames'] += extra_css
    if extra_js:
        PIPELINE['JAVASCRIPT']['scripts']['source_filenames'] += extra_js
    return PIPELINE
