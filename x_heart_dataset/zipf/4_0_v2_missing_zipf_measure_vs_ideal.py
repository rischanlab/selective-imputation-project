# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20, 70, 100, 192]

    for k in k_list:
        file_ideal_topk = 'raw_results/heart.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        #print("Ideal topk", topk)
        a_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
        for a in a_list:
            for j in range(100):
                y = int(a * 100)
                try:
                    file_name = "raw_results/db_zipf" + str(y) + "_missing_measure" + str(j+1) + '.xlsx'
                    for file_view in glob.glob(file_name):
                        print(a, file_name, k)
                        missing = ag.get_topk_aggregate(k, file_view)
                        #print("Missing topk: ", missing)
                        #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                        #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                        with open('results/missing_zipf_measures_vs_ideal.csv', 'a', newline='') as f:
                            fields = [a, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                            writer = csv.writer(f)
                            writer.writerow(fields)
                except:
                    pass
