import pkgutil
import importlib
import subpackages


def print_submod_his():
    impl_modules = pkgutil.iter_modules(subpackages.__path__, subpackages.__name__ + ".")
    for mod in impl_modules:
        loaded_mod = importlib.import_module(mod.name)
        print(loaded_mod.sayhi())
