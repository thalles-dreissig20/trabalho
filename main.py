from controllers.index import IndexController

if __name__ == "__main__":
    try:
        IndexController().initialize()
    except KeyboardInterrupt:
        print("\nEncerrando o programa. Até logo!")