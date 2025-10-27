pip instatry:
    import openpyxl
    print(f"openpyxl è installato (versione: {openpyxl.__version__})")
except ImportError:
    print("openpyxl non è installato")