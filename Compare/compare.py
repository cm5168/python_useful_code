import numpy as np

prediction = np.genfromtxt("prediction.txt", delimiter="|")
prediction_index = prediction[:,0]*1000000+prediction[:,1]

trueResult = np.genfromtxt("test_valid_new.txt", delimiter = "|")
trueResult_index = trueResult[:,0]*1000000+trueResult[:,1]

index = np.arange(len(trueResult))
prediction_new = prediction[np.argsort(prediction_index)]
prediction_new = prediction_new[index[np.argsort(np.argsort(trueResult_index))]]

match_user = trueResult[:,0]==prediction_new[:,0]
match_item = trueResult[:,1]==prediction_new[:,1]

for i in range(int(len(prediction)/6)):
    temp_list = prediction_new[6*i:6*(i+1)]
    temp_score = temp_list[:,2]
    temp_score = [x for x in temp_score if x == x]
    temp_median = np.median(temp_score)
    temp_mean = np.mean(temp_score)
    for k in range(6):
        if temp_list[k,2]!=temp_list[k,2]:
            print("Found None at line #%d"%(6*i+k))
            prediction_new[i*6+k,2] = int(temp_mean >= temp_median)
        else:
            prediction_new[i*6+k,2] = int(prediction_new[i*6+k,2] >= temp_median)

match_rating = trueResult[:,2]==prediction_new[:,2]
print("########################################")
np.savetxt("prediction_ordered.txt",prediction_new, delimiter = "|",fmt="%d")
print(match_user.sum(),match_item.sum(),match_rating.sum())
print("Correct rate is %.4f"%(float(match_rating.sum())/float(match_user.sum())))
