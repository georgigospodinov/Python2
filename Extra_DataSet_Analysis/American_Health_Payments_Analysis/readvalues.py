import csv

def get_values():
    """
        Get the lists of possible values for each variable.
        Read these values from a file "values.csv".

        :return: A list that contains all lists of values
        :rtype: list
    """
    inf = csv.reader(open("values.csv"))
    drgDef_list = inf.__next__()
    providerId_list = inf.__next__()
    providerName_list = inf.__next__()
    providerStreet_list = inf.__next__()
    providerCity_list = inf.__next__()
    providerState_list = inf.__next__()
    providerZip_list = inf.__next__()
    hospRef_list = inf.__next__()
    totalDischarges_list = inf.__next__()
    avgCovered_list = inf.__next__()
    avgTotal_list = inf.__next__()
    avgMedicare_list = inf.__next__()
    values_lists = [drgDef_list, providerId_list, providerName_list,
    		providerStreet_list, providerCity_list, providerState_list,
    		providerZip_list, hospRef_list, totalDischarges_list,
    		avgCovered_list, avgTotal_list, avgMedicare_list]
    return values_lists
