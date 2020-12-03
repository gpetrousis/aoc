""" Noxfile definition """
import tempfile
import nox


nox.options.sessions = "lint", "tests"
locations = "src", "tests", "noxfile.py"


def install_with_constraints(session, *args, **kwargs):
    """ Install dev dependencies from poetry """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.8"])
def tests(session):
    """ Run tests """
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


@nox.session(python=["3.8"])
def lint(session):
    """ Run Linter """
    args = session.posargs or locations
    install_with_constraints(
        session, "flake8", "flake8-black", "flake8-bugbear", "flake8-bandit"
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def black(session):
    """ Run Black auto-formatter """
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)
