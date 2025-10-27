try:
    import xlrd
    print(f"xlrd è installato (versione: {xlrd.__version__})")
except ImportError:
    print("xlrd non è installato")