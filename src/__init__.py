"""change me"""
try:
    import pkg_resources as _pkg_resources
    _pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil as _pkg_util
    __path__ = _pkg_util.extend_path(__path__, __name__)
