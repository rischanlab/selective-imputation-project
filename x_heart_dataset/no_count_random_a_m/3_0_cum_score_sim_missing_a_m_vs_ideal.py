# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob



if __name__ == "__main__":

    k_list = [5,6,7,8,9,10,11,12,13,15,20,30,40,50,60,70,78,144]

    ideal_df = ag.df_ideal_sim('raw_results/heart.xlsx')


    for k in k_list:
        file_ideal_topk = 'raw_results/heart.xlsx'
        topk = ag.get_utility_score_ideal_topk_sim(k, ideal_df)
        print("Ideal topk", topk)
        percentage_list = [0,10,20,30,40,50,60,70,80,90]
        for percent in percentage_list:
            for i in range(100):
                try:
                    file_name = 'raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
                    for file_view in glob.glob(file_name):
                        print(percent, file_name, k)
                        missing = ag.get_utility_score_missing_topk_sim(k, ideal_df, file_view)
                        #print("Missing topk: ", missing)
                        #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                        #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                        with open('results/cum_sim_missing_a_m_vs_ideal.csv', 'a', newline='') as f:
                            fields = [percent, k, ag.cum_score(topk, missing)]
                            writer = csv.writer(f)
                            writer.writerow(fields)
                            print(fields)
                except:
                    pass  # doing nothing on exception
                print("done")