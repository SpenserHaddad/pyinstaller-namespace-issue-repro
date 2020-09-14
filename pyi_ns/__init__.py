import pkgutil
import importlib
import subpackages

def print_namespace():
    print(subpackages)

def print_submod_his():
    impl_modules = pkgutil.iter_modules(subpackages.__path__, subpackages.__name__ + ".")
    for mod in impl_modules:
        loaded_mod = importlib.import_module(mod.name)
        print(loaded_mod.sayhi())

def print_submod_b_hi():
    try:
        from subpackages import submod_b
        print(submod_b.sayhi())
    except ImportError:
        print("submod_b not installed!")
