# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob



ideal_df = ag.df_ideal('raw_results/heart.xlsx')


if __name__ == "__main__":

    k_list = [5, 10, 15, 20, 50, 80, 100, 192]

    for k in k_list:
        topk = ag.get_utility_score_ideal_topk(k, ideal_df)
        print("Ideal topk", topk)
        percentage_list = [0,5,10,15,20,25,30]
        for percent in percentage_list:
            for i in range(100):
                file_name = 'raw_results/db_' +str(percent) + 'rand_missing_measure' + str(i+1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)
                    missing = ag.get_utility_score_missing_topk(k, ideal_df, file_view)
                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/cum_missing_measures_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.cum_score(topk, missing)]
                        writer = csv.writer(f)
                        writer.writerow(fields)