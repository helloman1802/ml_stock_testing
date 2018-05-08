import numpy as np
def compute_error_for_line(b, m, points):
    # Initialize error value at 0
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) **2
    return totalError / float(len(points))

def gradient_decent_runner(points, starting_b, starting_m, learning_rate, num_of_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_of_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)

    return [b,m]

def step_gradient(b_current, m_current, points, learning_rate):

    b_gradient = 0
    m_gradient = 0
    
    n = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]

        b_gradient += -(2/n) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/n) * x * (y - ((m_current * x) + b_current))

    # Update b and m values
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def run():
    # Collect data
    points = np.genfromtxt('data.csv', delimiter=',')

    # Define hyperparamaters
    learning_rate = 0.0001
    # y = mx + b
    b_initial = 0
    m_initial = 0
    num_of_iterations = 1000

    # Train model
    print('initial b: {}, initial m: {}, error: {}'.format(b_initial, m_initial, compute_error_for_line(b_initial, m_initial, points)))
    
    [b, m] = gradient_decent_runner(points, b_initial, m_initial, learning_rate, num_of_iterations)

    print('ending b: {}, ending m: {}, ending error: {}'.format(b, m, compute_error_for_line(b, m, points)))


if __name__ == '__main__':
    run()