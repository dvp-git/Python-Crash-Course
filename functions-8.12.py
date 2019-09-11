# Exerecise 8.12 Sandwiches


##Defining a function called sandwiches which accepts list of items a person wants
def sandwiches(crust,filling='mayo',*layers):
    """Summarizing the sandwich"""
    print("\nHere is your " + crust + " crusted " + filling + " sandwich  with the following layers:")
    for layer in layers:
        print("-->" + layer)

        
sandwiches('thin','cheese','pepporoni','salami','peppers')

sandwiches('thin','','tuna')

sandwiches('pan')
