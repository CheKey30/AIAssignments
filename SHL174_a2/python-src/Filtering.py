def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.
    # predefined the probabilities in transition model and sensor model
    p_r_r = 0.7
    p_r_s = 0.3
    p_u_r = 0.9
    p_u_s = 0.2
    p_nu_r = 0.1
    p_nu_s = 0.8
    alepha = 0.9
    # read umbrella information form txt and save as list
    file = open(evidence_data_add)
    line = file.readline().strip()
    umbrella =[]
    while line:
        umbrella.append(not ("no" in line))
        line = file.readline().strip()
    x_prob_rain = [prior[0]]
    # x_prob_sunny[i] = 1 - x_prob_rain[i]
    # calculate the probability day by day
    for i in range(100):
        pr = p_r_r*x_prob_rain[-1]+p_r_s*(1-x_prob_rain[-1])
        if(umbrella[i-1]):
            pur = alepha*p_u_r*pr
        else:
            pur = alepha*p_nu_r*pr
        x_prob_rain.append(pur)
        
    return x_prob_rain




# following lines are main function:
evidence_data_add = "..\\data\\assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))