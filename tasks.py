import pathlib
import shutil
import warnings

import invoke


ROOT = pathlib.Path(__file__).resolve().parent


@invoke.task()
def clean(ctx, b=None):
    target = ROOT.joinpath('build')
    if b:
        target = target.joinpath(b)
    try:
        print(f'removing {target}')
        shutil.rmtree(str(target))
    except OSError as e:
        warnings.warn(f'failed to remove {target}: {e}', ResourceWarning)
