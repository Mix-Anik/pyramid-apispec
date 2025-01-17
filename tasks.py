import os
import sys
import webbrowser

from invoke import task

docs_dir = "docs"
build_dir = os.path.join(docs_dir, "_build")


@task
def clean(ctx):
    ctx.run("rm -rf dist")
    ctx.run("rm -rf build")
    ctx.run("rm -rf pyramid_apispec.egg-info")


@task
def clean_docs(ctx):
    ctx.run("rm -rf %s" % build_dir)


@task
def browse_docs(ctx):
    path = os.path.join(build_dir, "index.html")
    webbrowser.open_new_tab(path)


def build_docs(ctx, browse):
    ctx.run("sphinx-build {} {}".format(docs_dir, build_dir), echo=True)
    if browse:
        browse_docs(ctx)


@task
def docs(ctx, clean=False, browse=False, watch=False):
    """Build the docs."""
    if clean:
        clean_docs(ctx)
    if watch:
        watch_docs(ctx, browse=browse)
    else:
        build_docs(ctx, browse=browse)


@task
def watch_docs(ctx, browse=False):
    """Run build the docs when a file changes."""
    try:
        import sphinx_autobuild  # noqa
    except ImportError:
        print("ERROR: watch task requires the sphinx_autobuild package.")
        print("Install it with:")
        print("    pip install sphinx-autobuild")
        sys.exit(1)
    ctx.run(
        "sphinx-autobuild {} {} {} -z marshmallow".format(
            "--open-browser" if browse else "", docs_dir, build_dir
        ),
        echo=True,
        pty=True,
    )


@task
def readme(ctx, browse=False):
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab("README.html")


@task(clean)
def build(ctx):
    ctx.run("python3 -m build")


@task(build)
def release(ctx):
    ctx.run("python3 -m twine upload dist/*")
