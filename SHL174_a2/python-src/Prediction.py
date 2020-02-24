import Filtering
def prediction(evidence_data_add, prior, start_day, end_day):
    # you need to implement this method.

    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]
    # get filtering probability of the last day(day 100)
    filter_last = Filtering.filtering(evidence_data_add,prior,100)[-1]

    # based on the probability of day 100, predict the future day by day
    for i in range(start_day, end_day+1):
        x_prob_rain.append(filter_last*0.7+(1-filter_last)*0.3)
        filter_last = x_prob_rain[-1]

    return x_prob_rain




# following lines are main function:
evidence_data_add = "..//data//assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
for i in range(start_day, end_day+1):
    print("Day " + str(i) + ": rain " + str(x_prob_rain[i-start_day]) + ", sunny " + str(1 - x_prob_rain[i-start_day]))
    # print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))