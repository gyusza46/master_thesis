# portfólió varinciája
def portfolio_variance(weights, cov_matrix):
    return weights.T @ cov_matrix @ weights

# portfólió hozama
def portfolio_return(weights, mean_returns):
    return np.dot(weights, mean_returns)

# max portfoliohoz
def portfolio_return_neg(weights, mean_returns):
    return -np.dot(weights, mean_returns)

# hasznossági függvény negativan adom meg hogy minimalizalni kelljen 
def utility_function(weights, gamma):
    return -portfolio_return(weights) + gamma/2 *portfolio_variance(weights)

